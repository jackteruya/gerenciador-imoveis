from django.urls import path

from anfitriao.views import (ListarCriarAnfitriaoAPIView, VerAtualizarDeletarAnfitriaoAPIView,
                             ListarCrearHospedeAPIView, VerAtualizarDeletarHospedeAPIView,
                             ListarCrearImovelAPIView, VerAtualizarDeletarImovelAPIView,
                             ListarCrearReservaAPIView, VerAtualizarDeletarReservaAPIView,
                             ListarCrearToDoAPIView, VerAtualizarDeletarToDoAPIView,
                             ListarToDoAnfitriaoAPIVew, VerToDoAnfitriaoAPIVew)


urlpatterns = [
    # view do crud anfitriao
    path('anfitriao/', ListarCriarAnfitriaoAPIView.as_view(), name='listar-criar-anfitriao'),
    path('anfitriao/<uuid:pk>/', VerAtualizarDeletarAnfitriaoAPIView.as_view(), name='ver-atualizar-deletar-anfitriao'),

    # view do crud hospede
    path('hospede/', ListarCrearHospedeAPIView.as_view(), name='listar-criar-hospede'),
    path('hospede/<uuid:pk>/', VerAtualizarDeletarHospedeAPIView.as_view(), name='ver-atualizar-deletar-hospede'),

    # view do crud imovel
    path('imovel/', ListarCrearImovelAPIView.as_view(), name='listar-criar-imovel'),
    path('imovel/<uuid:pk>/', VerAtualizarDeletarImovelAPIView.as_view(), name='ver-atualizar-deletar-imovel'),

    # view do crud reserva
    path('reserva/', ListarCrearReservaAPIView.as_view(), name='listar-criar-reserva'),
    path('reserva/<uuid:pk>/', VerAtualizarDeletarReservaAPIView.as_view(), name='ver-atualizar-deletar-reserva'),

    # view do crud to_do
    path('to-do/', ListarCrearToDoAPIView.as_view(), name='listar-criar-to-do'),
    path('to-do/<uuid:pk>/', VerAtualizarDeletarToDoAPIView.as_view(), name='ver-atualizar-deletar-to-do'),

    # view para listar a agenda do anfitriao
    path('agenda-anfitriao/', ListarToDoAnfitriaoAPIVew.as_view(), name='lista-anfitriao-agendas'),
    path('agenda-anfitriao/<uuid:pk>/', VerToDoAnfitriaoAPIVew.as_view(), name='agenda-anfitriao'),
]
