from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["POST"])
def add_todo(request):
    return Response("Adding todo")


@api_view(["GET"])
def show_todo(request, todo_id):
    print(f"Passed todo id: {todo_id}")
    return Response("Showing todo...")


@api_view(["GET"])
def show_by_year(request, year):
    print(f"Year is: {year}")

    return Response(f"Year is: {year}")