import machine
import time


def main():
    # Initialize ADC on GPIO 26 (ADC0)
    adc = machine.ADC(26)

    print("Reading microphone output...")
    while True:
        # Read the ADC value (0-65535 for 16-bit resolution)
        mic_value = adc.read_u16()
        print("Mic Output:", mic_value)

        # Add a small delay to avoid flooding the output
        time.sleep(0.1)


if __name__ == "__main__":
    main()
