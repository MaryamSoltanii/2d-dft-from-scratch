# 2D DFT from Scratch – Line Pattern (x = y)

## Overview
This repository demonstrates a **manual implementation of the 2D Discrete Fourier Transform (DFT)** based directly on its mathematical definition.

A simple synthetic image containing a diagonal line (x = y) is used to clearly illustrate:
- Frequency domain behavior
- Magnitude spectrum
- Phase spectrum

No FFT functions are used.

## What Is Implemented
- Generation of a 64×64 grayscale image with a diagonal line (x = y)
- Manual nested-loop computation of the 2D DFT
- Manual calculation of:
  - Magnitude: √(Re² + Im²)
  - Phase: atan2-based logic (explicit conditions)
- Visualization of:
  - Original image
  - Magnitude spectrum
  - Phase spectrum

## Why This Is Useful
- Understanding Fourier Transform fundamentals
- Educational purposes in Digital Image Processing
- Verifying frequency-domain properties of simple geometric patterns

## Requirements
- Python 3.x
- NumPy
- Matplotlib

Install dependencies:
```bash
pip install numpy matplotlib

<img width="1530" height="524" alt="image" src="https://github.com/user-attachments/assets/19046e2c-717e-4832-967d-0576592b69d3" />

