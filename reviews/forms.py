from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout, Fieldset, ButtonHolder, Submit, Field)
from .models import Review, Product


class ReviewForm(forms.ModelForm):
    """Review form """

    class Meta:
        model = Review
        fields = ['title', 'body', 'rating']
