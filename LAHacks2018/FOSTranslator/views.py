from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from FOSTranslator.models import Idiom
from FOSTranslator.serializers import FOSTranslatorSerializer

# Create your views here.
@csrf_exempt
def get_idioms(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET
        text_to_check = request.data.text

        inputIdiom = FOSTranslator.objects.filter(idiom=text_to_check)

        idioms = FOSTranslator.objects.all()
        serializer = FOSTranslatorSerializer(FOSTranslator, many=True)
        return JsonResponse(serializer.data, safe=False)
