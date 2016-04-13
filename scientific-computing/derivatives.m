function derivatives
h = 10.^(-16:1:-1);
f1 = (sin(1+h) - sin(1))./h;
subplot(2, 2, 1);
loglog(h, abs(f1-cos(1)));
xlabel('h');
ylabel('||error||');
title('cos(1)-forward divided difference');

f2 = (sin(1+h)-sin(1-h))./(2*h);
subplot(2, 2, 2);
loglog(h, abs(f2-cos(1)));
xlabel('h');
ylabel('||error||');
title('cos(1)-central divided difference');

m = 1+(10^6)*pi;
f3 = (sin(m+h) - sin (m))./h;
subplot(2, 2, 3);
loglog(h, abs(f3-cos(m)));
xlabel('h');
ylabel('||error||');
title('cos(1+10e6*pi)-forward divided difference');

f4 = (sin(m+h) - sin (m-h))./(2*h);
subplot(2, 2, 4);
loglog(h, abs(f4-cos(m)));
xlabel('h');
ylabel('||error||');
title('cos(1+10e6*pi)-central divided difference');