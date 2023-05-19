from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoriesAPIViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('categories/<int:id>/', views.CategoriesAPIViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
     })),

    path('reviews/', views.ReviewsAPIViews.as_view()),
    path('reviews/<int:id>/', views.ReviewsDetailAPIViews.as_view()),

    path('products/', views.ProductsAPIViews.as_view()),
    path('products/<int:id>/', views.RetrieveUpdateDestroyAPIView.as_view()),
    path('products/reviews/', views.ProductsReviewsAPIViews.as_view())
]