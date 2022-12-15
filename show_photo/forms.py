from django.forms import ModelForm
from .models import *

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
class MessagesForm(ModelForm):
    class Meta:
        model = Messages
        fields = '__all__'
