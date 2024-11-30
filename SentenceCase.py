#Capitalize the first letter of every sentence
with open('snowwhite.txt') as file:
    text = file.read()

sentences = text.split(". ")
corrected_Sentences = []

for sentence in sentences:
    sentence = sentence.capitalize()
    sentence = sentence + ". "
    corrected_Sentences.append(sentence)

sentencetext = "".join(corrected_Sentences)
with open('snowwhitecorrected.txt', 'w') as file:
    file.write(sentencetext)
