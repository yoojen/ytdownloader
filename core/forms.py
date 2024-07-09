from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class SearchForm(forms.Form):
    query=forms.CharField(max_length=256)
    upload_at=forms.DateField(widget=DateInput(),required=False)