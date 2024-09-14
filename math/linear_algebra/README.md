# Linear Algebra
This project covers concepts in linear algebra

1. **What is a vector?**
   - A **vector** is a one-dimensional array of numbers. In mathematics, it can be thought of as a list of numbers arranged in a row or a column. For example, \([1, 2, 3]\) is a row vector and \(\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}\) is a column vector. Vectors represent quantities with both magnitude and direction in physics and engineering contexts.

2. **What is a matrix?**
   - A **matrix** is a two-dimensional array of numbers, arranged in rows and columns. For example, \(\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\) is a 2x2 matrix. Matrices are used in linear algebra to represent systems of equations, transformations, and more.

3. **What is a transpose?**
   - The **transpose** of a matrix is an operation that flips the matrix over its diagonal. This means rows become columns and columns become rows. For example, the transpose of \(\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}\) is \(\begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix}\).

4. **What is the shape of a matrix?**
   - The **shape** of a matrix refers to its dimensions, i.e., the number of rows and columns. For example, a matrix with 3 rows and 4 columns has the shape \((3, 4)\). In general, the shape is written as \((m, n)\), where \(m\) is the number of rows and \(n\) is the number of columns.

5. **What is an axis?**
   - In the context of matrices and arrays, an **axis** refers to a specific dimension of the array. For a 2D matrix, axis 0 refers to rows, and axis 1 refers to columns. In higher-dimensional arrays, there may be more axes, each representing a different dimension.

6. **What is a slice?**
   - A **slice** is a way to extract a subset of elements from an array or matrix. It allows you to select specific rows, columns, or both from the original array. Slicing is done using indices or ranges of indices.

7. **How do you slice a vector/matrix?**
   - You slice a vector or matrix by using index notation. For example, in Python, given a vector `v = [1, 2, 3, 4]`, `v[1:3]` will return `[2, 3]`. For a matrix `M`, you can slice it like `M[0:2, 1:3]`, which will return a submatrix consisting of the first two rows and the second and third columns.

8. **What are element-wise operations?**
   - **Element-wise operations** are mathematical operations applied to each element of an array individually. For example, given two matrices `A` and `B` of the same shape, adding them together element-wise means that each element in `A` is added to the corresponding element in `B`. Similarly, element-wise multiplication would multiply corresponding elements from the two matrices. 

9. **How do you concatenate vectors/matrices?**
   - **Concatenation** involves joining two or more vectors or matrices along a particular axis. For example, you can concatenate two vectors `[1, 2, 3]` and `[4, 5, 6]` to form `[1, 2, 3, 4, 5, 6]`. For matrices, concatenation depends on the shape. You can concatenate matrices either row-wise (axis 0) or column-wise (axis 1). In Python's NumPy library, this can be done using functions like `np.concatenate()`, `np.vstack()` (for vertical concatenation), and `np.hstack()` (for horizontal concatenation).

10. **What is the dot product?**
   - The **dot product** is an operation that takes two vectors of the same size and returns a single scalar value. For two vectors \(\mathbf{a} = [a_1, a_2, \dots, a_n]\) and \(\mathbf{b} = [b_1, b_2, \dots, b_n]\), the dot product is calculated as:
     \[
     \mathbf{a} \cdot \mathbf{b} = a_1b_1 + a_2b_2 + \dots + a_nb_n
     \]
     This operation is widely used in physics, engineering, and machine learning to compute things like projections and angles between vectors.

11. **What is matrix multiplication?**
   - **Matrix multiplication** is a more complex operation than element-wise multiplication. Given two matrices \(A\) (of shape \(m \times n\)) and \(B\) (of shape \(n \times p\)), their product is a new matrix \(C\) (of shape \(m \times p\)), where each element \(C_{ij}\) is the dot product of the \(i\)-th row of \(A\) and the \(j\)-th column of \(B\). It can be written as:
     \[
     C_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}
     \]
     Matrix multiplication is used for linear transformations, solving systems of linear equations, and more.

12. **What is NumPy?**
   - **NumPy** is a popular Python library for scientific computing. It provides powerful tools for working with arrays (vectors, matrices, and higher-dimensional arrays), enabling efficient computation of mathematical operations like matrix multiplication, dot products, and element-wise functions. It’s widely used in data analysis, machine learning, and computational mathematics because it optimizes operations using highly efficient C-based implementations.

13. **What is parallelization and why is it important?**
   - **Parallelization** refers to the process of dividing a computational task into smaller subtasks that can be executed simultaneously on multiple processors or cores. This allows for faster computation, especially in large-scale problems like matrix operations, simulations, or data processing. Parallelization is crucial for high-performance computing (HPC) and modern applications like machine learning, where massive datasets and complex models require extensive computation.

14. **What is broadcasting?**
   - **Broadcasting** is a technique used in array operations, particularly in NumPy, where arrays of different shapes are automatically expanded to be compatible for element-wise operations. For example, if you add a scalar to a vector, or a vector to a matrix, the scalar or vector will be "broadcasted" across the elements of the larger array. This allows for efficient and intuitive operations without needing to explicitly reshape arrays. Broadcasting simplifies code and optimizes performance when dealing with arrays of different shapes.
