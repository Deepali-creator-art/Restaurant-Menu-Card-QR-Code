from django import forms 
#class definition for form creation
class QRcodeform(forms.Form):
    restaurant_name=forms.CharField(max_length=50)
    menucardlink=forms.URLField(max_length=50)