%Task8
clear all; close all; clc;

%Creating vector X
X = [1:10].^2

%Prob1
Y1 = X(3:3:end)

%Prob2
Y2 = sqrt(Y1)

%Prob3
Y3 = abs(Y1-Y2)

%Prob4
Y4 = Y3.*5

%Concatenation of everything to form vector Y
Y = [Y1;Y2;Y3;Y4]