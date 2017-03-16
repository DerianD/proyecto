from django import forms

from .models import libromodelo

OPCIONES_TIPO = (
    ('libro', "Libro"),
    ('foto', "Foto"),
    ('video juego', "Video Juego"),
)

class libroAddForms(forms.Form):

    nombre = forms.CharField()
    autor = forms.CharField()
    editorial = forms.CharField()
    ISBN = forms.CharField()
    precio = forms.DecimalField(max_digits=9999, decimal_places=2)
    tipo = forms.ChoiceField(choices=OPCIONES_TIPO)
    
    def clean_precio(self):
        precio2 = self.cleaned_data.get("precio")
        if precio2 <= 100.00:
            raise forms.ValidationError("El precio debe ser mayor que $100.00")
        elif precio2 >= 19999.00:
            raise forms.ValidationError("El precio debe ser menos que $19999.00")
        else:
            print "Nuevo libro creado"
            return precio2
    



class LibroModelForm(forms.ModelForm):
    tipo=forms.ChoiceField(choices=OPCIONES_TIPO)
    class Meta:
        model=libromodelo
        fields=[
            "nombre",
            "autor",
            "editorial",
            "ISBN",
            "tipo"
        ]
        labels={
            "nombre":"Cual es el nombre",
            "autor":"Cual es el autor",
            "precio":"Cual es el precio"
        }
        widgets={
            "nombre":forms.TextInput(attrs={'class':'form-control','placeholder':'Ponga el nombre'}),
            "autor":forms.Textarea(attrs={'class':'form-control'}),
            "precio":forms.NumberInput(attrs={'class':'form-control'})
        }

    def clean_precio(self):
        precio2 = self.cleaned_data.get("precio")
        if precio2 <= 100.00:
            raise forms.ValidationError("El precio debe ser mayor que $100.00")
        elif precio2 >= 19999.00:
            raise forms.ValidationError("El precio debe ser menos que $19999.00")
        else:
            print "Nuevo libro creado"
            return precio2

