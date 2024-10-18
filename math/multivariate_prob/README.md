# Multivariate Probability
It's *normal* I promise

## Mean and Covariance
- **Mean**: This is the average of the data points along each dimension  `np.mean(X, axis=0)`
- **Covariance**: This measures how much two dimensions vary together
$$
\text{Cov}(X) = \frac{1}{n-1} \cdot X_{\text{centered}}^T \cdot X_{\text{centered}}
$$
where Xcentered is the matrix after subtracting the mean from each data point