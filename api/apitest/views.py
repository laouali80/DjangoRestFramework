from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from django.core.exceptions import ValidationError

@api_view(['GET', 'POST'])
def usersInfo(request):
    
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                # print(serializer.errors)
                return Response("Email already exist! Please try with another email.")
            
        except ValidationError as e:
            return Response("Unsuccess!! an error has occur.")
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)        


@api_view(['GET','PUT', 'DELETE'])
def userDetail(request, id):
    try:
        user = User.objects.get(pk=id)
    except UnboundLocalError or ValueError:
        return Response("Error 404!! Not found.", status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response("Error 404!! Not found.", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':

        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
            user.delete()
            return Response("Successful Deletion of user!!", status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
