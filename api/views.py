from django.http import JsonResponse

def exemplo(request):
    data = {"message": "Olá, esta é a minha API seguindo o padrão MTV!"}
    return JsonResponse(data)