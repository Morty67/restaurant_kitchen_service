from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from restaurant.models import Dish, DishType, Cook


class AdminSiteTest(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345",
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="cook",
            password="cook123",
            years_of_experience="1",
        )

    def test_cook_years_of_experience_listed(self):
        """Test that cook's years_of_experience is in
         list _display on cook admin page"""
        url = reverse("admin:restaurant_cook_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_detailed_years_of_experience_listed(self):
        """Test that cook's years_of_experience is in cook detail admin
        page"""
        url = reverse("admin:restaurant_cook_change", args=[self.cook.pk])
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)

    def test_search_dish_by_name(self):
        """This test verifies that when searching for a dish by name
        in the Django admin panel, only the dish object whose name matches
        the search query "Green Soup" is returned, and that other dishes
        are not displayed in the search results. """
        cook = Cook.objects.create(
            years_of_experience=1
        )
        dish_type = DishType.objects.create(
            name="Soup",
        )
        dish1 = Dish.objects.create(
            name="Green Soup",
            description="tasty",
            price="13.99",
            dish_type=dish_type
        )
        dish1.cooks.set([cook])
        dish2 = Dish.objects.create(
            name="Borsch",
            description="tasty",
            price="13.99",
            dish_type=dish_type
        )
        dish2.cooks.set([cook])
        search_url = reverse(
            "admin:restaurant_cook_changelist"
        ) + "?q=Green Soup"
        response = self.client.get(search_url)
        self.assertContains(response, dish1.name)
        self.assertNotContains(response, dish2.name)
