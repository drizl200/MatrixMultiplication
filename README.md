# MatrixMultiplication
This is a graduate school project that looks at a different algorithm for multiplying matrices. 

Here I implement the Strassen Algorithm, a method for multiplying matrices that has a more efficent big O complexity than the normal matrix multiplicaiton process.
The normal process for multiplying matrices (often referred to as the Naive Algorithm) has O(n^3).
The Strassen Algorithm is a recurisve algorithm that has O(n^[log_2 7]) or approximately O(n^[2.801]).
The most interesting piece of implementing the Strassen Algorithm is that it falls within a space of being theoretically/asympotically more efficent than the Naive Algorithm, however, the memory cost of the algorithm still makes it much slower than the Naive Alorithm.

But all is not lost! We can mix the low level efficiency of the Naive Algorithm with the benefits of the Strassen Algorithms ability to hand large matrices and design a "modified Strassen Algorithm". We can choose an arbitrary matrix size within our recursion tree in which we stop recuring through the Strassen Algorithm and instead switch back to the Naive Algorithm. This result is a massive increase in efficiency (for certain sizes of matrices)

-S. Osborn
