def reverse_sentence(sentence):
    words = sentence.split(" ")

    reverse = ' '.join(reversed(words))

    return reverse

sentence = "reverse this string"

print (reverse_sentence(sentence))