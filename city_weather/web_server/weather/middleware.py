from django.core.cache import cache


class CacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        CACHE_LIFETIME = 1800

        if data := cache.get(request.get_full_path()):
            return data

        data = self.get_response(request)
        cache.set(request.get_full_path(), data, timeout=CACHE_LIFETIME)
        return data


