# -*- coding: utf-8 -*-
from django.core.serializers import serialize
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView

from digest.forms import SendDigestForm
from django.contrib.messages.views import SuccessMessageMixin

from digest.models import News
from digest.tasks import send


class SendDigestView(SuccessMessageMixin, FormView):
    form_class = SendDigestForm
    template_name = 'digest/send.html'
    success_url = reverse_lazy('send-digest-view')
    success_message = u'Дайджест новостей успешно отправлен'

    def form_valid(self, form):
        data = form.cleaned_data
        news = News.objects.filter(rubric=data.get('rubric'), published__gte=data.get('begin'),
                                   published__lte=data.get('final'))
        serialize_news = serialize('json', news)
        email = data.get('email')
        send.apply_async((serialize_news, email), queue='high')
        return super(SendDigestView, self).form_valid(form)
