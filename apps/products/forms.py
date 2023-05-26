from django.forms import ModelForm
from .models import Cart
from shopping.models import Review

class CartForm(ModelForm):
    class Meta:
        model=Cart
        fields='__all__'
        
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'