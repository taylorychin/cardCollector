from django.urls import path
from . import views

urlpatterns = [
    # routes localhost:8000
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('decks/', views.decks_index, name='index'),
    path("decks/<int:deck_id>/", views.decks_detail, name='detail'),
    path('decks/create/', views.DeckCreate.as_view(), name='decks_create'),
    path('decks/<int:pk>/update/', views.DeckUpdate.as_view(), name='decks_update'),
    path('decks/<int:pk>/delete/', views.DeckDelete.as_view(), name='decks_delete'),

    path('decks/<int:deck_id>/add_extra/',
         views.add_extra, name='add_extra'),
    path('extras/<int:pk>/update/',
         views.ExtraUpdate.as_view(), name='extras_update'),
    path('extras/<int:pk>/delete/',
         views.ExtraDelete.as_view(), name='extras_delete'),


    # path('accessories/<int:pk>/update/',
    #      views.AccUpdate.as_view(), name='acc_update'),
    # path('accessories/<int:pk>/delete/',
    #      views.AccDelete.as_view(), name='acc_delete'),

    path('accessories/', views.AccList.as_view(), name='accs_index'),
    path('accessories/<int:pk>/', views.AccDetail.as_view(), name='accs_detail'),
    path('accessories/create/', views.AccCreate.as_view(), name='accs_create'),
    path('accessories/<int:pk>/update/',
         views.AccUpdate.as_view(), name='accs_update'),
    path('accessories/<int:pk>/delete/',
         views.AccDelete.as_view(), name='accs_delete'),
    path('decks/<int:deck_id>/assoc_accessory/<int:accessory_id>/',
         views.assoc_acc, name='assoc_acc'),
]
