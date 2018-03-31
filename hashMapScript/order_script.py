from string import punctuation
import json
import os
import string

dir_path = os.path.dirname(os.path.realpath(__file__))
j_direct = dir_path[0:-13]+"scraper/"
n_direct = dir_path[0:-13]+"scraper2/"
print(j_direct)

hashmap = dict()
#create hashmap based on scraped idioms from json file
for letters in string.ascii_lowercase:
    cur_file = j_direct+"idioms-"+letters+".json"
    n_file = n_direct+"idioms-"+letters+"2.json"

    #print(cur_file)
    readr = open(cur_file, "r")
    writer = open(n_file, "w"   )
    writer.write("{\n")

    for lines in readr:
        if(len(lines) >1 and len(lines) >= 4):
            lines.strip()
            p_time = lines.split('"')
            #print(p_time)
            temp1 , temp2 = p_time[1] , p_time[3]
            if(len(temp1) >=1 and  len(temp2) >=1 ):
                #print('''\\":''')
                if(temp1[0].lower() != letters and temp2[0].lower() != letters or temp1.find('''\\":''') !=-1 or temp2.find('''\\":''') !=-1 ):
                    print(temp1[0] + temp2[0])
                elif (temp1[0].lower() != letters or len(temp1) > len(temp2)):
                    p_time[1], p_time[3] = '"' + temp2 + '"', '"' + temp1 + '"'
                    # print("reversed!")
                    # print(temp1[0].lower() + " " + letters)
                    # print(temp1[0].lower() != letters)
                    # print(len(temp1) > len(temp2))
                    writer.write("".join(p_time))
                else:
                    writer.write(lines)
                #print(temp1[0].lower() + " " + temp2[0].lower() +" "+ letters)

    writer.write("}")
    writer.close()

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
print (x)
