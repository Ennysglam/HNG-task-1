
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

class TaskApiView(APIView):


    def get(self, request, *args, **kwargs):
        data={"slack name" : "Ehny", "Backend": "True", "Age": "25", 
                     "Bio": "I am  ehny, an HNG intern, I enrolled for the backend track,\
                      I am ready to learn and input my ultimate best through out  this internship"}
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request,*args, **kwargs):
        operation_type= request.data.get("operation_type")
        x =request.data["x"]
        y = request.data["y"]
        
        if operation_type == "addition" :
            value = x + y

        elif operation_type == "subtraction" :
            value = x - y

        elif operation_type == "multiplication" :
            value = x * y
        else:
            value ="invalid operation_key"
        
        result = {"slackname":"Ehny", "operation_type": operation_type, "result":value}
        return Response(result, status=status.HTTP_201_CREATED)

# Create your views here.
