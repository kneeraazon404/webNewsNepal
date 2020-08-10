from django.contrib import admin

from .models import (
    Post,
    National,
    International,
    Covid,
    Sports,
    Entertainment,
    Politics,
    LifeStyle,
    Blog,
    Literature,
    Tech,
    Health,
    Business,
    Education,
    Contact,
    Subscription,
)

admin.site.register(Post)
admin.site.register(National)
admin.site.register(International)
admin.site.register(Covid)
admin.site.register(Sports)
admin.site.register(Politics)
admin.site.register(Entertainment)
admin.site.register(LifeStyle)
admin.site.register(Literature)
admin.site.register(Blog)
admin.site.register(Tech)
admin.site.register(Health)
admin.site.register(Business)
admin.site.register(Education)
admin.site.register(Contact)
admin.site.register(Subscription)

# admin.site.register(Comment)

