from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

from django.core.mail import send_mail
from django.http import HttpResponse

def test_email(request):
    send_mail(
        'Test de mail depuis Django',
        'Si tu lis ceci, le mail est bien parti !',
        config('EMAIL_USER'),  # <-- tu peux mettre config('EMAIL_USER') aussi
        [config('EMAIL_USER')],
        fail_silently=False,
    )
    return HttpResponse("E-mail envoyé !")