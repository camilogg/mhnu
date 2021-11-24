from django.urls import path

from .views import SliderAPIListView, MemberAPIListView, MemberRetrieveAPIView

app_name = 'web'
urlpatterns = [
    path(
        route='sliders',
        view=SliderAPIListView.as_view(),
        name='slider_list'
    ),
    path(
        route='members',
        view=MemberAPIListView.as_view(),
        name='member_list'
    ),
    path(
        route='members/<slug:slug>',
        view=MemberRetrieveAPIView.as_view(),
        name='member_list'
    ),
]
