from django.shortcuts import render,redirect,HttpResponse
import requests
from django.http import JsonResponse
import openai
from openai import api_key
import requests
from IPython.display import HTML
from django.contrib.auth.decorators import login_required

API_KEY = "YEA0AN5T0V1YRL33L93469UXAE58X14AU1I"
API_KEY2 = 'IA2RXD0U0MXL1UDB3PRKSXIQWNIR88QXMM5'

@login_required(login_url='/')
def HOME(request):
    return render(request, 'Hod/home.html')
@login_required(login_url='/')
def CHEM(request):
    return render(request, 'Hod/chem.html')


def hod_chat(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        input_text = request.POST.get('input_text', '')  # Get the input text from the AJAX request

        url = f"https://api.betterapi.net/youchat?inputs={input_text}&key={API_KEY}"  # Set API URL
        response = requests.get(url).json()  # Load JSON from API
        generated_text = response.get('generated_text', '')  # Extract the generated text

        return JsonResponse({'generated_text': generated_text})

    return JsonResponse({'error': 'Invalid request'})


def chem_chat(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        input_text = request.POST.get('input_text', '')  # Get the input text from the AJAX request

        url = f"https://api.betterapi.net/youchat?inputs={input_text}&key={API_KEY2}"  # Set API URL
        response = requests.get(url).json()  # Load JSON from API
        generated_text = response.get('generated_text', '')  # Extract the generated text

        return JsonResponse({'generated_text': generated_text})

    return JsonResponse({'error': 'Invalid request'})
