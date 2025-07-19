# main_verification.py

import argparse
import time
from prime_sieve import PrimeFilter

def run_iteration_and_verify(start_n, end_n):
    """Runs the main verification experiment for the sieve."""
    print("=" * 70)
    print(f"Starting iterative verification from n = {start_n} to {end_n}...")
    print("=" * 70)

    temp_filter = PrimeFilter()
    temp_filter._ensure_primes_available(end_n + 2)
    max_a1 = temp_filter._primes_list[end_n]
    max_a2 = temp_filter._primes_list[end_n+1]
    ground_truth_limit = max_a1 * max_a2
    
    print(f"Generating ground truth primes up to {ground_truth_limit:,}...")
    sieve_start_time = time.time()
    ground_truth_primes = temp_filter._sieve_up_to(ground_truth_limit)
    ground_truth_set = set(ground_truth_primes)
    print(f"Ground truth generated in {time.time() - sieve_start_time:.2f} seconds.\n")

    main_filter = PrimeFilter()
    all_missed_primes = {}
    all_false_positives = {}

    for n in range(start_n, end_n + 1):
        iter_start_time = time.time()
        print(f"--- Processing n = {n} ---")

        candidates, interval = main_filter.screen_new_primes(n)
        candidates_set = set(candidates)
        
        actual_primes_in_interval = {p for p in ground_truth_set if interval[0] < p < interval[1]}
        
        missed = sorted(list(actual_primes_in_interval - candidates_set))
        false_positives = sorted(list(candidates_set - actual_primes_in_interval))
        
        print(f"Interval: {interval}")
        print(f"Candidate count: {len(candidates_set)}, True prime count: {len(actual_primes_in_interval)}")

        if not missed and not false_positives:
            print(f"Status: SUCCESS! Perfect match.")
        else:
            if missed:
                print(f"Status: FAILED! Missed {len(missed)} primes: {missed}")
                all_missed_primes[n] = missed
            if false_positives:
                print(f"Status: FAILED! Found {len(false_positives)} pseudo-primes: {false_positives}")
                all_false_positives[n] = false_positives
        
        print(f"n={n} processed in {time.time() - iter_start_time:.4f} seconds.\n")

    print("=" * 70)
    print("Final Verification Report")
    print("=" * 70)
    if not all_missed_primes and not all_false_positives:
        print(f"SUCCESS: In all tests from n={start_n} to {end_n}, the algorithm was both complete and precise.")
    else:
        print(f"FAILURE: Errors were detected in the range n={start_n} to {end_n}.")
        # Further error reporting can be added here
    print("=" * 70)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the main verification for the prime sieving algorithm.")
    parser.add_argument("--start", type=int, default=4, help="Starting value of n for verification.")
    parser.add_argument("--end", type=int, default=1000, help="Ending value of n for verification.")
    args = parser.parse_args()
    
    run_iteration_and_verify(args.start, args.end)