from django import forms

class libroAddForms(forms.Form):

    nombre = forms.CharField()
    autor = forms.CharField()
    editorial = forms.CharField()
    ISBN = forms.CharField()
    precio = forms.DecimalField(max_digits=9999, decimal_places=2)
    """
    def clean_precio(self):
        precio2 = self.cleaned_data.get("precio")
        if precio2 <= 100.00:
            raise forms.ValidationError("El precio debe ser mayor que $100.00")
        elif precio2 >= 19999.00:
            raise forms.ValidationError("El precio debe ser menos que $19999.00")
        else:
            raise precio2
    """

