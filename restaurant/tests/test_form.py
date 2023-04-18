from django.test import TestCase
from django import forms

from restaurant.forms import (
    DishForm,
    CookCreationForm,
    CookSearchForm,
    SearchForm,
)
from restaurant.models import Ingredient, Cook, DishType


class CookFormsTest(TestCase):
    def test_cook_creation_form_with_years_of_experience_first_last_name(self):
        """This test verifies that the creation form for the Cook model works
        correctly. Specifically, the test checks that if the form is filled
        out correctly, the form will be considered valid and the data
        obtained from the form after cleaning will be equal
        to the original data. """
        form_data = {
            "username": "new_user",
            "password1": "user123test",
            "password2": "user123test",
            "first_name": "Test first",
            "last_name": "Test last",
            "years_of_experience": 1,
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class TestDishForm(TestCase):
    """These tests check the validity of the DishForm. The first test verifies
    that the form is valid when a correct set of data, including ingredients,
    dish type, and chef, is passed to it. The second test checks that
    the form is invalid when a set of data with an incorrect ID for one of the
    ingredients is passed to it."""
    def setUp(self):
        cook = Cook.objects.create(
            years_of_experience=1
        )
        dish_type = DishType.objects.create(
            name="Soup",
        )
        self.ingredient1 = Ingredient.objects.create(name="Ingredient 1")
        self.ingredient2 = Ingredient.objects.create(name="Ingredient 2")
        self.dish_data = {
            "name": "Test Dish",
            "description": "Test Description",
            "price": "10.99",
            "dish_type": dish_type,
            "cooks": [cook.id]

        }

    def test_valid_form(self):
        """This test checks that the DishForm is valid when a correct set
        of data is passed to it, including the ingredients, dish type,
        and cook."""
        data = self.dish_data.copy()
        data["ingredients"] = [self.ingredient1.id, self.ingredient2.id]
        form = DishForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """This test checks that the DishForm is invalid when an invalid ID
        is passed for one of the ingredients in the form data."""
        data = self.dish_data.copy()
        data["ingredients"] = [self.ingredient1.id, "invalid_id"]
        form = DishForm(data=data)
        self.assertFalse(form.is_valid())


class CookSearchFormTest(TestCase):
    """These tests are checking the CookSearchForm form. The first test
    checks that the only form field is username. The second test checks
    that the widget used for the username field is a forms.TextInput."""
    def test_form_fields(self):
        form = CookSearchForm()
        expected_fields = ["username"]
        self.assertSequenceEqual(list(form.fields), expected_fields)

    def test_username_widget(self):
        form = CookSearchForm()
        self.assertIsInstance(form.fields["username"].widget, forms.TextInput)


class SearchFormTest(TestCase):
    """These tests are checking the SearchForm, which has a single field for
    searching objects by name in the model. The first test verifies that
    the form contains only one field with the name "name". The second test
    verifies that the widget used in the "name" field is a TextInput."""
    def test_form_fields(self):
        form = SearchForm()
        expected_fields = ["name"]
        self.assertSequenceEqual(list(form.fields), expected_fields)

    def test_model_widget(self):
        form = SearchForm()
        self.assertIsInstance(form.fields["name"].widget, forms.TextInput)
