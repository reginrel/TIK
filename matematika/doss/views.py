from django.shortcuts import render
from . models import Dosen, Staf

# Create your views here.
def doss(request):
    dosen = Dosen.objects.all()
    staf = Staf.objects.all()

    konteks={
        'dataDosen' : dosen,
        'dataStaf': staf,
    }
    return render(request, 'doss.html', konteks)