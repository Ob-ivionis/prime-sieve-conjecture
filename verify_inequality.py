# verify_inequality.py

import argparse
from prime_sieve import PrimeFilter

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify the prime gap inequality a_{k+3} < 2 * a_{k+1}.")
    parser.add_argument("--start", type=int, default=1, help="Starting value of k.")
    parser.add_argument("--end", type=int, default=34000, help="Ending value of k.")
    args = parser.parse_args()

    verifier = PrimeFilter()
    verifier.verify_gap_inequality(args.start, args.end)