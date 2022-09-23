from django.shortcuts import render
from http.client import HTTPResponse

from miblogApp.models import *
from django.http import HttpResponse

# Create your views here.
#def curso(request):

#    materia = Curso(nombre="Hacking", camada=99999)

#    materia.save()

#    return HttpResponse(f"Estoy guardando el primer curso: {materia.nombre}")

        
def verindex(request):
    #conn = sqlite3.connect('db.sqlite3')
    #print ("Opened database successfully")
    #lista_familia = conn.execute("SELECT * FROM Appentregable1_familiar")
    #lista_blog= verindex.objects.all()
    #context = {'verindex': verindex}
    
    #return render(request, 'index.html', context=context)   
    return render(request, 'index.html')

def aboutme(request):
    #conn = sqlite3.connect('db.sqlite3')
    #print ("Opened database successfully")
    #lista_familia = conn.execute("SELECT * FROM Appentregable1_familiar")
   # lista_familia= verindex.objects.all()
   # context = {'lista_familia': lista_familia}
    
    #return render(request, 'index.html', context=context)   
    return render(request, 'aboutme.html')

def blog(request):
    #conn = sqlite3.connect('db.sqlite3')
    #print ("Opened database successfully")
    #lista_familia = conn.execute("SELECT * FROM Appentregable1_familiar")
   # lista_familia= verindex.objects.all()
   # context = {'lista_familia': lista_familia}
    lista_blog= Blog.objects.all()
    context = {'lista_blog': lista_blog}
    
    #return render(request, 'index.html', context=context)   
    return render(request, 'blog.html', context=context)    
    

def curriculum(request):
    #conn = sqlite3.connect('db.sqlite3')
    #print ("Opened database successfully")
    #lista_familia = conn.execute("SELECT * FROM Appentregable1_familiar")
   # lista_familia= verindex.objects.all()
   # context = {'lista_familia': lista_familia}
    
    #return render(request, 'index.html', context=context)   
    return render(request, 'curriculum.html')

def portfolio(request):
    #conn = sqlite3.connect('db.sqlite3')
    #print ("Opened database successfully")
    #lista_familia = conn.execute("SELECT * FROM Appentregable1_familiar")
   # lista_familia= verindex.objects.all()
   # context = {'lista_familia': lista_familia}
    
    #return render(request, 'index.html', context=context)   
    return render(request, 'portfolio.html')

def contacto(request):
    #conn = sqlite3.connect('db.sqlite3')
    #print ("Opened database successfully")
    #lista_familia = conn.execute("SELECT * FROM Appentregable1_familiar")
   # lista_familia= verindex.objects.all()
   # context = {'lista_familia': lista_familia}
    
    #return render(request, 'index.html', context=context)   
    return render(request, 'contacto.html')

def blogentrada(request):
    #conn = sqlite3.connect('db.sqlite3')
    #print ("Opened database successfully")
    #lista_familia = conn.execute("SELECT * FROM Appentregable1_familiar")
   # lista_familia= verindex.objects.all()
   # context = {'lista_familia': lista_familia}
    
    #return render(request, 'index.html', context=context)   
    return render(request, 'formblogentrada.html')


# Create your views here.
