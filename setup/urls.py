from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')


# Essa é a URL do projeto, onde você cadastra as demais rotas para serem exibidas na url do browser
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
