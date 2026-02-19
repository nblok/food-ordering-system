import typing as t

from common.common_domain.event.domain_event import DomainEvent


T = t.TypeVar("T", bound=DomainEvent, contravariant=True)


class DomainEventPublisher(t.Protocol[T]):

    def publish(self, domain_event: T) -> None:
        ...
