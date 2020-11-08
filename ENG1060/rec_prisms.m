function [area, vol] = rec_prisms(h,b,l)
% [area, vol] = rec_prism(h,b,l)
% Written by TBE, 07/11/2018
% 
% Input Arguments
% ---
% h - height
% b - base
% l - length
% Outputs
% ---
% area - area of rectangular prism
% vol - volume of rectangular prism
area = (2*b*h)+(2*b*l)+(2*l*h);
vol = (b*l*h);
end
