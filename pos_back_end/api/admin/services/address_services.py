from sqlalchemy.orm import Session
from pos_back_end.api.admin.models.admin_request_models import AddressRequestAndResponse
from pos_back_end.db.models.address import Address
from pos_back_end.db.models.state import State


class AddressServices:

    @staticmethod
    def get_states(db: Session):
        return db.query(State).all()

    @staticmethod
    def create_address(request: AddressRequestAndResponse):
        new_address = Address(
            street_address=request.street_address,
            city=request.city,
            state=request.state,
            zipcode=request.zipcode,
        )

        return new_address

