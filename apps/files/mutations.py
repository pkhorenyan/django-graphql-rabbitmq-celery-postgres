# import graphene
# from graphene_file_upload.scalars import Upload
# from graphene_django import DjangoObjectType
# from .models import File
# from graphql import GraphQLError

from .types import FileType
import graphene
from graphene_file_upload.scalars import Upload
from .models import File
from graphql import GraphQLError
from .tasks import process_file  # Импорт задачи

class UploadFileMutation(graphene.Mutation):
    class Arguments:
        file = Upload(required=True)
        name = graphene.String(required=True)

    file = graphene.Field(FileType)  # Импорт из types.py

    def mutate(self, info, file, name):
        user = info.context.user
        if not user.is_authenticated:
            raise GraphQLError("Authentication required.")

        # Сохраняем файл с начальным статусом 'pending'
        file_instance = File(user=user, name=name, file=file, status='pending')
        file_instance.save()

        # Отправляем задачу в очередь Celery
        process_file.delay(file_instance.id)

        return UploadFileMutation(file=file_instance)

class Mutation(graphene.ObjectType):
    upload_file = UploadFileMutation.Field()


