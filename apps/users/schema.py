import graphene
from .queries import Query as UsersQuery
from .mutations import Mutation as UsersMutation

class Query(UsersQuery, graphene.ObjectType):
    pass

class Mutation(UsersMutation, graphene.ObjectType):
    pass