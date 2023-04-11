from django.shortcuts import render, redirect
from web.forms import MForm
from web.models import Category, Review

def main(request):
    list = Review.objects.all()
    form = MForm()
    if request.method == 'POST':
        form = MForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('main')
    return render(request, 'main.html', {
        'form': form,
        'list': list
    })




