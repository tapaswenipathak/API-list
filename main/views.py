from django.shortcuts import render, redirect
from main.forms import RegisterForm
from twilio.rest import Client
from django.contrib import messages

# Create your views here.
def homepage(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			sendSms(form.data.get('phone_number'))
			messages.success(request, f"You have been registered successfully")
			return redirect("main:homepage")
	else:
		form = RegisterForm()
	return render(request, 'main/home.html', {'form': form})

def sendSms(phone_number):
	account_sid = "AC2380c7d75df5d70337e8de3ca514e6ec"
	account_token = "c8144d0944b4f6ae842c042fc3a689a1"
	phone_number = "+91" + phone_number
	client = Client(account_sid, account_token)

	client.messages.create(to=phone_number, from_="+12053405484", body="This is sent using python")