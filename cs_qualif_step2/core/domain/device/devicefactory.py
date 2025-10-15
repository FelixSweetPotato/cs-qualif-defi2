import hashlib
import re

from cs_qualif_step2.core.domain.device.device import Device
from cs_qualif_step2.core.domain.device.device_id import DeviceId
from cs_qualif_step2.core.domain.device.exception.invalid_mac_adress import InvalidMacAddress
from cs_qualif_step2.core.domain.device.exception.invalid_firmware import InvalidFirmware

from cs_qualif_step2.core.application.dto.device_config import DeviceConfig


class DeviceFactory:
    def create_device(self, device_config: DeviceConfig) -> Device:
        if not re.match(r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$', device_config.macAddress):
            raise InvalidMacAddress("Invalid MAC address format")
        # Regex de fou (oui il est valide)
        if not re.match(r'^[0-9].[0-9].[0-9]$', device_config.firmwareVersion):
            raise InvalidFirmware("Invalid Firmware Version")

        return Device(
            device_id=device_config.device_id,
            macAddress=device_config.macAddress,
            model=device_config.model,
            firmwareVersion=device_config.firmwareVersion,
            serialNumber=device_config.serialNumber,
            displayName=device_config.displayName,
            location=device_config.location,
            timezone=device_config.timezone
        )
