function z = poly(x, y) 
% Written by TBE 25/10/2018
% Calculates a series of values ...
sqrd = x.^2 + y.^1 ; 
cubed = x.^3 + y.^2 ; 
quart = x.^4 + y.^3 ; 
z = [ sqrd ; cubed; quart ]; 