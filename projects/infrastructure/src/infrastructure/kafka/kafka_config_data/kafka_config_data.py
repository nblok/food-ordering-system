from dataclasses import dataclass


@dataclass(frozen=True)
class KafkaConfigData:
    bootstrap_servers: str
    schema_registry_url_key: str
    schema_registry_url: str
    num_partitions: int = 3
    replication_factor: int = 3