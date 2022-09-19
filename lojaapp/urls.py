from django.urls import path
from.views import *

app_name = "lojaapp"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("sobre/", SobreView.as_view(), name="sobre"),
    path("contato/", ContatoView.as_view(), name="contato"),
    path("todos-produtos/", TodosProdutosView.as_view(), name="todosprodutos"),
    path("produto/<slug:slugs>/", DetalheView.as_view(), name="detalhe"),

]
