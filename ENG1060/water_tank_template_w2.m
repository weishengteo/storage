% Written by: ???, ID: 12345678
% Last modified: ???
clear all; close all; clc;
%% part a
% variables
radius = 1:1:15;
volume = 800;

% height rearranged from volume equation
height = (volume - ((2*pi*radius.^3)/3))./(pi*radius.^2);

% costs rearranged from surface area
cost_cylin = 2*pi*radius.*height*300;
cost_hemi = 2*pi*(radius.^2)*400;
total_cost=cost_cylin+cost_hemi;

% Plot graph
plot(radius,total_cost)
title('Graph of water tank radius vs cost')
xlabel('Radius')
ylabel('Cost')
grid on


%% part b
%finding minimum cost
[mincost, pos] = min(total_cost);
corr_r = radius(pos);
corr_h = height(pos);

%plotting minimum point
hold on
plot(corr_r,mincost,'r*');
hold off