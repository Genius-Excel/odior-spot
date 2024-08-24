from django import forms
from .models import OrderRequest


class OrderRequestForm(forms.ModelForm):
    class Meta:
        model = OrderRequest
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(OrderRequestForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})