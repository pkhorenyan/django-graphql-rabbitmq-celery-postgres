import graphene
from .queries import Query
from .mutations import Mutation

class FilesQuery(Query, graphene.ObjectType):
    pass

class FilesMutation(Mutation, graphene.ObjectType):
    pass