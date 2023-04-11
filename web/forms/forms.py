from web.models import Review, Category
from django import forms

class M_form():
    forms.formset_factory()


class Meta():
    model = Review
    field = ['name', 'category', 'text']

