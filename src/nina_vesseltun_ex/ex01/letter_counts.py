def letter_freq(txt):
    txt = txt.lower()
    found_letters = {}
    for sign in txt:
        if sign in found_letters:
            found_letters[sign] += 1
        if sign not in found_letters:
            found_letters[sign] = 1
    return found_letters


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
