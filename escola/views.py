from rest_framework import viewsets
from escola.models import Aluno, Curso
from escola.serializer import AlunoSerializer, CursoSerializer

# os ViewSets permitem definir as interações da sua API e permitir que a estrutura REST construa os URLs dinamicamente com um objeto roteador.
# Chamando as classes que foram serializadas e as interpretando para python
class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer