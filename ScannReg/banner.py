

import pyfiglet
from termcolor import colored

def mostrar_banner():
    texto = "\nScannReg"
    ascii_art = pyfiglet.figlet_format(texto, font="4max")
    ascii_coloreado = colored(ascii_art, color="green")
    print(ascii_coloreado)






