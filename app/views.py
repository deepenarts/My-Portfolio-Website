from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render


def home(request):
    return render(request,'home.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        if name and email and subject and message:
            try:
                send_mail(
                    subject,
                    f"Name: {name}\nEmail: {email}\nMessage: {message}",
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER],  # You can change this to your email address
                    fail_silently=False,
                )
                
                messages.success(request, 'Your message has been sent successfully!')
            except Exception as e:
                messages.error(request, 'An error occurred while sending the email. Please try again later.')
        else:
            messages.error(request, 'Please fill in all required fields.')

        return redirect('contact')

    return render(request, 'home.html')
