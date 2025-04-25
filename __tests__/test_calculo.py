# Script para utilização em testes de unidade
# 1- Bibliotecas e framwork e referencias externas
import pytest
# Funções que serão testadas
from calculo.calculo import calculo_area_quadrado, calculo_area_retangulo, calculo_area_triangulo
from utils.utils import ler_csv

# 2- Testes
def test_calculo_area_quadrado():
    l = 5
    resultado_esperado = 25
    resultado_obtido = calculo_area_quadrado(l)
    assert resultado_esperado == resultado_obtido

def test_calculo_area_retangulo():
    l = 5
    h = 6
    resultado_esperado = 30
    resultado_obtido = calculo_area_retangulo(l, h)
    assert resultado_esperado == resultado_obtido

def test_calculo_area_triangulo():
    b = 6
    h = 6
    resultado_esperado = 18                             # O resultado esperado deve ser dividido por 2
    resultado_obtido = calculo_area_triangulo(b, h)
    assert resultado_esperado == resultado_obtido

# Tests utilizando massa de teste (lista) para calculo da area do retangulo = Data Driven Test (DDT)
@pytest.mark.parametrize('l, h, resultado_esperado',
                         [                                 
                             (5, 7, 35),                
                             (2, 4, 8),
                             (6, 4, 24),
                             (6, 3.75, 22.5)
                         ]
                        )
def test_calculo_area_retangulo_lista(l, h, resultado_esperado):
    resultado_obtido = calculo_area_retangulo(l, h)
    assert resultado_esperado == resultado_obtido

# Tests utilizando massa de teste de um arquivo csv, para calculo da area do triangulo
@pytest.mark.parametrize('b, h, resultado_esperado',   
                        ler_csv('./fixtures/massa_calculo_triangulo.csv')   # Botão direito no arquivo massa / Copy Relative Path
                        )
def test_calculo_area_triangulo_csv(b, h, resultado_esperado):
    resultado_obtido = calculo_area_triangulo(float(b), float(h))
    assert float(resultado_esperado) == resultado_obtido
