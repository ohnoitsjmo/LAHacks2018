from string import punctuation
import json
import os
import string

dir_path = os.path.dirname(os.path.realpath(__file__))
j_direct = dir_path[0:-13]+"scraper2/"
#print(j_direct)

hashmap = dict()
#create hashmap based on scraped idioms from json file
for letters in string.ascii_lowercase:
    cur_file = j_direct+"idioms-"+letters+"2.json"
    #print(cur_file)
    with open(cur_file, "r") as file:
      #  print(file)
        temp_dict = json.load(file)
        hashmap.update(temp_dict)
       # print("sucess" +letters)


with open('master.json', 'w') as fp:
    json.dump(hashmap, fp, indent =4)
    fp.write("\n")
#print( hashmap)
#Input text from the user
text = "all the more"


def main(text):
    text = ''.join(c for c in text if c not in punctuation).lower()
    for phrase in hashmap:
        if phrase in text:
            translation = hashmap[phrase]
            return translation

x = main(text)
#print (x)
