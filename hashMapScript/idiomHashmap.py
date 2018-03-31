from string import punctuation
import json

#create hashmap based on scraped idioms from json file

with open("test.json", "r") as file:
    hashmap = json.load(file)

text = "Today, it was raining cats and dogs, although a bunch of fives showed up."

def main(text):
    text = ''.join(c for c in text if c not in punctuation).lower()
    for phrase in hashmap:
        if phrase in text:
            print(hashmap[phrase])

main(text)
