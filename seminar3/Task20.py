def getLetters():
    letters = {}
    letters = getLettersForDictionary(letters, 'A, E, I, O, U, L, N, S, T, R', 1)
    letters = getLettersForDictionary(letters,'D, G', 2)
    letters = getLettersForDictionary(letters, 'B, C, M, P', 3)
    letters = getLettersForDictionary(letters, 'F, H, V, W, Y', 4)
    letters = getLettersForDictionary(letters, 'K',5)                                  
    letters = getLettersForDictionary(letters, 'J, X', 8)
    letters = getLettersForDictionary(letters, 'Q, Z', 10)
    letters = getLettersForDictionary(letters, 'А, В, Е, И, Н, О, Р, С, Т ', 1)
    letters = getLettersForDictionary(letters,'Д, К, Л, М, П, У', 2)
    letters = getLettersForDictionary(letters, 'Б, Г, Ё, Ь, Я', 3)
    letters = getLettersForDictionary(letters, 'Й, Ы', 4)
    letters = getLettersForDictionary(letters, 'Ж, З, Х, Ц, Ч',5)                                  
    letters = getLettersForDictionary(letters, 'Ш, Э, Ю', 8)
    letters = getLettersForDictionary(letters, 'Ф, Щ, Ъ', 10)                                 
    return letters
def getLettersForDictionary(letters_dictionary, letters, score):
    for letter in letters.split(', '):
        letters_dictionary[letter] = score
    return letters_dictionary
def getScore(word, dict):
    score = 0
    for letter in range(len(word.strip())):
        score += dict[word[letter].upper()]
    return score
dictionary = getLetters()
word = input('Enter a word scrabble counting: ')
score = getScore(word, dictionary)
print(f'The score of word {word} is {score}')
