from uuid import UUID

from api.models import Service


class ServiceRepository:
    @staticmethod
    def get_by_id(service_id: UUID) -> Service | None:
        return Service.objects.filter(id=service_id).first()

    @staticmethod
    def get_by_name(service_name: str) -> Service | None:
        return Service.objects.filter(name=service_name).first()

    @staticmethod
    def create(data: dict) -> Service:
        return Service.objects.create(**data)


service_repository = ServiceRepository()