# find_prime_index.py

import argparse
import sympy
from prime_sieve import PrimeFilter

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the precise index for a target number.")
    parser.add_argument("target", type=int, help="The target number (e.g., 396738 for Dusart's theorem).")
    args = parser.parse_args()

    indexer = PrimeFilter()
    prime_found, index_calculated = indexer.find_prime_index_for(args.target)
    
    print("\n" + "="*70)
    print("Calculation Result")
    print("="*70)
    print(f"First prime >= {args.target:,} is: {prime_found:,}")
    print(f"Calculated index (pi(p)): {index_calculated:,}")
    print("="*70)

    print("\n" + "="*70)
    print("Cross-verification with SymPy")
    print("="*70)
    prime_sympy = sympy.nextprime(args.target - 1)
    index_sympy = sympy.primepi(prime_sympy)
    print(f"SymPy found prime: {prime_sympy:,}")
    print(f"SymPy calculated index: {int(index_sympy):,}")

    if prime_found == prime_sympy and index_calculated == int(index_sympy):
        print("\nSUCCESS: Results match SymPy perfectly.")
    else:
        print("\nFAILURE: Results do not match SymPy.")
    print("="*70)