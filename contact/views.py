from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
        'subject': form.cleaned_data['subject'], 
        'from_email': form.cleaned_data['from_email'], 
        'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'lee_yechan@hufs.ac.kr', ['lee_yechan@hufs.ac.kr']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("contactform/contact.html")

	form = ContactForm()
	return render(request, "contactform/contact.html", {'form':form})

def homepage(request):
	return render(request, "polls/index.html")