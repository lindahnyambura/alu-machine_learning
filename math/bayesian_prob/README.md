# Bayesian Probability Project

This repository contains solutions to a series of tasks focused on Bayesian probability. Each task progressively builds upon concepts such as likelihood, intersection, marginal probability, and posterior probability, implementing them with Python while adhering to specific constraints. The only allowed imports are `numpy` and `scipy.special`, unless otherwise noted.

## Table of Contents
- [General Overview](#general-overview)
- [Tasks](#tasks)
  - [Task 1: Likelihood Calculation](#task-1-likelihood-calculation)
  - [Task 2: Intersection Calculation](#task-2-intersection-calculation)
  - [Task 3: Marginal Probability](#task-3-marginal-probability)
  - [Task 4: Posterior Calculation](#task-4-posterior-calculation)
  - [Task 5: Posterior Probability for a Specific Range](#task-5-posterior-probability-for-a-specific-range)
- [Requirements](#requirements)

## General Overview

This project involves applying Bayesian statistics to a case study about a revolutionary cancer drug. The aim is to compute various probabilities regarding the likelihood of severe side effects among patients using the drug. Each task in this project breaks down the components of Bayes' theorem, including likelihood, marginal, and posterior probabilities. We assume binomial distribution behavior for the data, and tasks include validation checks to ensure input correctness.

## Tasks

### Task 1: Likelihood Calculation

**File:** `0-likelihood.py`

This task calculates the likelihood of observing a specific number of patients with severe side effects given a total number of patients and various hypothetical probabilities. The function uses the binomial distribution formula.

**Function:** `def likelihood(x, n, P):`

- `x`: Number of patients that developed side effects
- `n`: Total number of patients observed
- `P`: A numpy array of hypothetical probabilities

### Task 2: Intersection Calculation

**File:** `1-intersection.py`

This task calculates the intersection of obtaining the observed data with various hypothetical probabilities, taking into account the prior beliefs.

**Function:** `def intersection(x, n, P, Pr):`

- `x`: Number of patients that developed side effects
- `n`: Total number of patients observed
- `P`: A numpy array of hypothetical probabilities
- `Pr`: A numpy array of prior beliefs

### Task 3: Marginal Probability

**File:** `2-marginal.py`

This task computes the marginal probability of obtaining the observed data across all hypothetical probabilities. The marginal is computed as the sum of the intersections.

**Function:** `def marginal(x, n, P, Pr):`

- `x`: Number of patients that developed side effects
- `n`: Total number of patients observed
- `P`: A numpy array of hypothetical probabilities
- `Pr`: A numpy array of prior beliefs

### Task 4: Posterior Calculation

**File:** `3-posterior.py`

This task calculates the posterior probability for the various hypothetical probabilities of developing side effects given the observed data, based on Bayes' theorem.

**Function:** `def posterior(x, n, P, Pr):`

- `x`: Number of patients that developed side effects
- `n`: Total number of patients observed
- `P`: A numpy array of hypothetical probabilities
- `Pr`: A numpy array of prior beliefs

### Task 5: Posterior Probability for a Specific Range

**File:** `100-continuous.py`

This task calculates the posterior probability that the probability of developing severe side effects falls within a specified range, assuming a uniform prior distribution.

**Function:** `def posterior(x, n, p1, p2):`

- `x`: Number of patients that developed side effects
- `n`: Total number of patients observed
- `p1`: Lower bound on the range
- `p2`: Upper bound on the range

## Requirements

- Python 3.x
- `numpy`
- `scipy.special`

## How to Use

Clone the repository and run each Python script with your desired input values. The functions will raise appropriate errors if the inputs do not meet the specified conditions.

Example:
```bash
$ python3 0-likelihood.py
