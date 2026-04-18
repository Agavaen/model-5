from django.http import JsonResponse
from .models import Student, Teacher

def people(request):
    return JsonResponse({"ok": True})