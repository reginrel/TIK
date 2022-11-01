from django.shortcuts import render
from . models import Matkul

# Create your views here.
def matkul(request):
    matkul = Matkul.objects.all()

    konteks={
        'dataMatkul': matkul,
    }
    return render(request, 'matkul.html', konteks)