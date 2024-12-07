% Parametry
v = 3e8; % Prędkość sygnału (np. światła w próżni) w m/s
s = 0:100:1e6; % Odległości od 0 do 1 000 000 m, krok co 100 m

% Obliczanie opóźnień
t = s / v; % Czas opóźnienia w sekundach

% Wykres
figure;
plot(s, t, 'b-', 'LineWidth', 1); % Rysowanie wykresu
grid on; % Włączenie siatki
title('Opóźnienie sygnału w zależności od odległości');
xlabel('Odległość s (m)');
ylabel('Opóźnienie t (s)');