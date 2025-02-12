"""
Nesse arquivo é elaborada a função para ler um arquivo txt.
"""
import os

def leitor_txt():
    file_path = os.path.join(os.path.dirname(__file__), '../assets/br-sem-acentos.txt')
    with open(file_path, 'r') as file:
        words = [line.lower() for line in file.read().splitlines()]
    #file = open("assets/br-sem-acentos.txt",'r')
    #words = file.read().splitlines()
    file.close()
    return words

"""
Refs: 
https://hackernoon.com/how-to-read-text-file-in-python
"""