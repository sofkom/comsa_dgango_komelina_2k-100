from web.models import Review, Category
    from django import forms

    class MForm(forms.ModelForm):
        class Meta:
            model = Category
            fields = ['name', 'category', 'text']


    return render(request, 'main.html', {'form': form}, {'list': list})

