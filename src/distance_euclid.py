"""
1 - Ordenar o alfabeto de acordo com a tabela ascii
    printando um caracter ascii pelo seu código: https://forum.micropython.org/viewtopic.php?t=7282
    obtendo o codigo de um char ascii: ord()

2 - Calcula a distância euclidiana entre uma palavra inserida pelo usuário e uma lista de palavras do dicionário.
    Retorna as 5 sugestões com as menores distâncias.
"""

import math

def euclidean_distance(user_word, words):
    # Criando uma lista vazia que armazenara um dicionario
    corrections = []

    # transformando a palavra do usuário em um 'vetor' ascii
    user_word_vector = word_to_ascii(user_word)

    for word in words:
        # transformando a palavra do dicionario em um 'vetor' ascii
        word_vector = word_to_ascii(word)

        # obtendo o maior tamanho entre as duas palavras
        max_len = max(len(user_word_vector), len(word_vector))

        # extendendo os vetores até que fiquem com o mesmo tamanho e preenchendo esses novos espaços com zeros
        user_vec = user_word_vector + [0] * (max_len - len(user_word_vector))
        word_vec = word_vector + [0] * (max_len - len(word_vector))

        # calculando a distância
        distance = math.sqrt(sum((v1 - v2) ** 2 for v1, v2 in zip(user_vec, word_vec)))

        if (distance == 0):
            continue

        # adicionando o resultado a lista
        corrections.append({'word': word, 'distance': distance})

    # ordenando pela menor distancia
    corrections = sorted(corrections, key=lambda word: word['distance'])

    # retornando as cinco menores distancias
    return corrections[:5]


def word_to_ascii(word: str): 
    return [ord(char) for char in word]