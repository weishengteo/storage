%Task5
clear all; close all; clc;

Q = 9.81*10^-6;
R = (50/2)*10^-4;
mu = 0.03;
tao = (4*mu/(pi*R^3))*Q

% The variables (Q, R, mu) must be declared before the formula so that the variables actually hold values that can be used to calculate.
% Q is shifted to the right in order to find the value of tao.
% (pi*R^3) must be in a bracket
% The value of R is wrong. 