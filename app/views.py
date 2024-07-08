# application/views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm



def index(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        
        # Send email
        send_mail(
            f'Message from {name} ({email})',
            message,
            email,
            [settings.DEFAULT_FROM_EMAIL],  # Replace with your recipient email or use a list of emails
            fail_silently=False,
        )
        return render(request, 'index.html', {'form': form, 'success_message': 'Your message has been sent!'})

    return render(request, 'index.html', {'form': form})

def view_github_project(request):
    return redirect('https://github.com/Kartik-Patil20?tab=repositories')


def view_certificates(request):
    return redirect('https://drive.google.com/drive/folders/1thlH3QUBM-r-sSgdLl-UyKF_tGExEeGT?usp=sharing')