import graphene
from graphql import GraphQLError

from .models import File
from .types import FileType

class Query(graphene.ObjectType):
    user_files = graphene.List(FileType, user_id=graphene.ID(required=True))

    def resolve_user_files(self, info, user_id):
        # Проверяем аутентификацию
        user = info.context.user
        if not user.is_authenticated:
            raise GraphQLError("Authentication required.")

        # Проверяем, что запрашиваемый user_id совпадает с текущим пользователем
        if str(user.id) != str(user_id):
            raise GraphQLError("You can only view your own files.")

        # Получаем файлы пользователя
        return File.objects.filter(user_id=user_id)