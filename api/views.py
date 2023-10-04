from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Document
import openai
import os
# Create your views here.

openai.api_key = os.getenv("OPENAI_API_KEY")
def index(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == 'POST':
        category = "public"
        uploaded_file = request.FILES['file']
        document = Document()
        document.category = 'public'
        document.file = uploaded_file
        document.name = uploaded_file.name
        document.size = uploaded_file.size

        document.save()
        return redirect('/chat')
        
def chat(request):
    return render(request, 'chat.html')

def channel_chat(request):
    if request.method == 'POST':
        question = request.POST['question']

        
        return HttpResponse(question)

def format(request):
    if request.method == 'POST':
        text = request.POST['text']
        count = len(text.split(' '))
        if count > 10:
            response = "You have exceeded word limit: " + str(count-10)
        else:
            response = generate(text)
        return HttpResponse(response)
        
        
        
def generate(text):
    system_prompt = """
    
    Proof read and re-write the following text using university grade grammar/formatting and improve it's structural flow/cadence
    
    Respond with the information about converted_text, firstName, lastName, email and textbox.
      
      """
    # PROSE Publishing invites newcomers to submit a 1,000-word draft. 
    # Please edit the grammar, spelling, punctuation, spacing, formatting, and readability/clarity, while preserving the original tone of the writer.
    
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ],
      temperature=0.7
    )
    
    return response['choices'][0]['message']['content'] 