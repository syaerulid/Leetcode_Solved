class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.8 + 32]

class Kelvin(Solution):
    def convertTemperature(self, kelvin: float) -> List[float]:
        celsius = kelvin - 273.15
        super().convertTemperature(celsius)


class Fahrenheit(Solution):
    def convertTemperature(self, fahrenheit: float) -> List[float]:
        celsius = (fahrenheit - 32) / 1.8
        super().convertTemperature(celsius)
