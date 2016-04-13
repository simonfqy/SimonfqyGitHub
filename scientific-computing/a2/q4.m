function q4
% f(x) = x^5 - x^3 - 4*x
% f'(x) = 5*x^4 - 3*x^2 - 4
% phi(x) = x - f(x)/f'(x)
f = @(x) x^5 - x^3 -4*x;
df = @(x) 5*x^4 - 3*x^2 - 4;
root = fzero(f, 1);

x = 1;
results = newton(f, df, x, root, 1e-10);
disp(results);
% x does not converge if the initial value is 1
% for initial value x0 = 1, newton's method gets values iterating at points
% 1 and -1, never converges to the true root.
x = 2;
results = newton(f, df, x, root, 1e-10);
disp(results);
% x converges to the true root in 5 iterations if the initial value is set to 2