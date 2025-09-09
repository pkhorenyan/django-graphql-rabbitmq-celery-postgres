import graphene
from apps.users.schema import Query as UsersQuery, Mutation as UsersMutation
from apps.files.schema import Query as FilesQuery, Mutation as FilesMutation

class Query(UsersQuery, FilesQuery, graphene.ObjectType):
    pass

class Mutation(UsersMutation, FilesMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)



# import graphene
# from apps.users.schema import Query as UsersQuery, Mutation as UsersMutation
#
# class Query(UsersQuery, graphene.ObjectType):
#     pass
#
# class Mutation(UsersMutation, graphene.ObjectType):
#     pass
#
# schema = graphene.Schema(query=Query, mutation=Mutation)