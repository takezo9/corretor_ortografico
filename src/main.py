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
from distance_cosine import cosine_distance
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
    cosine_correction = cosine_distance(user_word,words)
    levenshtein_correction = levenshtein_distance(user_word,words)
    jaccard_correction = jaccard_distance(user_word,words)
    jaccard_correction_weighted = jaccard_distance_weighted(user_word,words)
    
    print("Euclidiana:",", ".join(dict["word"] for dict in euclidean_correction))
    print("Cosseno:", ", ".join(dict["word"] for dict in cosine_correction))
    print("Levenshtein:",", ".join(dict["word"] for dict in levenshtein_correction))
    print("Jaccard:",", ".join(dict["word"] for dict in jaccard_correction))
    print("Jaccard (Ponderada):",", ".join(dict["word"] for dict in jaccard_correction_weighted))

    """ Para ver o valor das distâncias
    print("Euclidiana:",", euclidean_correction)
    print("Cosseno:", angular_correction)
    print("Levenshtein:", levenshtein_correction)
    print("Jaccard:", jaccard_correction)
    print("Jaccard (Ponderada):", jaccard_correction_weighted)
    """

main()