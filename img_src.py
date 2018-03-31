from bs4 import BeautifulSoup
import requests
import re
from urllib.request import *
import os
import http.cookiejar
import json

def get_soup(url,header):
    return BeautifulSoup(urlopen(Request(url,headers=header)),'html.parser')


def get_image(query):
    image_type="pic"
    query= query.split()
    query='+'.join(query)
    url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
    #print url
    #add the directory for your image here
    DIR="Pictures"
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
    }
    soup = get_soup(url,header)


    ActualImages=[]# contains the link for Large original images, type of  image

    count = 0
    for a in soup.find_all("div",{"class":"rg_meta"}):
        link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
        ActualImages.append((link,Type))
        count+=1
        break

    #print  ("there are total" , len(ActualImages),"images")

    if not os.path.exists(DIR):
                os.mkdir(DIR)
    DIR = os.path.join(DIR, query.split()[0])

    if not os.path.exists(DIR):
                os.mkdir(DIR)
    ###print images
    for i , (img , Type) in enumerate( ActualImages):
       try:
        req = Request(img, headers={'User-Agent' : header})
        cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1

        if len(Type) == 0:
            f = os.path.join(DIR, image_type + "_" + str(cntr) + ".jpg")
        else:
            f = os.path.join(DIR, image_type + "_" + str(cntr) + "." + Type)

        urlretrieve(ActualImages[0][0], f)

        return f

       except Exception as e:
        print( "could not load : "+img)
    ##        print e

'''
if __name__ == '__main__':
   print (get_image("raining heavily"))
'''