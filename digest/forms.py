# -*- coding: utf-8 -*-
from django import forms

from digest.models import Rubric


class SendDigestForm(forms.Form):
    begin = forms.DateTimeField()
    final = forms.DateTimeField()
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(), empty_label=None, label=u'Рубрика')
    email = forms.EmailField(label=u'E-mail')

    def clean(self):
        cleaned_data = super(SendDigestForm, self).clean()
        begin = cleaned_data.get('begin')
        final = cleaned_data.get('final')

        if begin > final:
            self.add_error('begin', u'Начальное значение интервала больше конечного.')
