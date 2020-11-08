%Written by:
%Last modified:
clear al; close all; clc

%variables
p = linspace(0,600,1000);
pref = 2*10^-5;
spl = 20*log10(p/pref);

%plot
subplot(2,1,1);
plot(p,spl);
subplot(2,1,2);
loglog(p,spl);