from django import forms


class Routes(forms.Form):
    file = forms.FileField()

    file.widget.attrs.update({'class': 'custom-file-input'})
