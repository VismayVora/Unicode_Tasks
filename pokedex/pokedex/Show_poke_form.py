from django import forms
 
 class ShowPokeForm(forms.Form):
     type = forms.CharField(max_length=100, label='Pokemon Type')
     id = forms.i=IntegerField(required=False, label='Pokemon ID')