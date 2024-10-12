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
same thing as Poission, but when calculating lambtha, we will need to take the inverse of the mean of the data because mu = 1 / lambda soo...

2. **PDF Method**
- check if x is out of range
- we mash up the formula

3. **CDF Method**
- check if x is out of range
- cook the formula