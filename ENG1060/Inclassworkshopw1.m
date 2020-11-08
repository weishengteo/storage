%Task3
clear all; close all; clc;

R = [ 400, 5000, 8000, 300 ]

%Resistance if the circuit is connected in series
Rs = sum(R)

%Resistance if the circuit is connected in parallel
Rp = 1/(sum(1./R))