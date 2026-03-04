from palindromo import es_palindromo
from utils import suma

# Tests para es_palindromo
def test_radar():
    assert es_palindromo("radar") == True

def test_radar_mayuscula():
    assert es_palindromo("Radar") == True

def test_frase_palindromo():
    assert es_palindromo("anita lava la tina") == True

def test_no_palindromo():
    assert es_palindromo("python") == False

def test_cadena_vacia():
    assert es_palindromo("") == True

# Tests para suma
def test_suma_positivos():
    assert suma(2, 3) == 5

def test_suma_con_cero():
    assert suma(0, 5) == 5

def test_suma_negativos():
    assert suma(-2, 3) == 1