from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from pos_back_end.api.address.address_models import StateItem, StateResponseBody
from pos_back_end.api.address.address_services import AddressServices
from pos_back_end.db.dependencies import get_db

router = APIRouter()


@router.get("/states")
def get_states(db: Session = Depends(get_db)):

    states = AddressServices().get_states(db)
    state_items = [StateItem.from_orm(state) for state in states]

    return StateResponseBody(states=state_items)

