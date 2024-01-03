from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from orm.models import SentEmail, Contact


class EventTrackerApiView(APIView):
    authentication_classes = []
    permission_classes = []

    def __init__(self):
        super().__init__()

    def _process(self):
        # get data
        request_data = self.request.data
        email_type = request_data.get('type')
        email_id = request_data.get('data').get('email_id')

        # get sent email object & update status
        sent_email = SentEmail.objects.get_via_resend_id(email_id)
        if sent_email:
            Contact.objects.unsubscribe(sent_email.contact.lead_id)
            SentEmail.objects.update_status(sent_email, email_type)

        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        return self._process()


def unsubscribe_view(request, unsubscribe_token):
    Contact.objects.unsubscribe(unsubscribe_token)
    return render(request, 'event/template.html')
