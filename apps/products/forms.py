from django.forms import ModelForm
from .models import Cart

class CartForm(ModelForm):
    class Meta:
        model=Cart
        fields='__all__'