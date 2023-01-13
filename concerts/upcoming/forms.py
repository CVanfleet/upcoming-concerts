from django import forms

class ArtistForm(forms.Form):
    artist = forms.CharField(label='Enter your favorite artist', max_length=100)