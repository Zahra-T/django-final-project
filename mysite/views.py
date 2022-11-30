from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post
from django.utils import timezone
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    posts=Post.objects.filter(published_date__lte=timezone.now())[:3]
    Post.objects.filter(published_date__lte=timezone.now(), status=0).update(status=1)
    context={'posts':posts}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message submited successfully.')
        else:
            messages.error(request, 'Sorry, something went wrong. we didn\'t recive your message.')
            pass
        return redirect('mysite:contact')
    form=ContactForm()
    return render(request, 'contact.html', {'form':form})

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "accounts/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'zahraeset@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return render(request, 'accounts/password/password_reset_done.html')
			messages.error(request, 'An invalid email has been entered.')
			return redirect('password_reset')
	password_reset_form = PasswordResetForm()
	return render(request, "accounts/password/password_reset.html", {"password_reset_form":password_reset_form})
