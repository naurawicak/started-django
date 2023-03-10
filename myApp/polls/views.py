from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Pilih, Pertanyaan
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'pertanyaan_terakhir_list'

    def get_queryset(self):
        return Pertanyaan.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Pertanyaan
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Pertanyaan.objects.filter(pub_date__lte=timezone.now())


class HasilView(generic.DetailView):
    model = Pertanyaan
    template_name='polls/hasil.html'

def suara(request, pertanyaan_id):
    pertanyaan = get_object_or_404(Pertanyaan, pk=pertanyaan_id)
    try:
        selected_pilih = pertanyaan.pilih_set.get(pk=request.POST['pilih'])
    except (KeyError, Pilih.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'pertanyaan': pertanyaan,
            'error_message': "Kamu tidak memilih pilihan",
        })
    else:
        selected_pilih.suara += 1
        selected_pilih.save()
        return HttpResponseRedirect(reverse('polls:hasil', args=(pertanyaan.id)))

    


