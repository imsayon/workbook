with open("sample.txt", "r") as file:
    text = file.read()

words = text.split()

clean_words = []
for word in words:
    clean_words.append(word.strip(".,!?;:").lower())

palindromes = []
for word in clean_words:
    if len(word) >= 5 and word == word[::-1]:
        palindromes.append(word)

palindromes.sort(key=len)

print(palindromes)