from systemdesign.vending_machine.interface import IInventory, IState
from systemdesign.vending_machine.models import Inventory
from systemdesign.vending_machine.state import IdleState

class VendingMachine:
    def __init__(self):
        self._inventory = Inventory()
        self._current_state: IState = IdleState(self)

    def set_state(self, state: IState):
        self._current_state = state

    def handle(self):
        self._current_state.handle()

    def get_inventory(self) -> IInventory:
        return self._inventory
