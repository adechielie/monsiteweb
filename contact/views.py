from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm
from .gmail_service import send_gmail


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Préparation de l'email
            subject = "Nouveau message de contact"
            message = (
                f"Nom : {contact.nom}\n"
                f"Prénom : {contact.prenom}\n"
                f"Email : {contact.email}\n\n"
                f"Message :\n{contact.message}"
            )

            try:
                # Appel à l’API Gmail
                if send_gmail(settings.CONTACT_EMAIL, subject, message):
                    messages.success(request, "Votre message a été envoyé avec succès !")
                else:
                    messages.warning(request, "Votre message a été enregistré mais l'email n'a pas pu être envoyé.")
            except Exception as e:
                messages.warning(request, f"Erreur lors de l’envoi du mail : {e}")

            # Redirection pour éviter le double envoi
            return redirect('contact_succes')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def contact_succes(request):
    return render(request, 'contact/contact_succes.html')
