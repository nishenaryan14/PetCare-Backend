
from django.urls import path
from .views import SignupView, LoginView, AddFavoritePetView, GetFavoritePetsView, SuggestBreedView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('add-favorite-pet/<str:user_id>/', AddFavoritePetView.as_view(), name='add-favorite-pet'),
    path('favorite-pets/<str:user_id>/', GetFavoritePetsView.as_view(), name='favorite-pets'),
    path('suggest-breed/', SuggestBreedView.as_view(), name='suggest_breed'),
]
