from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from django.views.generic.base import View
from . import models
from . import forms


class MessageListView(ListView):
    template_name = "messages/messages_list.html"
    model = models.Messages

    def get_queryset(self):
        this_user = self.request.user
        return models.Messages.objects.get_my_messages(this_user, this_user)



class SendMessageView(View):
    form_class = forms.SendMessageForm
    template_name = "messages/send_message.html"
    context = {}

    def get(self, request, *args, **kwargs):
        send_message_form = self.form_class(request.POST or None)
        self.context["send_message_form"] = send_message_form
        return render(self.request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        send_message_form = self.form_class(request.POST or None)
        if send_message_form.is_valid():
            title = send_message_form.cleaned_data.get('title')
            text = send_message_form.cleaned_data.get('text')
            subject = send_message_form.cleaned_data.get('subject')
            to_username = send_message_form.cleaned_data.get('to_user')
            from_user = self.request.user

            is_user_exists = User.objects.filter(username=to_username).exists()
            if is_user_exists is not None:
                to_user = get_object_or_404(User, username=to_username)

                if to_user is not None:

                    models.Messages.objects.create(
                        title=title,
                        text=text,
                        subject=subject,
                        to_user=to_user,
                        from_user=from_user
                    )
                    return redirect('/messages')

                else:
                    send_message_form.add_error(
                        'to_user', 'to user is not exists')
                    return redirect('/send-message')

        self.context["send_message_form"] = send_message_form
        return render(self.request, self.template_name, self.context)
