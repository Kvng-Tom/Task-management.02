from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from account.models import OTP 
import random
from django.utils import timezone
from datetime import timedelta
import requests



def generate_otp():
    otp = random.randint(100000, 999999)
    return otp

User = get_user_model()

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        instance.is_active = True
        instance.save()

        otp = generate_otp()
        print(otp)

        expiry_date = timezone.now() + timedelta(minutes=10)

        OTP.objects.create(
            otp=otp,
            user=instance,
            expiry_date=expiry_date
        )

        url = "https://api.useplunk.com/v1/track"
        header = {
            "Authorization": "Bearer sk_f1a0a516aca711fd52ba193b1bfd04751ca591abb96e9b5a",
            "Content-Type": "application/json"
        }

        data = {
            "email": instance.email,
            "event": "welcome",
            "data": {
                "full_name": instance.full_name,
                "otp": str(otp)
            }
        }

        response = requests.post(
            url=url,
            headers=header,
            json=data
        )

        print(response.json())



