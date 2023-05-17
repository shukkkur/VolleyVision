class RangedFileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 200 and 'Content-Range' not in response and 'Accept-Ranges' not in response:
            response['Accept-Ranges'] = 'bytes'
        return response
