from .models import Colours
from .serializers import ColoursSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def colours_list(request, format=None):
    #GET REQUESTING \\ ALSO MULTIPLE REQUEST
    if request.method == 'GET':
        colours = Colours.objects.all() #get all drinks
        serializer = ColoursSerializer(colours, many=True) #serialise 
        return JsonResponse({'colours' :serializer.data})

    if request.method == 'POST':
        serializer = ColoursSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def colours_details(request, id, format=None):
    try:
        colours = Colours.objects.get(pk=id)
    except Colours.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = ColoursSerializer(colours)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer  =ColoursSerializer(colours, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        colours.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

