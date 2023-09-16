from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def home_consultas(request):
    return HttpResponse("Hello world!") 


def consulta_CNPJ(request):
    cnpj = '09235353000145'
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    return HttpResponse(requests.get(url))

def consulta_CEP(request):
    cep = '59151240'  #8digitos
    url = f'https://viacep.com.br/ws/{cep}/json/'
    
    return HttpResponse(requests.get(url))