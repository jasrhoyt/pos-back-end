from pos_back_end.db.models.restaurant import Restaurant


class RestaurantServices:

    @staticmethod
    def post_restaurant(name, email, phone_number, admin_id, address_id):
        new_restaurant = Restaurant(
            restaurant_name=name,
            restaurant_email=email,
            phone_number=phone_number,
            admin_id=admin_id,
            address_id=address_id
        )

        return new_restaurant
