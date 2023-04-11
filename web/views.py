from models import Review
list = Review.objects.all()



from django.shortcuts import render
from views import M_form

def main(request):
    form = M_form()

    if request.method == 'POST':
        form = M_form('POST')
        return request('POST')
    if form.is_valid:
        form.safe()



    return render(request, 'main.html', {'form': form}, {'list': list})



