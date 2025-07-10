from django.shortcuts import render
from .models import About
from .forms import CollaborateForm
from django.contrib import messages

# Create your views here.


def about_view(request):
    """
    Display the about page.
    **Context:**
    ``about``
        An instance of :model:`about.About`.
        **Template:**
        :template:`about/about.html`
    """
    about = About.objects.all().order_by("-updated_on").first()
    collaborate_form = CollaborateForm()

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_request = collaborate_form.save(commit=False)
            collaborate_request.read = False
            collaborate_request.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Collaboration request received! I endeavour to respond within 2 working days.",
            )

    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about, "collaborate_form": collaborate_form},
    )
