from datetime import datetime, timezone


class ZonedDateTime:

    @classmethod
    def utc_now(cls):
        return datetime.now(timezone.utc)