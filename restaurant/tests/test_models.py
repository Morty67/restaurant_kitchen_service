from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import DishType, Dish


class ModelsTests(TestCase):
    def test_cook_str(self):
        """In this test, we create an instance of the Cook model, set the
        values of all necessary fields (username, first_name, and last_name),
        and compare the string representation of the model to the expected
        value. """
        cook = get_user_model().objects.create_user(
            years_of_experience=1,
            username="test",
            first_name="Rick",
            last_name="Sanchez"
        )
        self.assertEqual(str(cook),
                         f"Username: {cook.username}, (Name: {cook.first_name}"
                         f"Surname: {cook.last_name})"
                         )

    def test_dish_type_str(self):
        """This test creates an instance of the DishType model, sets its name
        field, and compares its string representation with the expected value,
        which is the name of the dish type. """
        dish_type = DishType.objects.create(
            name="Soup",
        )
        self.assertEqual(str(dish_type), dish_type.name)

    def test_dish_str(self):
        """This test creates instances of related models, DishType and Cook,
        and creates an instance of the Dish model, setting its fields and
        assigning a Cook instance to its cooks many-to-many field.
        The test then compares the string representation of the Dish instance
        with its name field."""
        dish_type = DishType.objects.create(
            name="Soup"
        )
        cook = get_user_model().objects.create_user(
            years_of_experience=1,
            username="test",
            first_name="Rick",
            last_name="Sanchez"
        )
        dish = Dish.objects.create(
            name="Borsch",
            description="tasty",
            price="13.99",
            dish_type=dish_type,
        )
        dish.cooks.set([cook])
        self.assertEqual(str(dish), dish.name)

    def test_create_cook_years_of_experience(self):
        """This it checks whether the user is created successfully and the
        assigned values are stored correctly in the database. It verifies the
        username, password, and years_of_experience fields of the created user
        by calling the appropriate methods and assertions."""
        username = "test"
        password = "test12345"
        years_of_experience = 1
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience
        )
        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, years_of_experience)
