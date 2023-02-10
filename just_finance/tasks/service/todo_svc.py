from urllib import request
from ..models import Todo , Note



def add_todo(new_task):
    todo = Todo(description=new_task)
    todo.save()
    return todo.to_dict_json()


def list_notes(request):
    notes = Note.objects.filter(user=request.user)
    return [note.to_dict_json() for note in notes]

# def apagar_notes(request, id):
#     notes = Note.objects.filter()