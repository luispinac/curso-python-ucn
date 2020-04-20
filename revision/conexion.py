import subprocess
import sys

def instalar(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def conectar():
    pip install requests
    pip install -r requirements.txt
    from firebase import firebase
    print("Todo ok")
    return

# class q1():
#     def __init__(self):
#         print("Hola, te estoy saludando desde el __init__"  \
#               "de la clase Saludo")
    
#     def imprimirPrueba1():
#         print("esta es una prueba")

