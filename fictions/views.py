from django.shortcuts import render, get_object_or_404
from .models import Fiction

def fiction_list(request):
    fictions = Fiction.objects.all()
    return render(request, 'fictions/fiction_list.html', {'fictions': fictions})

def fiction_detail(request, pk):
    fiction = get_object_or_404(Fiction, pk=pk)
    return render(request, 'fictions/fiction_detail.html', {'fiction': fiction})