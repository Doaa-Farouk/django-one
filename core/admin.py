from django.contrib import admin
from core.models import Event, Speaker, Sponsor, Venue, Accounts
# Register your models here.

admin.site.register(Event)
admin.site.register(Speaker)
admin.site.register(Sponsor)
admin.site.register(Venue)
admin.site.register(Accounts)