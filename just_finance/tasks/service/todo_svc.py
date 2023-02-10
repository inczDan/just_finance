from urllib import request
from ..models import Todo , Note



def add_todo(new_task):
    todo = Todo(description=new_task)
    todo.save()
    return todo.to_dict_json()


def list_todos():
    user = request.user
    notes = Note.objects.filter(user=user)
    return [note.to_dict_json() for note in notes]

def list_notes():
    notes = Note.objects.all()
    return [note.to_dict_json() for note in notes]