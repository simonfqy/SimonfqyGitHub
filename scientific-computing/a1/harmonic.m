%(a) Because the harmonic series increases quite slowly, I first guess that
% the sum is in about 10^2 or 10^3 level, or between 2^7 and 2^11. Thus m
% is around 10. Multiplying the exponent by the machine epsilon, we have
% 2^(-14), and in this case k = 2^14 = 16384. To be conservative, let m = 7
% and now the limit would be 2^(-17), k = 2^17 = 131072. So I guess this
% value k would be within 10^4~4*10^5.

%(b)
function [out, sum] = harmonic
sum = single(0);
arrived = false;
k = single(1);
while(~arrived)
    sum2 = sum + single(1/k);
    if (sum2 > sum)
        sum = sum2;
    else
        out = k;
        arrived = true;
    end
    k = k + 1;
end