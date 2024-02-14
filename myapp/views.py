from django.http import JsonResponse

def hello(request):
    data = {'message': 'Hello, world!'}
    return JsonResponse(data)