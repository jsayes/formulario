from django.shortcuts import render
from formulario.models import clientes

# Create your views here.
def index(request):
    return render(request, 'index.html')

def reserva(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        celular = request.POST['celular']
        email = request.POST['email']

        nombre1 = request.POST['nombre']
        celular2 = request.POST['celular']
        email2 = request.POST['email']


        cliente = clientes(celular=celular2, nombre=nombre1, correo=email2)
        cliente.save()

    return render(request, 'guardar.html',{
        'nombre': nombre,
        'celular': celular,
        'email': email

    })
