import RPi.GPIO as GPIO


class PWM_DAC:
    def __init__(self, gpio_bits, pwm_frequency, verbose=False):
        self.gpio_bits = gpio_bits
        self.pwm_frequency = pwm_frequency
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):
        bits = [int(bit) for bit in bin(number)[2:].zfill(8)]
        GPIO.output(self.gpio_bits, bits)

        if self.verbose:
            voltage = number / 255 * self.dynamic_range
            print(f"Число на вход ЦАП: {number}, биты: {bits}")
            #print(f"Расчётное напряжение: {voltage:.2f} В")

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            if self.verbose:
                print(f"Напряжение выходит за динамический диапазон (0.00 - {self.dynamic_range:.2f} В)")
                #print("Устанавливаем 0.0 В")
            number = 0
        else:
            number = int(voltage / self.dynamic_range * 255)
            self.set_number(number)


if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()