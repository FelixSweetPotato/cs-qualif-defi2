from cs_qualif_step2.core.domain.device.device_id import DeviceId

class Television:
    def __init__(self,
        device_id: DeviceId,
        channels: [],
        applications: [],
        networkSettings: [],
        displaySettings: [],
    ) -> None:
        self.__device_id = device_id,
        self.__channels = channels,
        self.__applications = applications,
        self.__networkSettings = networkSettings,

    def get_device_id(self) -> DeviceId:
        return self.__device_id

