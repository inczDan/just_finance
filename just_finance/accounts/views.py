# coding: utf-8

#python ./manage.py shell
#importamos  a parte do user e começamos a ver o que tem de bom no banco (jeito rapido)


import json
from django.http import JsonResponse
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User




from ..tasks.service import log_svc

@csrf_exempt
def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)



def logout(request):
    if request.method.lower() != "post":
        raise Exception("Logout only via post")
    if request.user.is_authenticated:
        log_svc.log_logout(request.user)
    auth.logout(request)
    return JsonResponse({})


def whoami(request):
    i_am = (
        {
            "user": _user2dict(request.user),
            "authenticated": True,
        }
        if request.user.is_authenticated
        else {"authenticated": False}
    )
    return JsonResponse(i_am)


def _user2dict(user):
    d = {
        "id": user.id,
        "name": user.get_full_name(),
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "permissions": {
            "ADMIN": user.is_superuser,
            "STAFF": user.is_staff,
        },
    }
    return d


@csrf_exempt
def getstarted(request):
    if request.method == 'POST':
        user_input = json.loads(request.body)
        username = user_input.get("username")
        email = user_input.get("email")
        password = user_input.get("password")
        #easter egg {se voce leu até aqui, bora comer pastel}
        # Verificar se todos os dados foram preenchidos
        if not username or not email or not password:
            return JsonResponse({'error': 'Todos os dados são obrigatórios.'})

        # bisu se o email já está em uso
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email já está sendo usado.'})
        user = User.objects.create_user(
            username=username,
            email=email,
            password= password
        )
        user.save()
        return JsonResponse({'success': 'Usuário criado com sucesso.'})
    else:
        return JsonResponse({'error': 'Metodo não suportado.'})


def novanotacao(request):
    pass
