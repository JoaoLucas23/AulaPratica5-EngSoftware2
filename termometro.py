class Termometro:
    CELSIUS = 'C'
    FAHRENHEIT = 'F'
    KELVIN = 'K'

    def __init__(self, temperatura=0, unidade_medida='C'):
        self._validar_unidade(unidade_medida)
        self.unidade_medida = unidade_medida
        self.temperatura = temperatura

    def _validar_unidade(self, unidade):
        unidades_validas = [self.CELSIUS, self.FAHRENHEIT, self.KELVIN]
        if unidade not in unidades_validas:
            raise ValueError(f'Unidade inválida. As unidades válidas são: {", ".join(unidades_validas)}')

    @property
    def imprime_temperatura(self) -> str:
        return f'{self.temperatura} {self.unidade_medida}'

    @property
    def converte_para_celsius(self) -> float:
        if self.unidade_medida == self.FAHRENHEIT:
            return (self.temperatura - 32) * 5 / 9
        elif self.unidade_medida == self.KELVIN:
            return self.temperatura - 273.15
        else:
            return self.temperatura

    @property
    def converte_para_fahrenheit(self) -> float:
        if self.unidade_medida == self.CELSIUS:
            return (self.temperatura * 9 / 5) + 32
        elif self.unidade_medida == self.KELVIN:
            return (self.temperatura - 273.15) * 9 / 5 + 32
        else:
            return self.temperatura

    @property
    def converte_para_kelvin(self) -> float:
        if self.unidade_medida == self.CELSIUS:
            return self.temperatura + 273.15
        elif self.unidade_medida == self.FAHRENHEIT:
            return (self.temperatura - 32) * 5 / 9 + 273.15
        else:
            return self.temperatura
