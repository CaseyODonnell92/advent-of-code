import sys

def valid_passphrase(phrase, anagrams):
    phrase_dict = {}
    words = [word.strip() for word in phrase.split(" ")]

    if anagrams:
        for i in range(0, len(words)):
            new_word = ""
            for c in sorted(words[i]):
                new_word += c
            words[i] = new_word

    for word in words:
        if phrase_dict.get(word, 0) > 0:
            return False
        phrase_dict[word] = 1
    return True

def num_valid_passphrases(phrases, anagrams=False):
    count = 0
    for phrase in phrases:
        if valid_passphrase(phrase, anagrams):
            count += 1
    return count

if __name__ == "__main__":
    input_file = open("input.txt")
    lines = input_file.readlines()
    input_file.close()

    if len(sys.argv) > 1 and sys.argv[1] == 'b':
        print(num_valid_passphrases(lines, True))
    else:
        print(num_valid_passphrases(lines))