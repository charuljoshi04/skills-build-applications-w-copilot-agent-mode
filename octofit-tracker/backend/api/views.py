import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev"
    else:
        scheme = request.scheme
        host = request.get_host()
        base_url = f"{scheme}://{host}"
    return Response({
        'users': base_url + reverse('user-list', request=request, format=format),
        'teams': base_url + reverse('team-list', request=request, format=format),
        'activities': base_url + reverse('activity-list', request=request, format=format),
        'workouts': base_url + reverse('workout-list', request=request, format=format),
        'leaderboard': base_url + reverse('leaderboard-list', request=request, format=format),
    })
