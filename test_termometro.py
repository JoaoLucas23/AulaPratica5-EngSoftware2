from termometro import Termometro

def test_cria_termometro_padrao():
    termometro = Termometro()
    assert termometro.temperatura == 0
    assert termometro.unidade_medida == 'C'

def test_cria_termometro_com_temperatura_medida_padrao():
    termometro = Termometro(temperatura = 10)
    assert termometro.temperatura == 10
    assert termometro.unidade_medida == 'C'

def test_cria_termometro_com_temperatura_e_medida():
    termometro = Termometro(temperatura = 10, unidade_medida = 'F')
    assert termometro.temperatura == 10
    assert termometro.unidade_medida == 'F'

def test_imprime_temperatura():
    termometro = Termometro(temperatura = 10, unidade_medida = 'F')
    assert termometro.imprime_temperatura() == '10 F'

def test_converte_kelvin_para_celsius():
    termometro_kelvin = Termometro(temperatura = 273.15, unidade_medida = 'K')
    assert termometro_kelvin.converte_para_celsius() == 0

def test_converte_fahrenheit_para_celsius():
    termometro_fahrenheit = Termometro(temperatura = 32, unidade_medida = 'F')
    assert termometro_fahrenheit.converte_para_celsius() == 0

def test_converte_celsius_para_fahrenheit():
    termometro_celsius = Termometro(temperatura = 0, unidade_medida = 'C')
    assert termometro_celsius.converte_para_fahrenheit() == 32

def test_converte_kelvin_para_fahrenheit():
    termometro_kelvin = Termometro(temperatura = 273.15, unidade_medida = 'K')
    assert termometro_kelvin.converte_para_fahrenheit() == 32

def test_converte_celsius_para_kelvin():
    termometro_celsius = Termometro(temperatura = 0, unidade_medida = 'C')
    assert termometro_celsius.converte_para_kelvin() == 273.15

def test_converte_fahrenheit_para_kelvin():
    termometro_fahrenheit = Termometro(temperatura = 32, unidade_medida = 'F')
    assert termometro_fahrenheit.converte_para_kelvin() == 273.15

def test_unidade_medida_invalida():
    try:
        termometro_invalido = Termometro(unidade_medida='X')
        assert False, "Deveria ter lançado uma exceção para unidade inválida"
    except ValueError as e:
        assert str(e) == 'Unidade inválida. As unidades válidas são: C, F, K'