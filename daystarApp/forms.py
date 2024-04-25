from django.forms import ModelForm
from .models import *


class AddBabyForm(ModelForm):
    class Meta:
        model = Baby
        fields = '__all__'

class AddPaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'