# Recovering Locations From Distances
## Problem Description
Given all pairs of distances between a set of points, I recover the locations of the points such that their pairwise distances remain the same. The pairs of distances is given in the form of a n x n matrix. Each entry in the matrix will contain the euclidean distance between two points.

#### Specifically for this problem:
Given a matrix that contains the distances between different cities I will recover the locations of the cities so that their distances given in the matrix are maintained.

## Solution and Proof
Given the distance matrix D, we can find the gram matrix of the set of points P (nxn matrix). We can use eigenvalue decomposition to recover the matrix P, which contains the locations of the points. Singular value decomposition generalizes the eigendecomposition to asymetric matrices (non-square). 

Proof: [image]

## Figures
Heatmap of the euclidian distances
Plot of estimated city locations

