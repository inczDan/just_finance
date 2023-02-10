# coding: utf-8
import json
from decimal import Decimal as D
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from ..commons.django_views_utils import ajax_login_required
from .service import todo_svc
from .models import Note


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
    if request.content_type == 'application/json':
        data = json.loads(request.body)
    else:
        data = request.POST

    nome = data.get("nome")
    valor_reais = data.get("valor_reais")
    tipo = data.get("tipo")
    return JsonResponse({"nome": nome, "valor_reais": valor_reais, "tipo": tipo})

        

def view_notes(request):
    notes = todo_svc.list_todos()
    return JsonResponse({"notes": notes})