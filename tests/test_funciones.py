from src.logica.funciones import saludar

def test_saludar():
    assert saludar("Mundo") == "¡Hola, Mundo!"