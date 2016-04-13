function out = bisect(func, init_x, lbound, rbound, tol)
a = lbound;
b = rbound;
x = init_x;
out = zeros(1, 1);
counter = 0;
while (b - a > tol)
    counter = counter + 1;
    if (counter > 1)
        x = (a+b)/2;
    end
    if (sign(func(a)) == sign(func(x)))
        a = x;
    elseif (sign(func(x)) == 0)
        if (counter == 1)
            out(1) = x;
        else
            out = [out x];
        end
        break
    else
        b = x;
    end
    if (counter == 1)
        out(1) = x;
    else
        out = [out x];
    end
end
