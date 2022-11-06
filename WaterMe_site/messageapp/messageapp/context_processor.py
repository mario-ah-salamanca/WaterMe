from .models import TwilioAccount


def settings(request):
    return {'settings': TwilioAccount.load()}