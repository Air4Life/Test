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


def main():
    t, signal = generate_signal()
    amplitude = compute_amplitude(signal)
    plt.figure(figsize=(10, 4))
    plt.plot(t, signal, label='Signal')
    plt.plot(t, amplitude, label='Amplitude', alpha=0.7)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title('Generated Audio Signal and Amplitude')
    plt.legend()
    plt.tight_layout()
    plt.savefig('signal.png')


if __name__ == '__main__':
    main()
