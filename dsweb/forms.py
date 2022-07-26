from django import forms
from dsweb.models import Inquiry


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'subject', 'content']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class':'form-control'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control'}),
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows':10}),
        # }
        labels = {
            'name': '이름',
            'email': '이메일',
            'subject': '제목',
            'content': '내용',
        }
