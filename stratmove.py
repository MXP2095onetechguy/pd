from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional

class Move(Enum):
    COOPERATE = 'cooperate'
    BETRAY = 'betray'

class Strategy(ABC):
    @abstractmethod
    def decide_move(self) -> Move:
        pass

    @abstractmethod
    def feed(self, last_move: Optional[Move], total_rounds: Optional[int], current_round: Optional[int]) -> None:
        pass
