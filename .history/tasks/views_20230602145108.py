from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    
    if request.method == 'GET':
         return render(request, 'signup.html',{
        'form': UserCreationForm
    })

    else:
        if request.POST['password1'] == request.POST['password2']:
            
            
        print('Obteniendo datos')    
        
   
