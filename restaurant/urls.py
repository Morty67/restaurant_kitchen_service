from django.urls import path

from restaurant.views import (
    index,
    CookListView,
    CookDetailView,
    DishTypeListView,
    DishTypeDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    IngredientListView,
    IngredientDetailView,
    IngredientCreateView,
    IngredientDeleteView,
    IngredientUpdateView,

)

urlpatterns = [
    path("", index, name="index"),
    path(
        "cook/",
        CookListView.as_view(),
        name="cook-list",
    ),
    path("cook/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path(
        "dish-type/",
        DishTypeListView.as_view(),
        name="dish-type-list",
    ),
    path(
        "dish-type/<int:pk>/",
        DishTypeDetailView.as_view(),
        name="dish-type-list-detail",
    ),
    path(
        "dish-type/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-list-create",
    ),
    path(
        "dish-type/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-list-update",
    ),
    path(
        "dish-type/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-list-delete",
    ),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dish/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update/",
         DishUpdateView.as_view(),
         name="dish-update"
         ),
    path("dish/<int:pk>/delete/",
         DishDeleteView.as_view(),
         name="dish-delete"
         ),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("ingredients/<int:pk>/",
         IngredientDetailView.as_view(),
         name="ingredient-detail"
         ),
    path("ingredients/create/", IngredientCreateView.as_view(),
         name="ingredient-create"),
    path("ingredients/<int:pk>/delete/", IngredientDeleteView.as_view(),
         name="ingredient-delete"),
    path("ingredients/<int:pk>/update/", IngredientUpdateView.as_view(),
         name="ingredient-update"),

]

app_name = "restaurant"
