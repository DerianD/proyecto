from django.shortcuts import render 
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import libromodelo
from .forms import libroAddForms, LibroModelForm

# Create your views here.

def home(request):
    mensaje="Bienvenido a la Bibioteca :D"
    send={"me":mensaje}
    return render(request, 'home.html',send) 


# Vistas por clase

class LibroDetailView(DetailView):
    model = libromodelo

class LibroListView(ListView):
    model = libromodelo

    def get_queryset(self, *args, **kwargs):
        qs = super(LibroListView, self).get_queryset(**kwargs)
        return qs


def lista_libros2(request):
    #Logico de negocio alias hechizo
    librosclass = libromodelo.objects.all()
    print request
    m = "libro nuevo"
    template = "lista_libros.html"
    contexto= {"mensaje":m,
               "libros": librosclass }
    return render(request, template, contexto)

def detalle_libro(request, object_id=None):
    #Logico de negocio alias hechizo
    librosclass2 = get_object_or_404(libromodelo, id=object_id)
    m = "libro nuevo"
    template = "detalle.html"
    contexto= {"mensaje":m,
               "libros": librosclass2 }
    return render(request, template, contexto)

def detalle_s(request, slug=None):
    try:
        libroclass = get_object_or_404(libromodelo, slug=slug)
    except libromodelo.MultipleObjectsReturned:
        libroclass = libromodelo.objects.filter(slug=slug).order_by("-nombre").first()
    m = ""
    template = "detalle.html"
    contexto= {"mensaje":m,
           "libros": libroclass }
    return render(request, template, contexto)

def detalle_slug(request, slug=None):
    try:
        libroclass = get_object_or_404(libromodelo, slug=slug)
    except libromodelo.MultipleObjectsReturned:
        libroclass = libromodelo.objects.filter(slug=slug).order_by("-nombre").first()
    m = ""
    template = "detalle.html"
    contexto= {"mensaje":m,
           "libros": libroclass }
    return render(request, template, contexto)

def agregar_libro(request, object_id=None):
    form = libroAddForms(request.POST or None)
    if form.is_valid():
        form.save()
        print "Alta exitosa!"
    """
    if request.method == "POST":
        print request.POST
    if form.is_valid():
        # print request.POST
        data = form.cleaned_data
        nombre = data.get("nombre")
        autor = data.get("autor")
        editorial = data.get("editorial")
        ISBN = data.get("ISBN")
        precio = data.get("precio")
        # nuevo_producto = Producto.object.create(nombre = nombre,
        #                                         descripcion = descripcion,
        #                                         precio = precio)
        nuevo_libro = libromodelo()
        nuevo_libro.nombre = nombre
        nuevo_libro.autor = autor
        nuevo_libro.editorial = editorial
        nuevo_libro.ISBN = ISBN
        nuevo_libro.precio = precio
        nuevo_libro.save()
    """
    template = "agregar_libro.html"
    context = {
        "form":form
    }

    return render(request, template, context)


def actualizar(request, object_id=None):
    #Logico de negocio alias hechizo
    libros = get_object_or_404(libromodelo, id=object_id)
    form = LibroModelForm(request.POST or None, instance=libros)
    if form.is_valid():
        form.save()
        print "Actualizacion exitosa!"
    template = "actualizar.html"
    contexto= {
           "libros": libros,
           "form":form,
           "titulo":"Actualizar Libro"
           }
    return render(request, template, contexto)

