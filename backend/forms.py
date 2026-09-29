from django import forms

class QRCodeForm(forms.Form):
    restaurant_name=forms.CharField(max_length=100, label='QR Name',
                                    widget=forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Enter Restaurant name'
                                    }))
    url= forms.URLField(max_length=200, label='URL',
                        widget=forms.URLInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'Enter URL'
                        })) 