from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "category", "description", "thumbnail", "is_featured", "stock", "brand", "rating"]