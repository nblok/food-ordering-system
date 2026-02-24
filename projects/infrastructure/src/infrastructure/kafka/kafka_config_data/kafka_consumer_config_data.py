from dataclasses import dataclass

@dataclass(frozen=True)
class KafkaConsumerConfigData:
    key_deserializer: str
    value_deserializer: str
    auto_offset_reset: str
    specific_avro_reader: str
    specific_avro_reader_key: str
    batch_listener: bool
    auto_startup: bool
    concurrency_level: int
    session_timeout_ms: int
    heartbeat_interval_ms: int
    max_poll_interval_ms: int
    poll_timeout_ms: int
    max_poll_records: int
    max_partition_fetch_bytes_default: int
    max_partition_fetch_bytes_boost_factor: int