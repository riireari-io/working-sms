from django.shortcuts import render

def sms_sender_view(request):
    return render(request, 'sms_send/sms_sender.html')
