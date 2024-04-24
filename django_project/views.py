from django.shortcuts import render

import requests
def index(request):
  r1=requests.get('https://api.github.com/events')
  data = r1.json()
  events = data[0]["id"]
  
                    
  return render(request,'templates/index.html',{'events':events})
