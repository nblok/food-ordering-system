from dataclasses import dataclass


@dataclass(frozen=True)
class KafkaProducerConfigData:
    key_serializer_class: str
    value_serializer_class: str
    compression_type: str
    acks: str
    batch_size: int
    batch_size_boost_factor: int
    linger_ms: int
    request_timeout_ms: int
    retry_count: int
