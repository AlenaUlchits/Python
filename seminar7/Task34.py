

def check(phrase):
    counts = list(map(lambda word: len(list(filter(lambda item: item in vowels, word))), phrase.split()))
    return all(item == counts[0] for item in counts)

vowels = ['а', 'я', 'о', 'ё', 'э', 'е', 'ы', 'и', 'у', 'ю']
good_phrase = 'па-ра-ра рам-пам-па ра-па-дам ра-рам-па'
bad_phrase = 'па-ра-рам пам-ра-рам па-пам па-ра-па-дам'

print(f'{good_phrase} -> {check(good_phrase)}')
print(f'{bad_phrase} -> {check(bad_phrase)}')