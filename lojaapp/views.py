from django.shortcuts import render
from django.views.generic import TemplateView
from.models import *





class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produto_list']= Produto.objects.all()
        return context

class SobreView(TemplateView):
   template_name = "sobre.html"

class ContatoView(TemplateView):
    template_name = "contato.html"

class TodosProdutosView(TemplateView):
     template_name = "todosprodutos.html"
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todascategorias']= Categoria.objects.all().order_by("-id")
        return context


class DetalheView(TemplateView):
     template_name = "detalhe.html"
     
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs['slugs']
        produto = Produto.objects.get(slug=url_slug)
        context['produto']= produto
        return context
    