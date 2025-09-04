from pos_back_end.api.restaurant.restaurant_models import RestaurantItem, RestaurantsResponseBody
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

    @staticmethod
    def get_restaurants(admin_id, db):
        restaurants = db.query(Restaurant).where(Restaurant.admin_id == admin_id).all()
        restaurant_items = [RestaurantItem.model_validate(restaurant) for restaurant in restaurants]

        return RestaurantsResponseBody(restaurants=restaurant_items)

