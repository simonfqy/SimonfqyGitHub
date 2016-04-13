function out = newton(func, dfunc, init_x, root, tol)
x = init_x;
out = zeros(1, 1);
counter = 0;
while (abs(x - root) > tol && counter < 100)
    counter = counter + 1;
    x = x - func(x)/dfunc(x);
    if (counter == 1)
        out(1) = x;
    else
        out = [out x];
    end
    
end