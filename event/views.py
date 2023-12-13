from rest_framework.views import APIView
from rest_framework import status

from orm.models import SentEmail, EmailVariant


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
            SentEmail.objects.update_status(sent_email, email_type)

        return status.HTTP_200_OK

    def get(self, request):
        return self._process()
