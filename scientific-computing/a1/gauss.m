function out = gauss(A, b)
if (size(A, 1) ~= size(A,2))
    error('The input matrix is not square matrix.');
end
Aug = [A, b];
dim = size(b, 1);
perm = (1:dim)';

for i = 1:(dim-1)
    if (all(Aug(i:dim, i)) == 0)
        continue
    end
    [M, I] = max(abs(Aug(i:dim, i)));
    if ((I-1) ~= 0)
       store = perm(i);
       perm(i) = perm(I+i-1);
       perm(I+i-1) = store;
       storeRow = Aug(i,:);
       Aug(i, :) = Aug(I+i-1, :);
       Aug(I+i-1, :) = storeRow;
       M = Aug(i, i);
       %M is the pivotal value chosen.
    end
    for j = (i+1):(dim-1)
        divisor = Aug(j, i)/M;
        Aug(j, :) = Aug(j, :) - divisor*Aug(i, :);
    end    
end

if (all(Aug(dim, 1:dim) == 0))
    error('The input matrix is singular');
end
b = Aug(:, (dim+1));
out1 = ones(dim, 1);
out = ones(dim, 1);
out1(dim) = b(dim)/Aug(dim, dim);
for i = ((dim-1): -1: 1)
    sum = 0;
    for j = (dim: -1: i+1)
        sum = sum + Aug(i, j)*out1(j);
    end
    out1(i) = (b(i) - sum)/Aug(i, i);
end

for i = 1:dim
    j = perm(i);
    out(j) = out1(i);
end

