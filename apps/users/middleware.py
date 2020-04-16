from django.core.cache import cache
from django.utils import timezone
from users.models import Profile


def last_visit_middleware(get_response):

    def middleware(request):
        """
        Save the time of last user visit
        """
        response = get_response(request)

        if request.user.is_authenticated:
            Profile.objects.filter(user=request.user) \
                .update(last_visit=timezone.now())

        return response

    return middleware
