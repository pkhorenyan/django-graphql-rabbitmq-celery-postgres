import graphene
import graphql_jwt
from django.contrib.auth import get_user_model

class RegisterMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, username, password, email):
        user = get_user_model()(username=username, email=email)
        user.set_password(password)
        user.save()
        return RegisterMutation(success=True)

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()  # Логин
    refresh_token = graphql_jwt.Refresh.Field()          # Обновление токена
    revoke_token = graphql_jwt.Revoke.Field()           # Логаут
    register = RegisterMutation.Field()                  # Регистрация