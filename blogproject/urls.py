from django.contrib import admin
from django.urls import path, include 
from strawberry.django.views import GraphQLView
from app.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path("graphql", GraphQLView.as_view(schema=schema)),
]
