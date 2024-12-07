close all
clear all
clc

GT = 1.6;
GR = 1.6;

c=299792458;
f1=900000000;
f2=2400000000;

lam1=c/f1;
lam2=c/f2;

h1=30;
h2=3;

d=1:0.25:10000;

d1=sqrt((h1-h2)^2+d.^2);
d2=sqrt((h1+h2)^2+d.^2);

z1=abs(exp(1i*(-2)*pi*f1.*d1/c)./d1 - exp(1i*(-2)*pi*f1.*d2/c)./d2);
z2=abs(exp(1i*(-2)*pi*f2.*d1/c)./d1 - exp(1i*(-2)*pi*f2.*d2/c)./d2);

p1=10*log(GT*GR*(lam1/4*pi)^2.*z1);
p2=10*log(GT*GR*(lam2/4*pi)^2.*z2);

figure;
plot(d, p1, 'r-', 'LineWidth', 1);
hold on
plot(d, p2, 'b--', 'LineWidth', 1);
hold off

title('Wykres względnego spadku mocy.');
xlabel('odleglość - [m]');
ylabel('moc - [dB]');
legend('900MHz', '2400MHz'); % Legenda
grid on; % Włączenie siatk