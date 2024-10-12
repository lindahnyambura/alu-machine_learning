# There's a pretty high chance that this is probably probability


# Poisson Distribution

Poisson distribution models the probability of a given number of events occurring within a fixed interval of time or space, given a constant average rate (λ or lambtha).

Formula for Poisson Probability Mass Function (PMF):

(google to get reference, I'm not doing the latex ting)

where:
- \( P(X = k) \) is the probability of observing \( k \) events.
- (lambda) is the average number of events in the interval.
- \( k \) is the number of occurrences (events).
- \( e \) is the base of the natural logarithm (approximately equal to 2.71828).
- \( k! \) is the factorial of \( k \).


The Poisson distribution is often used to model random events such as:

- Number of calls received at a call center per hour.
- Number of arrivals at a hospital.
- Number of times a website goes down in a month.

## Poisson Class Implementation
1. **Initialization** (__init__):

We provided two ways to initialize the Poisson distribution:
- Using raw data (data): In this case, the rate (lambtha)is calculated as the mean of the data.
- Using a predefined lambtha value: Directly set the rate if no data is provided.

2. **PMF Method**:
- This method calculates the probability of observing exactly 𝑘 occurrences (successes) in a given interval.
- It uses the Poisson PMF formula
- We ensure k is treated as an integer, and if k is negative, the PMF is 0 (since negative events can't happen)

3. **Factorial Method**:
- We implemented our own method to compute the factorial of a number n since we are not importing libraries

4. **CDF Method**:
- The CDF gives the cumulative probability that the number of occurrences will be less than or equal to k
- It is computed by summing the PMF values from 0 to k.

# Exponential Distribution
The Exponential Distribution is a continuous probability distribution often used to model the time between independent events that occur at a constant average rate. It's widely applicable in fields like reliability engineering, queuing theory, and survival analysis.

## Exponential Class Implementation

1. (*with a British accent*) **Init?**

- same thing as Poission, but when calculating lambtha, we will need to take the inverse of the mean of the data because mu = 1 / lambda soo...

2. **PDF Method**
- check if x is out of range
- we mash up the formula

3. **CDF Method**
- check if x is out of range
- cook the formula

# Normal Distribution
The Normal Distribution is defined by two parameters:

- Mean (𝜇): The average of the data points.
- Standard Deviation (𝜎): Measures the dispersion of the data points around the mean.

The probability density function (PDF) for a normal distribution is given by:

(google the formula fam)

Where:

- 𝑒 is Euler's number (approximately 2.7182818285).
- 𝜋 is the constant pi (approximately 3.1415926536).

## Normal Class Implementation

1. **Constructor** *___init___*:

- Check if data is provided.
- If data is provided:
  - Check if it is a list and contains at least two elements.
  - Calculate the mean and standard deviation from the data.
- If no data is provided, check if the provided mean and stddev are valid.
- Raise appropriate exceptions if conditions are not met.

2. **Z-Score**:
    1. Method z_score(self, x):

        - This method takes a float x as an argument and calculates the z-score based on the current mean and standard deviation of the normal distribution. - It returns the calculated z-score.
    
    2. Method x_value(self, z):

        - This method takes a float z as an argument and calculates the corresponding x-value using the provided z-score, mean, and standard deviation. 
        - It returns the calculated x-value.

3. **PDF Method**
- google the formula bro
- Method pdf(self, x):
    - Takes a float x as an argument.
    - Calculates the PDF value using the normal distribution formula.
    - Returns the calculated PDF value.
    - If the standard deviation is not positive, it returns 0 (although this should be handled by the constructor).