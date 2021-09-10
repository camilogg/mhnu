from django.urls import path

from .views import SliderAPIListView, MemberAPIListView

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
    )
]
