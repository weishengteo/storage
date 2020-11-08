%Written by: ???, ID:???
%Date: ????
clear all; close all; clc;
%Matrix concatentation
%create the A, B and C matrices using eye, ones and zeros
A = eye(2,2);
B = ones(2,2);
C = zeros(2,2);

%create the D matrix by addressing only A, B and C
D = [A, 2*B, C ; C, 2*B, A+1]