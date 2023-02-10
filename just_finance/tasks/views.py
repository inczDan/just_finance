# coding: utf-8
import json
from decimal import Decimal as D
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from ..commons.django_views_utils import ajax_login_required
from .service import todo_svc
from .models import Note
from django.shortcuts import get_object_or_404, HttpResponse


@csrf_exempt
@ajax_login_required
def add_todo(request):
    todo = todo_svc.add_todo(request.POST["description"])
    return JsonResponse(todo)


@ajax_login_required
def list_todos(request):
    todos = todo_svc.list_todos()
    return JsonResponse({"todos": todos})

@login_required
def save_nota(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        nome =data.get('nome')
        valor_reais = D(data.get("valor_reais"))
        tipo = data.get("tipo")
        user = request.user
        note = Note.objects.create(
            nome=nome,
            valor_reais=valor_reais,
            tipo=tipo,
            user=user,
        )
        note.save()
        return JsonResponse({'sucess': True})

def mostra_nota(request):
  notes = todo_svc.list_notes(request)
  return JsonResponse({"notes":notes})


# def delete_note(request, pk):
#     note = get_object_or_404(Note, pk=pk)
#     note.delete()
#     return HttpResponse(status=204)
@csrf_exempt
@login_required
def delete_notes(request):
    if request.method == "DELETE":
        body = json.loads(request.body)
        Note.objects.filter(id__in=body["ids"]).delete()
        return JsonResponse({"message": "Notas deletadas com sucesso"})