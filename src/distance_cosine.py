"""
1 - O que é a similaridade cosseno
    https://www.youtube.com/watch?v=e9U0QAFbfLI&t=106s
    1 - cos(theta)

    <user_vec, dict_vec> / sqrt(<user_vec,user_vec>)*sqrt(<dict_vec,dict_vec>)

2 - Distancia angular = arcos(cos(theta))

"""

import math

from distance_euclid import word_to_ascii

def cosine_distance(user_word, words):

    # armazenando os resultados
    suggestions = []

    # transformando a palavra do usuário em um vetor
    user_word_vector = word_to_ascii(user_word)

    for dict_word in words:
        # transformando a palavra do dicionario em um vetor
        dict_word_vector = word_to_ascii(dict_word)

        # normalizando os vetores quanto ao tamanho
        # obtendo o tamanho maximo entre os vetores
        max_len = max(len(user_word_vector),len(dict_word_vector))

        # extendendo os vetores até que fiquem com o mesmo tamanho
        user_vec = user_word_vector + [0] * (max_len - len(user_word_vector))
        dict_vec = dict_word_vector + [0] * (max_len - len(dict_word_vector))

        # calculando a distancia, sabendo que d_ang = arc(cos(<a,b>))

        cos_similarity = 0
        
        if norm(user_vec) > 0 and norm(dict_vec) > 0:
            cos_similarity = dot_product(user_vec,dict_vec)/(norm(user_vec) * norm(dict_vec))
        else:
            cos_similarity = 0
        
        # distancia em graus
        # angle = math.degrees(math.acos(cos_similarity))
        distance = 1 - cos_similarity

        # armazenando resultado
        suggestions.append({'word': dict_word, 'distance': distance})
    
    suggestions = sorted(suggestions, key=lambda word:word['distance'])

    return suggestions[:5]


def dot_product(vec1, vec2):
    return sum((v1*v2) for v1,v2 in zip(vec1,vec2))

def norm(vec1):
    return math.sqrt(dot_product(vec1,vec1))