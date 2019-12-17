# Numerical Methods

[![Build Status](https://travis-ci.org/cfgnunes/numerical-methods-python.svg?branch=master)](https://travis-ci.org/cfgnunes/numerical-methods-python)

Numerical methods implementation in Python 3.

If you want these implementations in MATLAB, see [this repository](https://github.com/cfgnunes/numerical-methods-matlab).

## Getting Started

### Prerequisites

This section assumes Ubuntu 16.04 (also tested on Ubuntu 18.04), but the procedure is similar for other Linux distributions. The prerequisites is to install the following packages:

```sh
sudo apt -y install make python3-pip python3-venv
```

For Ubuntu 14.04:

```sh
sudo apt -y install make python3-pip python3.4-venv
```

### Running the examples

To run the main example, use:

```sh
make run
```

## Implementations

#### Solutions of equations

* Bisection method
* Newton method
* Secant method

#### Interpolation

* Lagrange method
* Neville method

#### Algorithms for polynomials

* Briot-Ruffini method
* Newton's Divided-Difference method

#### Numerical differentiation

* Backward-difference method
* Three-Point method
* Five-Point method

#### Numerical integration

* Composite Trapezoidal method
* Composite 1/3 Simpson's method

#### Initial-value problems for ordinary differential equations

* Euler's method
* Taylor's (Order Two) method
* Taylor's (Order Four) method
* Runge-Kutta (Order Four) method

#### Systems of differential equations

* Runge-Kutta (Order Four) method

#### Methods for Linear Systems

* Gaussian Elimination
* Backward Substitution
* Forward Substitution

#### Iterative Methods for Linear Systems

* Jacobi method
* Gauss-Seidel method

## Built With

* [Python](https://www.python.org/) - Programming language used

Other tools:

* [GNU Make](https://www.gnu.org/software/make/) - A build automation tool

## Authors

* Cristiano Nunes - *Developer*
