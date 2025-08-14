import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def generate_signal(freq=440, sample_rate=44100, duration=1.0):
    """Generate a sine wave audio signal."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # amplitude 0.5 sine wave
    signal = 0.5 * np.sin(2 * np.pi * freq * t)
    return t, signal


def compute_amplitude(signal):
    """Compute amplitude of the signal (absolute value)."""
    return np.abs(signal)


def compute_ema(signal, alpha=0.1):
    """Compute exponential moving average of a signal."""
    ema = np.zeros_like(signal)
    ema[0] = signal[0]
    for i in range(1, len(signal)):
        ema[i] = alpha * signal[i] + (1 - alpha) * ema[i - 1]
    return ema


def main():
    t, signal = generate_signal()
    amplitude = compute_amplitude(signal)
    ema = compute_ema(amplitude)
    plt.figure(figsize=(10, 4))
    plt.plot(t, signal, label='Signal')
    plt.plot(t, amplitude, label='Amplitude', alpha=0.7)
    plt.plot(t, ema, label='EMA', alpha=0.7)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title('Generated Audio Signal, Amplitude and EMA')
    plt.legend()
    plt.tight_layout()
    plt.savefig('signal.png')


if __name__ == '__main__':
    main()
