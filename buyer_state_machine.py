import asyncio
from enum import Enum
from typing import Any

class BuyerState(Enum):
    NEW = "new"
    PROCESSED = "processed"
    PAID = "paid"

class BuyerStateMachine:
    def __init__(self, buyer):
        self.buyer = buyer
        self.state = BuyerState.NEW

    async def process(self):
        await self._transition_to_processed()
        await self._transition_to_paid()

    async def _transition_to_processed(self):
        print(f"Buyer {self.buyer.id} moving to PROCESSED state")
        await asyncio.sleep(1)  # Simulating some async task
        self.state = BuyerState.PROCESSED

    async def _transition_to_paid(self):
        print(f"Buyer {self.buyer.id} moving to PAID state")
        await asyncio.sleep(1)  # Simulating some async task
        self.state = BuyerState.PAID

    def get_state(self) -> BuyerState:
        return self.state
