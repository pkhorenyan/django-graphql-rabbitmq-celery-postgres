from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Django app is up and running. Django + RabbitMQ/Redis + Celery + Postgres.")