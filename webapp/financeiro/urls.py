from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('admin/', admin.site.urls),
    path('users/', views.users, name='users'),
    path('users/<int:page_index>', views.users_pagination, name='users'),
    path('users/view/<int:id>', views.user_view, name='users'),
    path('users/add/', views.user_add, name='empresas'),
    path('users/edit/<int:id>', views.user_edit, name='users'),
    path('users/delete/<int:id>', views.user_delete, name='users'),
    path('empresas/', views.empresas, name='empresas'),
    path('empresas/<int:page_index>', views.empresas_pagination, name='empresas'),
    path('empresas/view/<int:id>', views.empresa_view, name='empresas'),
    path('empresas/add/', views.empresa_add, name='empresas'),
    path('empresas/edit/<int:id>', views.empresa_edit, name='empresas'),
    path('empresas/delete/<int:id>', views.empresa_delete, name='empresas'),
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/<int:page_index>', views.clientes_pagination, name='clientes'),
    path('clientes/view/<int:id>', views.cliente_view, name='clientes'),
    path('clientes/add/', views.cliente_add, name='clientes'),
    path('clientes/edit/<int:id>', views.cliente_edit, name='clientes'),
    path('clientes/delete/<int:id>', views.cliente_delete, name='clientes'),
    path('fornecedores/', views.fornecedores, name='fornecedores'),
    path('fornecedores/<int:page_index>', views.fornecedores_pagination, name='fornecedores'),
    path('fornecedores/view/<int:id>', views.fornecedor_view, name='fornecedores'),
    path('fornecedores/add/', views.fornecedor_add, name='fornecedores'),
    path('fornecedores/edit/<int:id>', views.fornecedor_edit, name='fornecedores'),
    path('fornecedores/delete/<int:id>', views.fornecedor_delete, name='fornecedores'),
    path('contas-bancarias/', views.contas_bancarias, name='contasbancarias'),
    path('contas-bancarias/<int:page_index>', views.contas_bancarias_pagination, name='contasbancarias'),
    path('planos-contas/', views.plano_de_contas, name='planocontas'),
    path('planos-contas/<int:page_index>', views.plano_de_contas_pagination, name='planocontas'),
    path('formas-pagamento/', views.formas_pagamento, name='formaspagamento'),
    path('formas-pagamento/<int:page_index>', views.formas_pagamento_pagination, name='formaspagamento'),
    path('tesouraria/', views.tesouraria, name='tesouraria'),
    path('tesouraria/<int:page_index>', views.tesouraria_pagination, name='tesouraria'),
    path('lancamentos-a-pagar/', views.lancamentos_a_pagar, name='lancamentos_a_pagar'),
    path('lancamentos-a-pagar/<int:page_index>', views.lancamentos_a_pagar_pagination, name='lancamentos_a_pagar'),
    path('lancamentos-a-pagar/view/<int:id>', views.lancamentos_a_pagar_view, name='lancamentos_a_pagar'),
    path('lancamentos-a-pagar/add/', views.lancamentos_a_pagar_add, name='lancamentos_a_pagar'),
    path('lancamentos-a-pagar/edit/<int:id>', views.lancamentos_a_pagar_edit, name='lancamentos_a_pagar'),
    path('lancamentos-a-pagar/delete/<int:id>', views.lancamentos_a_pagar_delete, name='lancamentos_a_pagar'),
    path('lancamentos-a-receber/', views.lancamentos_a_receber, name='lancamentos_a_receber'),
    path('lancamentos-a-receber/<int:page_index>', views.lancamentos_a_receber_pagination, name='lancamentos_a_receber'),
    path('lancamentos-a-receber/view/<int:id>', views.lancamentos_a_receber_view, name='lancamentos_a_receber'),
    path('lancamentos-a-receber/add/', views.lancamentos_a_receber_add, name='lancamentos_a_receber'),
    path('lancamentos-a-receber/edit/<int:id>', views.lancamentos_a_receber_edit, name='lancamentos_a_receber'),
    path('lancamentos-a-receber/delete/<int:id>', views.lancamentos_a_receber_delete, name='lancamentos_a_receber'),
    path('baixas-a-pagar/', views.baixas_a_pagar, name='baixas_a_pagar'),
    path('baixas-a-pagar/<int:page_index>', views.baixas_a_pagar_pagination, name='baixas_a_pagar'),
    path('baixas-a-pagar/view/<int:id>', views.baixas_a_pagar_view, name='baixas_a_pagar'),
    path('baixas-a-pagar/add/', views.lancamentos_a_pagar_add, name='lancamentos_a_pagar'),
    path('baixas-a-pagar/edit/<int:id>', views.baixas_a_pagar_edit, name='baixas_a_pagar'),
    path('baixas-a-pagar/delete/<int:id>', views.baixas_a_pagar_delete, name='baixas_a_pagar'),
    path('baixas-a-receber/', views.baixas_a_receber, name='baixas_a_receber'),
    path('baixas-a-receber/<int:page_index>', views.baixas_a_receber_pagination, name='baixas_a_receber'),
    path('baixas-a-receber/view/<int:id>', views.baixas_a_receber_view, name='baixas_a_receber'),
    path('baixas-a-receber/add/', views.baixas_a_receber_add, name='baixas_a_receber'),
    path('baixas-a-receber/edit/<int:id>', views.baixas_a_receber_edit, name='baixas_a_receber'),
    path('baixas-a-receber/delete/<int:id>', views.baixas_a_receber_delete, name='baixas_a_receber'),

]
