from django import forms
from .models import apply_inform


class apply_form(forms.ModelForm):
    class Meta:
        model = apply_inform
        fields = ('고객명','고객주소','주민등록번호','연락처','신분증사진')

