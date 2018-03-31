from string import punctuation
import json

#create hashmap based on scraped idioms from json file
with open("idioms-a.json", "r") as file:
    hashmap = json.load(file)

#Input text from the user
text = "all the more"


def main(text):
    text = ''.join(c for c in text if c not in punctuation).lower()
    for phrase in hashmap:
        if phrase in text:
            translation = hashmap[phrase]
            return translation

x = main(text)
print (x)
