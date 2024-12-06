import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


def plotAudio(Signal, Fs, TimeMargin=[0, 0.02]):
    """
    Funkcja do rysowania sygnału dźwiękowego i widma w decybelach.

    Parametry:
    - Signal: ndarray, sygnał dźwiękowy
    - Fs: int, częstotliwość próbkowania
    - TimeMargin: list, zakres czasu na osi OX (domyślnie [0, 0.02])
    """
    # Wyznaczenie zakresu próbek
    start_sample = int(TimeMargin[0] * Fs)
    end_sample = int(TimeMargin[1] * Fs)

    # Jeśli sygnał jest wielokanałowy, wybierz tylko pierwszy kanał
    if Signal.ndim > 1:
        Signal = Signal[:, 0]

    # Fragment sygnału do wykresu
    time = np.linspace(0, len(Signal) / Fs, len(Signal))
    time_fragment = time[start_sample:end_sample]
    signal_fragment = Signal[start_sample:end_sample]

    # Obliczenie widma
    fft_values = np.fft.fft(Signal)
    fft_magnitude = np.abs(fft_values[:len(fft_values) // 2])  # Połówka widma
    fft_db = 20 * np.log10(fft_magnitude / np.max(fft_magnitude))  # Wartości w dB
    freqs = np.fft.fftfreq(len(Signal), d=1 / Fs)[:len(fft_values) // 2]

    # Tworzenie wykresów
    plt.figure(figsize=(12, 8))

    # Górny wykres - sygnał w czasie
    plt.subplot(2, 1, 1)
    plt.plot(time_fragment, signal_fragment)
    plt.title("Sygnał dźwiękowy w czasie")
    plt.xlabel("Czas [s]")
    plt.ylabel("Amplituda")
    plt.grid()

    # Dolny wykres - widmo
    plt.subplot(2, 1, 2)
    plt.plot(freqs, fft_db)
    plt.title("Widmo sygnału (połówka)")
    plt.xlabel("Częstotliwość [Hz]")
    plt.ylabel("Amplituda [dB]")
    plt.grid()

    # Ograniczenie zakresu czasu
    plt.xlim(TimeMargin)

    plt.tight_layout()
    plt.show()
