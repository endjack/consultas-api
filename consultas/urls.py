from django.urls import path
from .views import *

urlpatterns = [
    path('', home_consultas, name='consultas'),
    path('cnpj', consulta_CNPJ, name='consulta_cnpj'),
    path('cep', consulta_CEP, name='consulta_cep'),
]