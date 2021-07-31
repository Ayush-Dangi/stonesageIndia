from django.shortcuts import render
from datetime import datetime
import requests

def about_us(request):
    return render(request, 'aboutus/aboutus.html')