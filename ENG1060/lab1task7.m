%Task7
clear all; close all; clc;

A = [8 7 9 5 7; 9 6 0 5 5; 3 6 0 2 3; 4 6 0 8 9; 2 1 2 1 2];
B = [38;-10;44;-7;53];

%Transpose of matrix A
A_T = transpose(A);

%Product of A_T and B
product = A_T*B;

%Sorting result of A_T and B in descending order
sorting = sort(product,'descend');

%Find the square of matrix A
Asquare = A^2;

%Forming a 3x4 matrix from A from 3,4,5 row and 2,3,4,5 column
Anew = A([3 4 5], [2 3 4 5]);

%Forming a 3x4 matrix from A from 2,3,4 row and 1,2,3,4 column
Anew2 = A([2 3 4], [1 2 3 4]);

%Difference between Anew2 and Anew
ANewDiff = Anew - Anew2;

%Element by element square of ANewDiff
ANewDiff.^2