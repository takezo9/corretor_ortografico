def distance_levenshtein(X, Y):
    m, n = len(X), len(Y)
    
    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        table[i][0] = i  
    for j in range(n + 1):
        table[0][j] = j  
 
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            
            custo = 0 if X[i - 1] == Y[j - 1] else 1
            table[i][j] = min(
                table[i - 1][j] + 1,     
                table[i][j - 1] + 1,     
                table[i - 1][j - 1] + custo  
            )

    return table[m][n]

def levenshtein_distance(user_word, words):

    suggestions = []

    for dict_word in words:
        
        distance = distance_levenshtein(user_word, dict_word)
        if distance == 0: continue
        
        suggestions.append({'word': dict_word, 'distance': distance})

    suggestions = sorted(suggestions, key=lambda word: word['distance'])
    
    return suggestions[:5]