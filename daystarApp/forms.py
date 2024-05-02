from django.forms import ModelForm
from .models import *




class AddPaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

class AddBabyForm(ModelForm):
    class Meta:
        model = Baby
        fields = '__all__'

class AddSitterForm(ModelForm):
    class Meta:
        model = Sitter
        fields = '__all__'



class AddDollForm(ModelForm):
    class Meta:
        model = Doll
        fields = '__all__'