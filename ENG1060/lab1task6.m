%Task6
clear all; close all; clc;

% Variable
x = [ -5, pi, exp(1), 999]

% Formula
y = (x.*sin(x))./((x.^3)-2)

% Finding the value of f(-5) x f(999)
value = y(1)*y(4)