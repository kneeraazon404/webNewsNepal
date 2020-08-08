from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == "POST":
        post_id = request.POST["post_id"]
        post = request.POST["post"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        user_id = request.POST["user_id"]
        user_email = request.POST["user_email"]

        #  Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                post_id=post_id, user_id=user_id
            )
            if has_contacted:
                messages.error(
                    request, "You have already made an inquiry for this post"
                )
                return redirect("/posts/" + post_id)

        contact = Contact(
            post=post,
            post_id=post_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
        )

        contact.save()

        # Send email
        # send_mail(
        #   'Property post Inquiry',
        #   'There has been an inquiry for ' + post + '. Sign into the admin panel for more info',
        #   'traversy.brad@gmail.com',
        #   [realtor_email, 'techguyinfo@gmail.com'],
        #   fail_silently=False
        # )

        messages.success(
            request,
            "Your request has been submitted, a realtor will get back to you soon",
        )
        return redirect("/posts/" + post_id)

