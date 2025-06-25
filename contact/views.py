from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Message de succès
            messages.success(request, "Votre message a été envoyé avec succès !")

            # Envoi d’un email
            subject = "Nouveau message de contact"
            message = (
                f"Nom : {contact.nom}\n"
                f"Prénom : {contact.prenom}\n"
                f"Email : {contact.email}\n\n"
                f"Message :\n{contact.message}"
            )
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.CONTACT_EMAIL]  # à définir dans settings.py

            try:
                send_mail(subject, message, from_email, recipient_list)
            except Exception as e:
                messages.warning(request, "Le message a été enregistré mais l'email n'a pas pu être envoyé.")

            return redirect('contact')  # Redirection pour éviter le double envoi
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

