import subprocess
import sys

def instalar(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def instalar2(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", package])

def configurarFirebase():
    from firebase import firebase
    firebase2 = firebase.FirebaseApplication("https://python-ucn-2020.firebaseio.com/", None)
    return firebase2
    


def configurar():
    instalar('requests')
    instalar2('requirements.txt')
    fircon = configurarFirebase()
    data = {
        'Profesor': 'Luis Piña',
        'Nombre': 'Andres Silva',
        'Email': 'andres@alumnos.ucn.cl'
    }
    return fircon, data

# def conectar():
#     pip install requests
#     pip install -r requirements.txt
#     from firebase import firebase
#     print("Todo ok")
#     return

# class q1():
#     def __init__(self):
#         print("Hola, te estoy saludando desde el __init__"  \
#               "de la clase Saludo")
    
#     def imprimirPrueba1():
#         print("esta es una prueba")

