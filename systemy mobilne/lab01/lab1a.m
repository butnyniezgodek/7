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

d1=1:0.25:100;
d2=1:0.25:10000;

p1=zeros(1,length(d1));
p2=zeros(1,length(d1));
p3=zeros(1,length(d2));
p4=zeros(1,length(d2));

for i= 1:length(d1)
    p1(i)=10*log(GT*GR*(lam1/(4*pi*d1(i)))^2);
    p2(i)=10*log(GT*GR*(lam2/(4*pi*d1(i)))^2);
end

figure;
plot(d1, p1, 'r-', 'LineWidth', 1);
hold on
plot(d1, p2, 'b--', 'LineWidth', 1);
hold off

title('Wykres względnego spadku mocy.');
xlabel('odleglość - [m]');
ylabel('moc - [dB]');
legend('900MHz', '2400MHz'); % Legenda
grid on; % Włączenie siatki

for j= 1:length(d2)
    p3(j)=10*log(GT*GR*(lam1/(4*pi*d2(j)))^2);
    p4(j)=10*log(GT*GR*(lam2/(4*pi*d2(j)))^2);
end

figure;
plot(d2, p3, 'r-', 'LineWidth', 1);
hold on
plot(d2, p4, 'b--', 'LineWidth', 1);
hold off

title('Wykres względnego spadku mocy.');
xlabel('odleglość - [m]');
ylabel('moc - [dB]');
legend('900MHz', '2400MHz'); % Legenda
grid on; % Włączenie siatki