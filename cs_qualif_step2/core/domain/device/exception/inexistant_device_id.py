from cs_qualif_step2.core.domain.exception.ConflictException import ConflictException


class InexistantDeviceId(ConflictException):
    def __init__(self, device_id: str):
        self.device_id = device_id
        super().__init__(f"Device id {device_id} not found.")
