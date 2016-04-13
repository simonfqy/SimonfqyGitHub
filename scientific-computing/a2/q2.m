%y = a * x ^ b, transform it into log y = b * log x + log a
%We get a = 92.4813, b = -0.4414, so y = 92.4813*(x^(-0.4414))
function [a, b] = q2
x = [2.2 2.6 3.4 4.0];
log_x = log(x);
X = [log_x; 1 1 1 1]';
y = [65 61 54 50];
lnY = (log(y))';
B = X\lnY;
b = B(1);
a = exp(B(2));