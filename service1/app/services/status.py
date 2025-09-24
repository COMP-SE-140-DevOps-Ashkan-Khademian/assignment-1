import datetime
import shutil
from typing import ClassVar


class StatusService:
    STATUS_TEMPLATE: ClassVar[str] = (
        "{iso_now}: uptime {uptime:.3f} hours, free disk in root: {free_disk:.2f} MBytes"
    )

    def _get_iso_now(self) -> str:
        return (
            datetime.datetime.now(datetime.timezone.utc)
            .isoformat(timespec="seconds")
            .replace("+00:00", "Z")
        )

    def _get_uptime(self) -> float:
        with open("/proc/uptime", "r") as f:
            uptime_seconds = float(f.read().split()[0])
        return uptime_seconds / 3600

    def _get_free_disk(self) -> float:
        _, _, free_bytes = shutil.disk_usage("/")
        return free_bytes / (1024 * 1024)

    def _get_status_metadata(self) -> dict:
        return {
            "iso_now": self._get_iso_now(),
            "uptime": self._get_uptime(),
            "free_disk": self._get_free_disk(),
        }

    def get_status(self) -> str:
        metadata = self._get_status_metadata()
        return self.STATUS_TEMPLATE.format(**metadata)
