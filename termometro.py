class Termometro:
    def __init__(self, temperatura = 0, unidade_medida = 'C'):
        self.unidade_medida = unidade_medida
        self.temperatura = temperatura

    def imprime_temperatura(self):
        return f'{self.temperatura} {self.unidade_medida}'

    def converte_para_celsius(self, temperatura, unidade_medida):
        if unidade_medida == 'F':
            return (temperatura - 32) * 5 / 9
        elif unidade_medida == 'K':
            return temperatura - 273.15
        else:
            return temperatura
        
    def converte_para_fahrenheit(self, temperatura, unidade_medida):
        if unidade_medida == 'C':
            return (temperatura * 9 / 5) + 32
        elif unidade_medida == 'K':
            return (temperatura - 273.15) * 9 / 5 + 32
        else:
            return temperatura
    
    def converte_para_kelvin(self, temperatura, unidade_medida):
        if unidade_medida == 'C':
            return temperatura + 273.15
        elif unidade_medida == 'F':
            return (temperatura - 32) * 5 / 9 + 273.15
        else:
            return temperatura
    