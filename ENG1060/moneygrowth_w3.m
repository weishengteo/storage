%Written by: ???, ID:???
%Date: ????
% money
clear all; close all; clc;

% variables 
P = 1000;
r = 3.5/100;

%% Part 1
% input prompts
n = input('Enter the number of times'); % n: no of times interest compounded
t = input('Enter the number of years'); % t: years


% Amount after t years at n times compounding
disp('The balance after t years at n times compounding:')
A = P*(1+r/n)^(n*t);

% Money earned
% display the appropriate variable here
disp(A);