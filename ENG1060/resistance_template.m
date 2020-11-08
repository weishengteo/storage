clear all; close all; clc;

%variables
R1 = 270;
R2 = 1000;
R3 = 800;
R4 = 3000;

%calculating the equivalent resistance
%series connection
Rs = R1 + R2 + R3 + R4

%parallel connection
Rp = 1/ ((1/R1) + (1/R2) + (1/R3) + (1/R4))