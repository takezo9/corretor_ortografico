"""
Nesse arquivo é construído o corretor utilizando todas as distancias

Receber um input do usuário: uma palavra com erro ortográfico.
    Ler a palavra do usuário
    Validar e formatar a palavra do usuário
        Usando unidecode: https://stackoverflow.com/questions/19771751/how-to-use-unidecode-in-python-3-3
"""

from txt_reader import leitor_txt
from unidecode import unidecode
from distance_euclid import euclidean_distance
from distance_angular import angular_distance
from distance_levenshtein import levenshtein_distance
from distance_jaccard import jaccard_distance
from distance_jaccard import jaccard_distance_weighted

def input_validator():
    word = input("Insira uma palavra: ").lower().replace(" ","").replace("-","")

    if not word.isalpha: 
        print("Insira uma palavra válida")
        input_validator()
    
    return unidecode(word)

def main():
    
    words = leitor_txt()
    
    #print(words)
    #for word in words: print(word)

    user_word = input_validator()

    euclidean_correction = euclidean_distance(user_word,words)
    angular_correction = angular_distance(user_word,words)
    levenshtein_correction = levenshtein_distance(user_word,words)
    jaccard_correction = jaccard_distance(user_word,words)
    jaccard_correction_weighted = jaccard_distance_weighted(user_word,words)

    #print("Correção euclidiana: ", euclidean_correction)
    #print("Correção angular: ", angular_correction)
    #print("Correção Levenshtein: ", levenshtein_correction)
    #print("Correção Jaccard: ", jaccard_correction)

main()