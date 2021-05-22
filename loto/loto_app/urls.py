from django.urls import path

from loto.loto_app import views
from loto.loto_app.views import mybetsview, edit_bet, player_choice, player_bets, event_choice, event_bets, ranking_view

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('my_bets/', mybetsview, name='my bets'),
    path('edit/<int:pk>/', edit_bet, name='edit bet'),
    path('player/', player_choice, name='player'),
    path('player_bets/<int:pk>/', player_bets, name='player bets'),
    path('event/', event_choice, name='event'),
    path('event_bets/<int:pk>/', event_bets, name='event bets'),
    path('ranking/', ranking_view, name='ranking'),
]