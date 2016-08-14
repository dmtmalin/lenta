# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView

from digest.forms import SendDigestForm
from django.contrib.messages.views import SuccessMessageMixin


class SendDigestView(SuccessMessageMixin, FormView):
    form_class = SendDigestForm
    template_name = 'digest/send.html'
    success_url = reverse_lazy('send-digest-view')
    success_message = u'Дайджест новостей успешно отправлен'

    def form_valid(self, form):

        return super(SendDigestView, self).form_valid(form)
