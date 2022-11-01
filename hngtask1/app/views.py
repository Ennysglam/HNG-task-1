
from django.http import JsonResponse

def index(request):
    return JsonResponse({"slack name" : "Ehny", "Backend": "True", "Age": "25", 
                     "Bio": "I am  ehny, an HNG intern, I enrolled for the backend track, I am ready to learn and input my ultimate best through out  this internship"})

# Create your views here.
