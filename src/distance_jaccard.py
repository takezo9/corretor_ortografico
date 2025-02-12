from collections import Counter

def jaccard_distance(user_word, words):
    suggestions = []

    # Convert a palavra do usuario em um conjunto
    user_set = set(user_word)

    for dict_word in words:
        # Converte a palavra do dicionario em um conjunto
        dict_set = set(dict_word)

        # intersecção e união
        intersection = len(user_set & dict_set)  
        union = len(user_set | dict_set)        

        if union == 0:
            distance = 0 
        else:
            distance = 1 - (intersection / union)

        suggestions.append({'word': dict_word, 'distance': distance})

    # Ordena as palavras pelo menor valor da distância Jaccard
    suggestions = sorted(suggestions, key=lambda x: x['distance'])
    
    return suggestions[:5]

# Essa versão da função utiliza a similaridade jaccard ponderada, onde leva em conta a ocorrência de cada elemento da string

def weighted_jaccard(word1, word2):
    # conta a frequência de cada caractere nas palavras
    freq1 = Counter(word1)
    freq2 = Counter(word2)

    # interseção: soma das menores ocorrências para cada caractere
    intersection = sum(min(freq1[char], freq2[char]) for char in freq1.keys() & freq2.keys())

    # união: soma das maiores ocorrências para cada caractere
    union = sum(max(freq1[char], freq2[char]) for char in freq1.keys() | freq2.keys())

    return 1 - (intersection / union) if union != 0 else 1  

def jaccard_distance_weighted(user_word, words):
    suggestions = []

    for dict_word in words:
        distance = weighted_jaccard(user_word, dict_word)
        suggestions.append({'word': dict_word, 'distance': distance})

    # Ordena pelas menores distâncias
    suggestions = sorted(suggestions, key=lambda x: x['distance'])

    return suggestions[:5]