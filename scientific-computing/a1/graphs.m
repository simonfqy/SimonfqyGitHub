%It is actually the work of Hu Mengnan
function graphs
cond_H = zeros(1,11);
cond_A = zeros(1,11);
for n = 2:12
    x0 = ones(n,1);
    H = zeros(n);
    for i = 1:n
        for j = 1:n
            H(i,j) = 1/(i+j-1);
        end
    end
    b = H * x0;
    x_hat = gauss(H,b);
    if max(size(x_hat)) == 1
        cond_A(n-1) = inf;
        cond_H(n-1) = inf;
        break
    end
    r = b - H * x_hat;
    delta_x = x_hat - x0;
    cond_A(n-1) = max(abs(delta_x));
    cond_H(n-1) = cond(H,inf);
end
n = 2:12;
figure
subplot(2,2,1)
semilogy(n,cond_H)
title('Conditional number of H')
subplot(2,2,2)
semilogy(n,cond_A)
title('Conditional number of \Delta x')
cond_Ai = zeros(1,100);
cond_i = zeros(1,100);
n = 1:100;
for i = 1:100
    A = -5 + 10.*rand(12,12);
    x0 = ones(12,1);
    b = A * x0;
    x_hat = gauss(A,b);
    if max(size(x_hat)) == 1
        cond_Ai(i) = inf;
        cond_i(i) = inf;
        break
    end
    r = b - H * x_hat;
    delta_x = x_hat - x0;
    cond_i(i) = max(abs(delta_x));
    cond_Ai(i) = cond(A,inf);
end
subplot(2,2,3)
semilogy(n,cond_Ai)
title('Conditional number of A_i')
subplot(2,2,4)
semilogy(n,cond_i)
title('Conditional number of \Delta x_i')