from random import choice
from django.conf import settings
from django.utils import timezone
from string import ascii_lowercase, digits
from datetime import datetime, timedelta

def update_url_details(obj):
    attrs = set_attrs(obj.lifespan)
    short_url = "".join([choice(ascii_lowercase + digits) for _ in range(int(attrs["chars"]))])
    
    attrs["short_url"] = short_url

    return attrs

def set_attrs(lifespan):
    chars = getattr(settings, "url_chars", 7)
    max_uses = getattr(settings, 'max_uses', 1)

    if lifespan != -1:
        expiry_date = timezone.now() + timedelta(seconds=lifespan)
    else:
        expiry_date = timezone.make_aware(timezone.datetime.max, timezone.get_default_timezone())
    
    date_created = datetime.now()

    return {"chars": chars, "max_uses": max_uses, "lifespan": lifespan, "expiry_date": expiry_date, "date_created": date_created}
    


