from django.forms import ModelForm
from .models import Extra


class ExtraForm(ModelForm):
    class Meta:
        model = Extra
        fields = ["name"]
