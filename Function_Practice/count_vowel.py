def count_vowels(sentence):
    vowel_count = 0

    sentence = sentence.lower()

    for ch in sentence:
        if ch in "aeiou":
            vowel_count += 1

    return vowel_count

sentence = input("Enter your sentence or word : ")
print(count_vowels(sentence))
