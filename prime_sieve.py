# prime_sieve.py

import math
import numpy as np
import time

class PrimeFilter:
    """
    Implements and provides tools for analyzing a novel iterative prime sieving algorithm.
    
    This class is the core engine of the research project, containing the definitions
    of the sieve, its optimization, and auxiliary functions used in its proof.
    """
    
    def __init__(self):
        """Initializes the filter with a small list of primes and caches."""
        self._primes_list = [2, 3, 5, 7, 11, 13, 17, 19] # Sequence {a_n}
        self._step_results_cache = {}

    def _ensure_primes_available(self, index):
        """Ensures the internal prime list has at least index+1 primes."""
        if index < len(self._primes_list): return
        num = self._primes_list[-1]
        while len(self._primes_list) <= index:
            num += 2 
            is_prime_flag = True
            for p in self._primes_list:
                if p * p > num: break
                if num % p == 0:
                    is_prime_flag = False
                    break
            if is_prime_flag:
                self._primes_list.append(num)

    def _sieve_up_to(self, limit):
        """Generates primes up to a given limit using a NumPy-optimized Sieve of Eratosthenes."""
        if limit < 2: return []
        is_prime = np.ones(limit + 1, dtype=bool)
        is_prime[0:2] = False
        for p in range(2, int(np.sqrt(limit)) + 1):
            if is_prime[p]: is_prime[p*p::p] = False
        return np.flatnonzero(is_prime).tolist()

    def process_step_123(self, n):
        """Calculates parameters for the n-th iteration (B_n, m_n, etc.)."""
        if n in self._step_results_cache: return self._step_results_cache[n]
        if not isinstance(n, int) or n < 1: raise ValueError("n must be a positive integer.")
        
        self._ensure_primes_available(n + 1)
        a_n, a_n_plus_1 = self._primes_list[n-1], self._primes_list[n]
        limit = a_n * a_n_plus_1
        b_n = self._sieve_up_to(limit)
        m = math.floor(math.log2(limit)) + 1 if limit > 0 else 1

        results = {"n": n, "a_n": a_n, "a_n+1": a_n_plus_1, "limit": limit, "b_n": b_n, "m": m}
        self._step_results_cache[n] = results
        return results

    def _is_in_grid(self, num, b_n_list, b_n_set, m):
        """On-the-fly check if a number belongs to the theoretical composite grid G_n."""
        factor_count = 0
        temp_num = num
        for p in b_n_list:
            if p * p > temp_num: break
            if temp_num % p == 0:
                while temp_num % p == 0:
                    factor_count += 1
                    if factor_count > m: return True
                    temp_num //= p
        if temp_num > 1:
            if temp_num in b_n_set:
                factor_count += 1
                if factor_count > m: return True
            else:
                return False
        return True

    def screen_new_primes(self, n):
        """Runs the main sieving algorithm for the n-th iteration."""
        step_results = self.process_step_123(n)
        m, b_n = step_results['m'], step_results['b_n']
        b_n_set = set(b_n)

        self._ensure_primes_available(n + 1)
        a_n_plus_1, a_n_plus_2 = self._primes_list[n], self._primes_list[n+1]
        start_interval = step_results['limit']
        end_interval = a_n_plus_1 * a_n_plus_2

        candidate_primes = []
        num = start_interval - (start_interval % 6) + 5
        if num <= start_interval: num += 2
        if num % 6 == 3: num += 2
        if num % 6 == 1: pass
        else: num += 4
        
        while num < end_interval:
            if not self._is_in_grid(num, b_n, b_n_set, m):
                candidate_primes.append(num)
            if (num + 2) % 6 == 1:
                num += 2
            else:
                num += 4
        return candidate_primes, (start_interval, end_interval)

    def verify_gap_inequality(self, start_k, end_k):
        """Verifies the inequality a_{k+3} < 2 * a_{k+1}."""
        print(f"Verifying a_{{k+3}} < 2 * a_{{k+1}} for k in [{start_k}, {end_k}]...")
        self._ensure_primes_available(end_k + 2)
        for k in range(start_k, end_k + 1):
            a_k_plus_1 = self._primes_list[k]
            a_k_plus_3 = self._primes_list[k+2]
            if a_k_plus_3 >= 2 * a_k_plus_1:
                print(f"Counterexample found at k={k}: a_{k+3}={a_k_plus_3} >= 2*a_{k+1}={2*a_k_plus_1}")
                return False
        print("Verification successful: No counterexamples found.")
        return True

    def find_prime_index_for(self, target_number):
        """Finds the first prime >= target_number and its precise index."""
        sqrt_limit = int(math.sqrt(target_number + 2000))
        primes_for_check = self._sieve_up_to(sqrt_limit)
        
        p = target_number if target_number % 2 != 0 else target_number + 1
        while True:
            is_p_prime = True
            for prime_divisor in primes_for_check:
                if prime_divisor * prime_divisor > p: break
                if p % prime_divisor == 0:
                    is_p_prime = False
                    break
            if is_p_prime:
                break
            p += 2
        
        print(f"Found prime p = {p}")
        print("Calculating precise index (pi(p))...")
        primes_up_to_p = self._sieve_up_to(p)
        index = len(primes_up_to_p)
        return p, index