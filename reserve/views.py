from django.shortcuts import render, redirect

from .forms import ReserveForm

def index(request):
    if request.method == "POST":
        print('Ölçek', request.POST)
        form = ReserveForm(request.POST)
        print('----')
        print(form.is_valid())
        if form.is_valid():
            print('Geçit')
            form.save()
            return redirect('reserve:confirm')
    else:
        form = ReserveForm()
    return render(request, 'reserve/index.html', {'form':form})

def confirm(request):
    return render(request, 'reserve/confirm.html')

def complete(request):
    return render(request, 'reserve/complete.html')

# Create your views here.
