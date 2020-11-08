% Written by: Teo Wei Sheng
% Last modified: ???
clear all; close all; clc;

% Matrices pre-defined
A = [8 7 9 5 7; 9 6 0 5 5; 3 6 0 2 3; 4 6 0 8 9; 2 1 2 1 2];

% Extracting sub matrix
%B = A(row, column)
B = A([1 2 3], [2 3 5])
