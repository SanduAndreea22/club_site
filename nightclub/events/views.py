from django.shortcuts import render
from django.views import View
from .models import Eveniment


# Exemplu de vizualizare bazată pe funcții

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def events_view(request):
    # Logic pentru a obține lista de evenimente din baza de date
    evenimente = Eveniment.objects.all()
    return render(request, 'events.html', {'evenimente': evenimente})

def gallery_view(request):
    # Logic pentru a obține imaginile din galerie
    # Poți utiliza modele sau simplu să trimiti o listă de imagini
    imagini = [
        'image1.jpg',
        'image2.jpg',
        'image3.jpg',
    ]
    return render(request, 'gallery.html', {'imagini': imagini})

def menu_view(request):
    # Logic pentru a obține meniul de băuturi și gustări
    meniu = {
        'bauturi': ['Cafea', 'Ceai', 'Suc', 'Apa'],
        'gustari': ['Sandwich', 'Salata', 'Pizza', 'Nachos'],
    }
    return render(request, 'menu.html', {'meniu': meniu})

def contact_view(request):
    # Logic pentru formularul de contact
    if request.method == 'POST':
        # Procesează datele trimise prin formular
        # Aici poți adăuga logica pentru a salva datele în baza de date sau a trimite un email
        return render(request, 'contact_success.html')
    return render(request, 'contact.html')

def reservations_view(request):
    # Logic pentru formularul de rezervări
    if request.method == 'POST':
        # Procesează datele trimise prin formular
        # Aici poți adăuga logica pentru a salva rezervarea în baza de date și a trimite o confirmare utilizatorului
        return render(request, 'reservations_success.html')
    return render(request, 'reservations.html')

# Exemplu de vizualizare bazată pe clase

class LoginView(View):
    def get(self, request):
        # Logica pentru afișarea formularului de login
        return render(request, 'login.html')

    def post(self, request):
        # Logica pentru procesarea datelor trimise prin formularul de login
        # Aici poți valida datele de login și a trimite utilizatorul către o pagină de succes sau de eroare
        return render(request, 'login_success.html')

class RegisterView(View):
    def get(self, request):
        # Logica pentru afișarea formularului de înregistrare
        return render(request, 'register.html')

    def post(self, request):
        # Logica pentru procesarea datelor trimise prin formularul de înregistrare
        # Aici poți crea un nou utilizator în sistem și a trimite utilizatorul către o pagină de succes sau de eroare
        return render(request, 'register_success.html')

