from django.http import JsonResponse

def welcome_message(request):
    message = "Welcome to My Django API!"
    return JsonResponse({'message': message})