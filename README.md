# A Novel Iterative Prime Sieving Algorithm

This repository contains the Python implementation and verification scripts for the research paper titled "A Precise Prime Sieving Algorithm in Iterative Intervals and Its Theoretical Proof".

## Overview

This project introduces a novel algorithm for precisely identifying all prime numbers within specific, dynamically generated intervals. Unlike traditional sieves optimized for speed, this algorithm's value lies in its deep connection to the structure of composite numbers, which allowed for a full theoretical proof of its correctness.

The core components are:
- **`prime_sieve.py`**: The main library file containing the `PrimeFilter` class, which is the engine of the algorithm.
- **`main_verification.py`**: A script to run the large-scale computational verification of the algorithm from a start to an end `n`.
- **`verify_inequality.py`**: An auxiliary tool used to computationally verify a key inequality related to prime gaps, which is a cornerstone of the theoretical proof.
- **`find_prime_index.py`**: A utility to find the precise index of a prime number, used to connect our proof to established number theory results (e.g., Dusart's theorem).

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/Ob-ivionis/prime-sieve-conjecture.git
   cd prime-sieve-conjecture
   ```

2. (Recommended) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Main Verification (Func 1)
To run the primary experiment and verify the algorithm over a range of `n`:
```bash
python main_verification.py --start 4 --end 1000
```
You can change the `--start` and `--end` arguments as needed.

### 2. Inequality Verification (Func 2)
To verify the prime gap inequality used in the proof:
```bash
python verify_inequality.py --start 1 --end 34000
```

### 3. Prime Index Finder (Func 3)
To find the precise index of the prime corresponding to a number (e.g., Dusart's limit):
```bash
python find_prime_index.py 396738
```