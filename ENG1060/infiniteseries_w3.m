%Written by: ???, ID:???
%Date: ????
clear all; close all; clc;
%Infinite series
%% part a
%define variables
n=1:100;
terms = ((9/10).^n)./n;
%%
%calculate sum for n up to 10
terms_n10 = terms(1:10);
sum_n10 = sum(terms_n10);

%calculate sum for n up to 20
sum_n20 = sum(terms(1:20));

%calculate sum for n up to 50
sum_n50 = sum(terms(1:50));

%calculate sum for n up to 100
sum_n100 = sum(terms(1:100));

%results in vector
n_plot = [10 20 50 100];
sum_plot = [sum_n10, sum_n20, sum_n50, sum_n100];
%plotting the sums
plot(n_plot, sum_plot,'bd')
xlabel('n')
ylabel('sum of terms')

%% part b
%create a vector for the log10 value
convergence = ones(1,100)*log(10);

%plotting log(10) as red line
hold on
plot(n,convergence,'r-')
xlabel('n')
ylabel('sum of terms')
legend('individual terms','log_e(10)')

%% Example 2b (using loop)
% n_all=1:100;
% terms = ((9/10).^n_all)./n_all;
% sum_terms = zeros(1,100)

% for n = 1:100
%     sum_terms(n) = sum(terms(1:n));
% end
% hold on
% plot(n_all,sum_terms,'bd')
% xlabel('n')
% ylabel('sum of terms')
% hold off