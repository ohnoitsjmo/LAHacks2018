import json
import os
os.environ['DJANGO_SETTINGS_MODULE']='LAHacks2018.settings'
import django
django.setup()
from FOSTranslator.models import Idiom

with open('../hashMapScript/master.json', 'r') as file:
     masterhashmap = json.load(file)

for idiom in masterhashmap:
    i = Idiom(idiom=idiom, definition=masterhashmap[idiom])
    i.save()
    print(idiom)
