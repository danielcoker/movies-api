from django.http import JsonResponse


def jsonResponse404(request, exception=None):
    return JsonResponse({
        'success': False,
        'message': 'API endpoint does not exist.',
    }, status=404)
