# coding: utf-8

from django.http import JsonResponse
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



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


def register(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]

# bisu se o email já está em uso
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email já está sendo usado.'})

# bisu se o usuário já existe
        if User.objects.filter(username=name).exists():
            return JsonResponse({'error': 'Nome de usuário já existe.'})

        user = User.objects.create_user(
            username=name,
            email=email,
            password=make_password(password)
        )
        user.save()
        log_svc.log_register(user)
        return JsonResponse({'success': 'Usuário criado com sucesso.'})
    return JsonResponse({'error': 'Método não permitido.'})






# def danielzin(request):
#     return JsonResponse({"nome": "daniel"})
