from django.http import HttpResponse
from plyer import notification

# Create your views here.

# view for push notification
def notification_push(request): 
    notification.notify(
            title = "Push notification",
            message="Meassage Successfully recived... ",
    )
    return HttpResponse("Notification Meassage Successfully send... ")
