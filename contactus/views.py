from django.shortcuts import render
from .models import ContactUs
from datetime import datetime
import requests

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phoneNumber = request.POST.get('email')
        email = request.POST.get('phoneNumber')
        message = request.POST.get('message')
        date_created = datetime.today()
        contactDetail = ContactUs(
            name=name,
            phoneNumber=phoneNumber,
            email=email,
            message=message,
            date_created=date_created
        )
        contactDetail.save()
        # saverequests.post("https://formspree.io/f/meqpkbyv", data='Name: '+ name + " \n Phone Number: " + phoneNumber +" \n Email: "+email+" \n Message: "+message)
        return render(request, 'contactus/contact.html', { "heading": "Your Request Submitted successfully! Thank you"})
    return render(request, 'contactus/contact.html', { "heading": "!! Thank You For Reaching us !!"})