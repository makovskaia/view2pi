from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from web.forms import GuestForm
def index(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            guest = form.save(commit=False)
            guest.ip = request.META.get("REMOTE_ADDR")
            guest.save()
            context = {
                'image': 'web/0.jpg',
                'markers': [(10,20)]
            }
            return render(request, 'web/index.html', context)
        else:
            return(request, 'web/form.html', {'form': form})
    else:
        form = GuestForm()
        template = loader.get_template('web/form.html')
        context = {
            form: form
        }
        return render(request, 'web/form.html', {'form': form})