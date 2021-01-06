from django.contrib import admin
from django.urls import path
from escola.views import alunos
# Essa é a URL do projeto, onde você cadastra as demais rotas para serem exibidas na url do browser
urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', alunos),
]
