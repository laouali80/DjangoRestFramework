from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


@api_view(['GET'])
def usersInfo(request):

    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def userDetail(request, id):
    try:
        user = User.objects.get(pk=id)
    except UnboundLocalError or ValueError:
        return Response("Error 404!! Not found.")
    except User.DoesNotExist:
        return Response("Error 404!! Not found.")
    
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)



@api_view(['POST', 'GET'])
def userCreate(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response("Unsuccess!! an error has occur.")
    
        return Response("Success!! User added.")



@api_view(['PUT', 'GET'])
def userUpdate(request, id):

    try:
        user = User.objects.get(pk=id)
    except UnboundLocalError or ValueError:
        return Response("Error 404!! Not found.")
    except User.DoesNotExist:
        return Response("Error 404!! Not found.")
    
    # if request.method == 'GET':
    #     users = User.objects.all()
    #     serializer = UserSerializer(users, many=True)
    #     return Response(serializer.data)
    
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("Successful data update!!")


@api_view(['DELETE', 'GET'])
def userDelete(request, id):

    # if request.method == 'GET':
    #     users = User.objects.all()
    #     serializer = UserSerializer(users, many=True)
    #     return Response(serializer.data)
    # else:
    try:
        user = User.objects.get(pk=id)
    except UnboundLocalError or ValueError:
        return Response("Error 404!! Not found.")
    except User.DoesNotExist:
        return Response("Error 404!! Not found.")

    user.delete()
    return Response("Successful Deletion of user!!")
