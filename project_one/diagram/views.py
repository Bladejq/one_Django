from django.shortcuts import render, redirect
from .models import QalaData
from .forms import QalaDataFrom

def index(request):
    data = QalaData.objects.all()
    if request.method == 'POST':
        form = QalaDataFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = QalaDataFrom()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'diagram/index.html', context)
