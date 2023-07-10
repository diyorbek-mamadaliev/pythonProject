from django.shortcuts import render,redirect,HttpResponse
import requests
from django.http import JsonResponse
import openai
from openai import api_key
import requests
import json
from IPython.display import HTML
from django.contrib.auth.decorators import login_required

API_KEY = "YEA0AN5T0V1YRL33L93469UXAE58X14AU1I"
API_KEY2 = 'IA2RXD0U0MXL1UDB3PRKSXIQWNIR88QXMM5'
API_KEY3 = 'ZM53SKKYP209H3IQ3L735PUUN9WEOGPFZ13'
API_KEY4 = 'ZM53SKKYP209H3IQ3L735PUUN9WEOGPFZ13'


def HOME(request):
    return render(request, 'Hod/home.html')

def CHEM(request):
    return render(request, 'Hod/chem.html')

def BIO(request):
    return render(request, 'Hod/bio.html')

def BOT(request):
    return render(request, 'Hod/bot.html')


import requests

def hod_chat(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        input_text = request.POST.get('input_text', '')  # Get the input text from the AJAX request

        url = "https://chatgpt-api7.p.rapidapi.com/ask"  # Set API URL
        payload = {"query": input_text,
                   "wordLimit": "1024"}
        headers = {
            "Content-Type": "application/json",
            "X-RapidAPI-Key": "eba8330802mshbce627085fbb152p1609f5jsnc3bcb8954510",
            "X-RapidAPI-Host": "chatgpt-api7.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)
        generated_text = response.json()

        generated_text_str = json.dumps(generated_text)  # Convert generated_text to a string

        return JsonResponse({'generated_text': generated_text_str})

    return JsonResponse({'error': 'Invalid request'})



def chem_chat(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        input_text = request.POST.get('input_text', '')  # Get the input text from the AJAX request

        url = f"https://api.betterapi.net/youchat?inputs={input_text}&key={API_KEY2}"  # Set API URL
        response = requests.get(url).json()  # Load JSON from API
        generated_text = response.get('generated_text', '')  # Extract the generated text

        return JsonResponse({'generated_text': generated_text})

    return JsonResponse({'error': 'Invalid request'})

def bio_chat(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        input_text = request.POST.get('input_text', '')  # Get the input text from the AJAX request

        url = f"https://api.betterapi.net/youchat?inputs={input_text}&key={API_KEY3}"  # Set API URL
        response = requests.get(url).json()  # Load JSON from API
        generated_text = response.get('generated_text', '')  # Extract the generated text

        return JsonResponse({'generated_text': generated_text})

    return JsonResponse({'error': 'Invalid request'})

def bot_chat(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        input_text = request.POST.get('input_text', '')  # Get the input text from the AJAX request

        url = f"https://api.betterapi.net/youchat?inputs={input_text}&key={API_KEY4}"  # Set API URL
        response = requests.get(url).json()  # Load JSON from API
        generated_text = response.get('generated_text', '')  # Extract the generated text

        return JsonResponse({'generated_text': generated_text})

    return JsonResponse({'error': 'Invalid request'})
