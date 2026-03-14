#code for checking for mistakes and counting the words
import re
from spellchecker import SpellChecker

#declaring a word
typedText = input('Write your text here: ')
print(typedText)
lenghtoftheText = len(typedText)

#dividing by backspace
#typedText=re.findall(r'\b\w+\b', typedText)
typedText = typedText.split()
print(typedText)

#outputting count of words
print(f"Count of the words in the text you have written is {len(typedText)}")

#checking for grammar
corrector = SpellChecker()
for i in range(len(typedText)-1):
    if typedText[i].isalpha() == True:
        if typedText[i] in corrector:
            typedText[i]=typedText[i]
        else:
            typedText[i]=corrector.correction(typedText[i])
    else:
        typedText[i]=typedText[i]
print(type(typedText))

listTextToString = ' '.join([str(element) for element in typedText])

print(f'Your text is "{listTextToString}"')