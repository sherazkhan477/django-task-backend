from django.urls import path
from django.http import JsonResponse
from .views import Task

# Root API landing response
def home(request):
    return JsonResponse({"message": "Task Zen API is live 🚀"})

urlpatterns = [
    path('', home, name='home'),  # Root route for basic health check or info

    # Task routes
    path('users/<int:user_id>/tasks/<int:task_id>', Task.as_view(), name='task_detail'),
    path('users/<int:user_id>/tasks', Task.as_view(), name='task_list'),
]
