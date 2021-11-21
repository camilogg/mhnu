from django.urls import path

from .views import SliderAPIListView, MemberAPIListView, PostAPIListView

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
        route='posts',
        view=PostAPIListView.as_view(),
        name='post_list'
    )
]
