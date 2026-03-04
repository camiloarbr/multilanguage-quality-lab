from utils import suma

from palindromo import es_palindromo


# Tests para es_palindromo
def test_radar():
    assert es_palindromo("radar")

def test_radar_mayuscula():
    assert es_palindromo("Radar")

def test_frase_palindromo():
    assert es_palindromo("anita lava la tina")

def test_no_palindromo():
    assert not es_palindromo("python")

def test_cadena_vacia():
    assert es_palindromo("")

# Tests para suma
def test_suma_positivos():
    assert suma(2, 3) == 5

def test_suma_con_cero():
    assert suma(0, 5) == 5

def test_suma_negativos():
    assert suma(-2, 3) == 1