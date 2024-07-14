from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class SearchForm(forms.Form):
    query=forms.CharField(max_length=256)
    upload_at=forms.DateField(widget=DateInput(),required=False)

class DownloadForm(forms.Form):
    yt_link = forms.CharField(max_length=256, help_text="Paste link from youtube")

    def clean_yt_link(self):
        yt_link = self.cleaned_data["yt_link"]
        if not yt_link.startswith("https://www.youtube.com/"):
            raise ValueError("Provide valid youtbe link")
        
        return yt_link
