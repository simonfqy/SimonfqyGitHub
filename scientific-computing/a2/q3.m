function q3
% Solving for (a)
f_a = @(x) x^3 - 2*x -5;
df_a = @(x) 3*x^2 - 2;
root_a = fzero(f_a, 4);
a = 2;
b = 4;
x = 4;
results_bis = bisect(f_a, x, a, b, 1e-10);
error_bis = abs(results_bis - root_a);
n_bis = length(results_bis);
results_newton = newton(f_a, df_a, x, root_a, 1e-10);
error_newton = abs(results_newton - root_a);
n_newton = length(results_newton);
%start plotting.
figure
subplot(2,2,1)
plot([1:n_bis], error_bis(1:n_bis), 'r-o', [1:n_newton], error_newton(1:n_newton), 'b-*', 'MarkerSize', 4)
title('Error Plot(a)')
xlabel('Iteration')
ylabel('Error')
legend('Bisection','Newton')
% Solution for (b)
f_b = @(x) exp(-x) - x;
df_b = @(x) -exp(-x) - 1;
root_b = fzero(f_b, 2);
a = 0;
b = 2;
x = 2;
results_bis = bisect(f_b, x, a, b, 1e-10);
error_bis = abs(results_bis - root_b);
n_bis = length(results_bis);
results_newton = newton(f_b, df_b, x, root_b, 1e-10);
error_newton = abs(results_newton - root_b);
n_newton = length(results_newton);
%Plotting
subplot(2,2,2)
plot([1:n_bis], error_bis(1:n_bis), 'r-o', [1:n_newton], error_newton(1:n_newton), 'b-*', 'MarkerSize', 4)
title('Error Plot(b)')
xlabel('Iteration')
ylabel('Error')
legend('Bisection','Newton')

% Solution for (c)
f_c = @(x) x*sin(x);
df_c = @(x) sin(x) + x*cos(x);
root_c = 0;
% Bisection method does not apply, since f(a)f(b)>0
x = 1;
results_newton = newton(f_c, df_c, x, root_c, 1e-10);
error_newton = abs(results_newton - root_c);
n_newton = length(results_newton);
subplot(2,2,3)
plot((1:n_newton), error_newton(1:n_newton), 'b-*', 'MarkerSize', 4)
title('Error Plot(c)')
xlabel('Iteration')
ylabel('Error')
legend('Newton')

% Solution for (d)
f_d = @(x) x^3 - 3*x^2 + 3*x - 1;
df_d = @(x) 3*x^2 - 6*x + 3;
root_d = 1;
% Bisection method can be applied, since f(a)f(b)=0
x = 0;
a = -1;
b = 1;
results_bis = bisect(f_d, x, a, b, 1e-10);
error_bis = abs(results_bis - root_d);
n_bis = length(results_bis);
results_newton = newton(f_d, df_d, x, root_d, 1e-10);
error_newton = abs(results_newton - root_d);
n_newton = length(results_newton);
subplot(2,2,4)
plot((1:n_bis), error_bis(1:n_bis), 'r-o', (1:n_newton), error_newton(1:n_newton), 'b-*', 'MarkerSize', 4)
title('Error Plot(d)')
xlabel('Iteration')
ylabel('Error')
legend('Bisection', 'Newton')