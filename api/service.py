from rest_framework.exceptions import ValidationError

from api.models import Service
from api.repository import ServiceRepository, service_repository


class ServiceService:
    def __init__(self, repo: ServiceRepository) -> None:
        self._repo = repo

    def register(self, register_data: dict) -> Service:
        name = register_data.get("name")

        existing_service = self._repo.get_by_name(name)

        if existing_service is not None:
            raise ValidationError({
                "name": f"Service with name '{name}' already exists."
            })

        return self._repo.create(**register_data)


service_service = ServiceService(service_repository)