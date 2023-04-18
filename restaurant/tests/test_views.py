from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from restaurant.models import DishType, Cook, Dish

DISH_TYPE = reverse("restaurant:dish-type-list")
DISH_URL = reverse("restaurant:dish-list")
COOK_LIST = reverse("restaurant:cook-list")
INGREDIENT_LIST = reverse("restaurant:ingredient-list")


class PublicDishTypeTest(TestCase):
    """This test checks that access to the Dish Type view is restricted to
    authenticated users. It sends a GET request to the view and asserts that
    the response status code is not 200, indicating that the user is not
    authorized to access the view."""
    def test_login_required(self):
        res = self.client.get(DISH_TYPE)
        self.assertNotEqual(res.status_code, 200)


class PublicDishTets(TestCase):
    """This test checks the access to the page with the list of dishes for
    unauthenticated users. The expected result is that the page should
    not be accessible and the response status code should not be 200."""

    def test_login_required(self):
        res = self.client.get(DISH_TYPE)
        self.assertNotEqual(res.status_code, 200)


class PublicCookTets(TestCase):
    """This test checks access to the page with the list of cooks for
    unauthorized users. The expected result is that the page should
    not be accessible and the status code should not be 200."""

    def test_login_required(self):
        res = self.client.get(INGREDIENT_LIST)
        self.assertNotEqual(res.status_code, 200)


class PublicIngredientTets(TestCase):
    """This test checks access to the page with the list of cooks for
    authorized users. The expected result is that the page should
    not be accessible and the status code should not be 200."""
    def test_login_required(self):
        res = self.client.get(COOK_LIST)
        self.assertNotEqual(res.status_code, 200)


class PrivateCookTest(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "test12345",
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_type(self):
        """This test checks access to the page with the list of dish types for
        authorized users. The expected result is that the page should be
        accessible and the response status code should be 200."""
        DishType.objects.create(name="Soup")
        DishType.objects.create(name="Seafood")

        res = self.client.get(DISH_TYPE)
        dish_type = DishType.objects.all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["dish_type_list"]),
            list(dish_type)
        )


class CookToggleAssignToDishTestCase(TestCase):
    """This test case checks whether a cook can be assigned to a dish and then
    removed from it by toggling a button on a web page. The test logs
    in a cook, asserts that the cook is not assigned to the dish, then posts
    a request to toggle the cook's assignment to the dish, and asserts that the
    cook is now assigned to the dish."""
    def setUp(self):
        self.client = Client()
        self.cook = get_user_model().objects.create_user(
            username="cook",
            password="cook12345",
            years_of_experience=2,
        )
        self.dish_type = DishType.objects.create(
            name="Soup"
        )
        self.dish = Dish.objects.create(
            name="Borsh",
            price="14.43",
            dish_type=self.dish_type,
        )
        self.url = reverse(
            "restaurant:toggle-dish-assign",
            args=[self.dish.id]
        )

    def test_toggle_assign_to_dish(self):
        self.client.force_login(self.cook)
        self.assertTrue(self.dish not in self.cook.dishes.all())
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.dish in self.cook.dishes.all())
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.dish not in self.cook.dishes.all())
