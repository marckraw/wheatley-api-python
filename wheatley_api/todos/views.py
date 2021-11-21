from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def add_todo(request):
    return HttpResponse("Adding todo")


def show_todo(request, todo_id):
    print(f"Passed todo id: {todo_id}")
    return HttpResponse("Showing todo...")