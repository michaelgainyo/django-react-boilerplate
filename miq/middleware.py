from django.conf import settings


class CORSMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        try:
            response["Access-Control-Allow-Origin"] = settings.CORS_ORIGIN
            response["Access-Control-Allow-Headers"] = "X-CSRFTOKEN, x-requested-with, Content-Type, Accept, Origin"
            response["Access-Control-Allow-Methods"] = "OPTIONS, GET, POST, PUT, DELETE, PATCH"
            response["Access-Control-Max-Age"] = 86400
            response["Access-Control-Allow-Credentials"] = 'true'
        except Exception:
            pass

        return response
