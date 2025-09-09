import graphene
from graphene_django import DjangoObjectType
from .models import File

class FileType(DjangoObjectType):
    class Meta:
        model = File
        fields = ('id', 'user', 'name', 'file', 'uploaded_at', 'line_count', 'status')