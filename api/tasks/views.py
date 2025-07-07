from django.http import JsonResponse
from django.views import View
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.http import Http404
import json
from .models import Tasks


class Task(View):
    @method_decorator(require_http_methods(['GET']))
    def get(self, request, user_id, task_id=None):
        try:
            user = get_object_or_404(User, id=user_id)
        except Http404:
            return JsonResponse({'response': 'user not found'}, status=404)
        
        if task_id is not None:
            try:
                task = get_object_or_404(Tasks, id=task_id, user=user)
                task_data = {
                    'title': task.title,
                    'description': task.description
                }
                return JsonResponse({'task': task_data}, status=200)
            except Http404:
                return JsonResponse({'response': 'task not found'}, status=404)

        tasks = Tasks.objects.filter(user=user)
        tasks_data = [{'title': task.title, 'description': task.description} for task in tasks]
        return JsonResponse({'tasks': tasks_data}, status=200)

    @method_decorator(require_http_methods(['POST']))
    def post(self, request, user_id):
        try:
            user = get_object_or_404(User, id=user_id)
        except Http404:
            return JsonResponse({'response': 'user not found'}, status=404)

        try:
            request_data = json.loads(request.body)
            title = request_data.get('title')
            description = request_data.get('description')

            if not title or not description:
                return JsonResponse({'response': 'title and description are required'}, status=400)

            new_task = Tasks(user=user, title=title, description=description)
            new_task.save()

            return JsonResponse({'response': {'id': new_task.id, 'message': 'created'}}, status=201)

        except Exception as e:
            return JsonResponse({'response': f'error: {str(e)}'}, status=400)
