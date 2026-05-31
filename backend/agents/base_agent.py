from __future__ import annotations

from abc import ABC, abstractmethod

from core.models import OmegaSequence


class BaseAgent(ABC):
    @abstractmethod
    def analyze(self, content: str, domain: str = "generic") -> OmegaSequence:
        raise NotImplementedError

    @abstractmethod
    def is_available(self) -> bool:
        raise NotImplementedError
