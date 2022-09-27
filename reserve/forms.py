from django import forms

from .models import Reserve

class ReserveForm(forms.ModelForm):
  

    class Meta:
        
        model = Reserve
        fields = ('reserve_date', 'reserve_num', 'reserve_time', 'name', 'email', 'tel', 'comment')
        widgets = {
                'reserve_date': forms.Select(attrs={
                    'class': 'form-select',
                    'name': 'reserve_date',
                    'placeholder': 'Rezervasyon Tarihi',
                }),
                'reserve_num': forms.Select(attrs={
                    'class': 'form-select',
                    'name': 'reserve_num',
                    'placeholder': 'Kişi Sayısı',
                }),
                'reserve_time': forms.Select(attrs={
                    'class': 'form-select',
                    'name': 'reserve_time',
                    'placeholder': 'Zaman',
                }),
                'name': forms.TextInput(attrs={
                    'class': 'form-control',
                    'name': 'name',
                    'placeholder': 'Ad Soyad',
                }),
                'email': forms.EmailInput(attrs={
                    'class': 'form-control',
                    'name': 'email',
                    'placeholder': 'Eposta Adresi',
                }),
                'tel': forms.TextInput(attrs={
                    'type': 'tel',
                    'class': 'form-control',
                    'name': 'tel',
                    'placeholder': 'Telefon Numarası',
                    }),
                'comment': forms.Textarea(attrs={
                    'class': 'form-control',
                    'name': 'reserve_time',
                    'placeholder': 'Açıklama Sütunu',
                }),
        }
