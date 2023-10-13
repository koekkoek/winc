import models
import peewee
from typing import List

__winc_id__ = "286787689e9849969c326ee41d8c53c4"
__human_name__ = "Peewee ORM"


def cheapest_dish() -> models.Dish:
    """You want ot get food on a budget

    Query the database to retrieve the cheapest dish available
    """
    return models.Dish.select().order_by(models.Dish.price_in_cents.asc()).first()


def vegetarian_dishes() -> List[models.Dish]:
    """You'd like to know what vegetarian dishes are available

    Query the database to return a list of dishes that contain only
    vegetarian ingredients.
    """
    dishes_list = []
    for dish in models.Dish.select():
        vegi_check = []
        for ingredient in dish.ingredients:
            vegi_check.append(ingredient.is_vegetarian)
        if all(vegi_check):
            dishes_list.append(dish)
    # print(dish)
    return dishes_list


def best_average_rating() -> models.Restaurant:
    """You want to know what restaurant is best

    Query the database to retrieve the restaurant that has the highest
    rating on average
    """
    avg_rating = peewee.fn.AVG(models.Rating.rating).alias("average_rating")

    query = (
        models.Restaurant.select(models.Restaurant, avg_rating)
        .join(models.Rating)
        .group_by(models.Restaurant)
        .order_by(avg_rating.desc())
        .limit(1)
    )
    highest_rated_restaurant = query.get()
    return highest_rated_restaurant


def add_rating_to_restaurant() -> None:
    """After visiting a restaurant, you want to leave a rating

    Select the first restaurant in the dataset and add a rating
    """
    query = models.Rating.select(models.Rating.restaurant, models.Rating.rating)
    firstRestaurant = query.get()
    firstRestaurant.update(rating = 1)
    firstRestaurant.save()

    return firstRestaurant.rating


def dinner_date_possible() -> List[models.Restaurant]:
    """You have asked someone out on a dinner date, but where to go?

    You want to eat at around 19:00 and your date is vegan.
    Query a list of restaurants that account for these constraints.
    """
    a = [restaurant for restaurant in
            (models.Restaurant
             .select(models.Restaurant, models.Dish)
             .join(models.Dish)
             .join(models.DishIngredient)
             .join(models.Ingredient)
             .where(models.Restaurant.closing_time >= '19:00')
             .group_by(models.Dish.name))
            if all(ingredient.is_vegan for ingredient in restaurant.dish.ingredients)
            ]
    return a


    #query = (models.Restaurant
    #         .select(models.Restaurant, models.Dish, models.Ingredient)
    #         .join(models.Dish, models.Ingredient)
    #         .where(models.Ingredient.is_vegan is True))
    #for restaurant in query:
    #    print(restaurant.name)


    #for dish in models.Dish.select():
    #    if (models.Dish.select(models.Dish, models.Ingredient)
    #        .join(models.Ingredient, on=(models.Ingredient.is_vegetarian))
    #        .where(models.Ingredient.is_vegetarian == True)):
    #        vegan_dishes.update(dish)


def add_dish_to_menu() -> models.Dish:
    """You have created a new dish for your restaurant and want to add it to the menu

    The dish you create must at the very least contain 'cheese'.
    You do not know which ingredients are in the database, but you must not
    create ingredients that already exist in the database. You may create
    new ingredients however.
    Return your newly created dish
    """
    ingredient_data = [
        ("milk", True, False, True),
        ("macaroni", True, True, False)
    ]

    for ingredient in ingredient_data:
        models.Ingredient.get_or_create(
            name=ingredient[0],
            is_vegetarian=ingredient[1],
            is_vegan=ingredient[2],
            is_glutenfree=ingredient[3])

    ingredient_1_id = models.Ingredient.get(
        models.Ingredient.name == 'cheese').id
    ingredient_2_id = models.Ingredient.get(
        models.Ingredient.name == 'macaroni').id

    models.Dish.get_or_create(
        name='Mac n Cheese',
        served_at_id=1,
        price_in_cents=500)

    dish_id = models.Dish.get(models.Dish.name == 'Mac n Cheese').id

    models.DishIngredient.get_or_create(
        dish_id=dish_id,
        ingredient_id=ingredient_1_id)

    models.DishIngredient.get_or_create(
        dish_id=dish_id,
        ingredient_id=ingredient_2_id)

    return (models.Dish
            .get(models.Dish.name == 'Mac n Cheese'))


if __name__ == "__main__":
    print(dinner_date_possible())
