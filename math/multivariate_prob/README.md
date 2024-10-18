# Multivariate Probability
It's *normal* I promise

## Mean and Covariance
- **Mean**: This is the average of the data points along each dimension  `np.mean(X, axis=0)`
- **Covariance**: This measures how much two dimensions vary together
Cov(X) = (1/(n-1))Xcentered^T . Xcentered (*hope this makes sense*)
where Xcentered is the matrix after subtracting the mean from each data point

## Correlation...
*... does not imply causation*

The **correlation matrix** can be computed from the **covariance matrix** by normalizing each element. The correlation between two dimensions Xi and Xj is given by:

ρ(Xi,Xj) = (Cov(Xi, Xj)) / (√Var(Xi) . √Var(Xj))

where:
- Cov(Xi, Xj) is the covariance between the dimensions Xi and Xj and
- Var(Xi) is the variance(diagonal elements of the covariance matrix)

1. **Type checks**
2. **Standard deviation**: we extract the variances(diagonal elements of `C`) and take their square root to get the standard deviations
3. **Deniminator**: we create a matrix where element *i, j* is the product of the standard deviations of dimension *i* and dimension *j*
4. **Correlation matrix**: we divide each element of the covariance matrix by the corresponding standard deviation product to get the correlation matrix