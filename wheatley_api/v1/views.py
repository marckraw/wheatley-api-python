from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FinancialCommitment
from .serializers import FinancialCommitmentSerializer


# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of available routes'
        },
    ]

    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = FinancialCommitment.objects.all()
    serializer = FinancialCommitmentSerializer(notes, many=True) # do we want to serialize multiple objects or single

    return Response(serializer.data)

# @api_view(['POST'])
# def createNote(request):
#     data = request.data
#     note = Note.objects.create(
#         body=data['body']
#     )
#     serializer = NoteSerializer(note, many=False)
#
#     return Response(serializer.data)
#
# @api_view(['GET'])
# def getNote(request, pk): #primary key
#     param = request.GET.get("id")
#     print("This is query param", param)
#
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(note, many=False) # do we want to serialize multiple objects or single
#
#     return Response(serializer.data)
#
# @api_view(['PUT'])
# def updateNote(request, pk):
#     data = request.data
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(instance=note, data=data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
# @api_view(['DELETE'])
# def deleteNote(request, pk):
#     note = Note.objects.get(id=pk)
#     note.delete()
#
#     return Response('Note was deleted!')
