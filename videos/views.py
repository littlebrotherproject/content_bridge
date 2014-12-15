from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from postmark_inbound import PostmarkInbound
from models import Email, Video
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import logging

logger = logging.getLogger(__name__)


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the videos index.")


@csrf_exempt
@require_http_methods(["GET", "POST"])
def email_handle_incoming(request):
    if request.method == 'GET':
        return HttpResponse("Webhook Endpoint")
    elif request.method == 'POST':
        print request.body
        logger.error(request.body)


        inbound = PostmarkInbound(json=request.body)
        print inbound
        print inbound.subject()
        print inbound.sender()['Email']
        print inbound.text_body()

        email = Email.objects.get_or_create(
            message_id=inbound.message_id(),
            subject=inbound.subject(),
            recieved=inbound.send_date(),
            from_address=inbound.sender()['Email'],
            text_body=inbound.text_body(),
            html_body=inbound.html_body(),
        )[0]

        print email

        email.populate_data()
        
        print "Youtube ID found in email: %s" % email.youtube_id

        video = Video.objects.get_or_create(
            youtube_id=email.youtube_id 
            )[0]
        
        video.populate_data()
        video.save()

        return HttpResponse(request.body)


