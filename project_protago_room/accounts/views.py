from django.views.generic.base import TemplateView

class LoginView(TemplateView):
    template_name = "registration/login.html"

# Create your views here.
class SignupView(TemplateView):
    template_name = "registration/singup.html"


class SignupDoneView(TemplateView):
    template_name = "registration/signup_done.html"