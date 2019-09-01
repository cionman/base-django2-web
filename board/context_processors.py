from django.utils import timezone


def board(request):
    return {
        'current_datetime': timezone.now(),
    }
