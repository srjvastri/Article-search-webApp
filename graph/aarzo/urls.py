from django.urls import path
from .import views

urlpatterns = [

    # path("", views.home, name="home"),
    path("", views.index, name="index"),
    # path("", views.plot_cum_returns, name="plot_cum_returns"),
    # path("combo/", views.combo, name="combo"),
    # path("programming/", views.programming, name="programming"),
    # path("multi_plot/", views.multi_plot, name="multi_plot"),
    # path("products/", views.products, name="products"),
    # path("pie/", views.pie, name="pie"),
    # path("test_html/", views.test_html, name="test_html"),

    
]