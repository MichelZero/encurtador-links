#
# autor: Michel
# data: 31/08/2024
#

# criar um encurtador de links

# importar a biblioteca pyshorteners
import pyshorteners

# criar uma variável para armazenar o link
link = input("Digite o link: ")

# criar uma objeto da classe Shortener da biblioteca pyshorteners para encurtar o link
encurtador = pyshorteners.Shortener()

# criar uma variável para armazenar o link encurtado
link_encurtado = encurtador.tinyurl.short(link)

# imprimir o link encurtado
print("Link encurtado: ", link_encurtado)

# fim do programa
