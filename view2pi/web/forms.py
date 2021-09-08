from django.forms import ModelForm
from web.models import Guest

class GuestForm(ModelForm):
 

    class Meta:
        model = Guest
        fields = ('name', 'email',  'phone')
   