import asyncio
from buyer_state_machine import BuyerStateMachine
from models import Buyer
from repository.sqlalchemy_repository import SQLAlchemyRepository
from database import SessionLocal

async def main():
    # Создание покупателя
    with SessionLocal() as session:
        buyer_repo = SQLAlchemyRepository(session, Buyer)
        buyer = Buyer(name="John Doe", budget=20000)
        buyer_repo.add(buyer)

        # Создание и запуск конечного автомата
        state_machine = BuyerStateMachine(buyer)
        await state_machine.process()

        print(f"Final state: {state_machine.get_state()}")

if __name__ == "__main__":
    asyncio.run(main())
