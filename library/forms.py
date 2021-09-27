from django import forms

#klasik 4 işlem
class FourOperationsForm(forms.Form):
    first_field = forms.CharField(required=True, label="First field")
    select = forms.CharField(required=True, label="Select sign +,-,*,/")
    second_field = forms.CharField(required=True, label="Second field")

    def __init__(self, *args, **kwargs):
        super(FourOperationsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {"class": "form-control"}

#trigonometrik işlemler
class TrigonometryForm(forms.Form):
    value = forms.CharField(required=True, label="value")

#2.dereceden denklem çözümü
class QuadraticEquationsForm(forms.Form):
    a = forms.FloatField(widget=forms.TextInput(attrs={'step':'0.01', 'placeholder': 'a'}))
    b = forms.FloatField(widget=forms.TextInput(attrs={'step':'0.01', 'placeholder': 'b'}))
    c = forms.FloatField(widget=forms.TextInput(attrs={'step':'0.01', 'placeholder': 'c'}))


class FactorialForm(forms.Form):
    value = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'for n! Enter the n'}))


class SquareRootForm(forms.Form):
    valuesquare = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter the x'}))

class ExponentsForm(forms.Form):
    expo1 = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter the x'}))
    expo2 = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter the y'}))

class LogarithmForm(forms.Form):
    loga = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter the a'}))
    logb = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter the b'}))

class EbobForm(forms.Form):
    eboba = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter the a'}))
    ebobb = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter the a'}))

class DegreeRadianForm(forms.Form):
    SELECT = (('seçiniz','seçiniz'), ('degree','degree'), ('radian','radian'))
    selectdegreeradian = forms.ChoiceField(choices=SELECT, required=True)
    degreeorradian = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': 'value'}))

class CircleForm(forms.Form):
    r = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter the r', 'class':'form-control'}))

class RectangleForm(forms.Form):
    recta = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter the a', 'class':'form-control'}))
    rectb = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter the b', 'class':'form-control'}))

class CubeForm(forms.Form):
    cubea = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter the a', 'class':'form-control'}))

class CylinderForm(forms.Form):
    cylinderr = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter the r', 'class':'form-control'}))
    cylinderh = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter the h', 'class':'form-control'}))

class SphereForm(forms.Form):
    spherer = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter the r', 'class':'form-control'}))