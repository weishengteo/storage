clear all; close all; clc;

%list two different ways to create vector A
A = [13 27 41 55 69];
A = linspace(13,69,5)

%defining B
B = [20 40 80 60 10];

%what is the result of Z=A.*B?
Z = A.*B

%create the following matrices by only addressing A and B vectors
C = [B ; A]
D = [A([1 4 5]) ; B([1 3 5])]