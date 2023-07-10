import uuid
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.context_processors import auth
from django.contrib.auth.models import User
from .form import UserFileForm



from dashboard.models import UserFile, Utilisateur
# Create your views here.
def index(request):
    
    return render(request, 'hello.html', {'name': 'salwa'})

def signup(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST.get('username')
        Cin = request.POST.get('Cin')
        Nom = request.POST.get('Nom')
        Prenom = request.POST.get('Prenom')
        Email = request.POST.get('Email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        role = request.POST.get('role')

        # Validation and user creation logic
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('signup/')

        myuser = User.objects.create_user(username=username, email=Email, password=pass1)

        # Generate a unique ID
        ID = str(uuid.uuid4())[:100]

        utilisateur = Utilisateur.objects.create(
            User=myuser, ID=ID, Cin=Cin, Nom=Nom, Prenom=Prenom, Email=Email
        )
        
        # Set role based on selection
        if role == 'authoritaire':
            utilisateur.is_authoritaire = True
        elif role == 'client':
            utilisateur.is_client = True
        utilisateur.save()

        messages.success(request, "Your account has been successfully created")
        return redirect('/login/')

    return render(request, 'signup.html')
    


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            utilisateur = Utilisateur.objects.get(User=user)
            if utilisateur.is_authoritaire:
                auth_login(request, user)
                return render(request, 'hello_autho.html', {'authenticated_user': user})
            elif utilisateur.is_client:
                auth_login(request, user)
                return render(request, 'hello_cl.html', {'authenticated_user': user})

        messages.error(request, "Invalid credentials! Please try again")
        return redirect('/login/')

    return render(request, 'login.html')

from django.contrib.auth import logout as auth_logout

def signout(request):
    auth_logout(request)
    messages.success(request, "Successfully logged out")
    return render(request, 'hello.html')

def authoritaire(request):
    return render(request, 'hello_autho.html')

def client(request):
    return render(request, 'hello_cl.html') 
  
def demande(request):
    return render(request, 'demande.html')

def hello_cl(request):
    user_files = UserFile.objects.filter(utilisateur=request.user.utilisateur)
    return render(request, 'hello_cl.html', {'user_files': user_files})

def hello_autho(request):
    clients = Utilisateur.objects.filter(is_client=True)  # Get all clients
    
    client_files = {}  # Dictionary to store client files as {client: [files]}
    
    for client in clients:
        files_uploaded = UserFile.objects.filter(clients=client)
        client_files[client] = files_uploaded
    
    return render(request, 'hello_autho.html', {'client_files': client_files})


def import_file(request):
    context = {'form': UserFileForm()}
    if request.method == 'POST':
        form = UserFileForm(request.POST, request.FILES)
        if form.is_valid():
            user_file = form.save(commit=False)
            user_file.save()
            user_file.clients.add(request.user.utilisateur)
            messages.success(request, "File uploaded successfully")
            return redirect('hello_cl')
        else:
            context['form'] = form
    return render(request, 'import_file.html', context)

def authoritaire(request):
   
    return render(request, 'hello_autho.html')

def list_files(request):
    user_files = UserFile.objects.all()
    context = { 'user_files': user_files }
    return render(request, 'list_files.html', context)