<h1 align="center">COE 352: Advanced Scientific Computation</h1>
<p align="center">
  <b>Coursework Repository for Fall 2024</b><br />
  Instructor: Corey Trahan
</p>

<br />

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#purpose)

# Purpose
This repository contains the coursework for COE 352, focusing on advanced scientific computation techniques and methodologies. The projects within this repository aim to deepen understanding and application of scientific computation in various contexts.

<br />

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#homework)

# Homework
- **[Homework 3](HW/hw3.ipynb)**: A finite difference analysis for Forward Euler, Backward Euler, and Trapezoidal Method.
  
<br />

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#projects)

# Projects
- **[Project 1](Project_1)**: A linear spring-mass system solver using an explicitly coded SVD decomposition (for computing matrix inversions).
### Files:
- **`linear_spring.py`**: The main script that implements the linear spring-mass system solver. This file contains the logic for setting up the system, applying forces, and solving for displacements using the SVD method.
  
- **`mysvd.py`**: An implementation of the Singular Value Decomposition (SVD) algorithm. This file includes the Gram-Schmidt process and other required computations to facilitate matrix inversion.
  
- **`test_linear_spring.py`**: A set of unit tests for validating the functionality of the `linear_spring.py` script. This file uses `pytest` to ensure the accuracy of the spring-mass system solver.
  
- **`test_svd.py`**: A collection of unit tests for the SVD implementation in `mysvd.py`. This file also employs `pytest` to confirm that the SVD calculations are correct and reliable.

<br />

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#installation)

# Installation
To get started with the coursework, follow the instructions below

## Setting Up Repository
1. Clone the repository:
  ```bash
  # Clone the repository
  git clone https://github.com/yourusername/COE352-Coursework.git
  
  # Navigate into the project directory
  cd COE-352
  ```
2. Install **`requirements.txt`** file:
  ```bash
  pip install -r requirements.txt
  ```
   
## Running Tests with pytest

To ensure the quality of the code, we use `pytest` for running our test suite. Follow the instructions below to set up and run the tests.

Once `pytest` has been installed (run the **`requirements.txt`** file), to test the files, particularly for **[Project 1](Project_1)**:
1. Navigate to project/homework directory:
   ```bash
   cd Project_1
   ```
2. Run `pytest`:
   ```bash
   pytest
   ```
