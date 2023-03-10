from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Pertanyaan

from django.template import loader
# Create your views here.

def index(request):
    pertanyaan_terakhir_list = Pertanyaan.objects.order_by('-pub_date')[:5]
    context = {
        'pertanyaan_terakhir_list': pertanyaan_terakhir_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, pertanyaan_id):
    pertanyaan = get_object_or_404(Pertanyaan, pk=pertanyaan_id)
    return render(request, 'polls/detail.html', {'pertanyaan': pertanyaan})

def hasil(request, pertanyaan_id):
    response = "kamu mencari hasil dari pertanyaan %s."
    return HttpResponse(response % pertanyaan_id)

def suara(request, pertanyaan_id):
    return HttpResponse("Kamu memilih suara dari pertanyaan %s." % pertanyaan_id)


