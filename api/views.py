from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.service import service_service
from api.serializers import CreateServiceSerializer

class ServiceView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._service = service_service

    def post(self, request):
        serializer_data = CreateServiceSerializer(data=request.data)
        serializer_data.is_valid(raise_exception=True)

        new_service = self._service.create(serializer_data.data)
        response_data = CreateServiceSerializer(new_service).data

        return Response(
            data=response_data,
            status=status.HTTP_201_CREATED
        )
