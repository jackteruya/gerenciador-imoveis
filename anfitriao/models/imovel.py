import uuid

from django.db import models


class UF(models.TextChoices):
    ACRE = 'ACRE', 'AC'
    ALAGOAS = 'ALAGOAS', 'AL'
    AMAPA = 'AMAPA', 'AP'
    AMAZONAS = 'AMAZONAS', 'AM'
    BAHIA = 'BAHIA', 'BA'
    CEARA = 'CEARA', 'CE'
    DISTRITO_FEDERAL = 'DISTRITO FEDERAL', 'DF'
    ESPIRITO_SANTO = 'ESPIRITO SANTO', 'ES'
    GOIAS = 'GOIAS', 'GO'
    MARANHAO = 'MARANHOA', 'MA'
    MATO_GROSSO = 'MATO GROSSO', 'MT'
    MATO_GROSSO_DO_SUL = 'MATO GROSSO DO SUL', 'MS'
    MINAS_GERAIS = 'MINAS GERAIS', 'MG'
    PARANA = 'PARANA', 'PR'
    PARAIBA = 'PARAIBA', 'PB'
    PARA = 'PARA', 'PA'
    PERNAMBUCO = 'PERNAMBUCO', 'PE'
    PIAUI = 'PIAUI', 'PI'
    RIO_GRANDE_DO_NORTE = 'RIO GRANDE DO NORTE', 'RN'
    RIO_GRANDE_DO_SUL = 'RIO GRANDE DO SUL', 'RS'
    RIO_DE_JANEIRO = 'RIO DE JANEIRO', 'RJ'
    RONDONIA = 'RONDONIA', 'RD'
    RORAIMA = 'RORAIMA', 'RR'
    SANTA_CATARINA = 'SANTA CATARINA', 'SC'
    SERGIPE = 'SERGIPE', 'SE'
    SAO_PAULO = 'SAO PAULO', 'SP'
    TOCANTINS = 'TOCANTINS', 'TO'


class Imovel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    logradoro = models.CharField(max_length=100)
    numero = models.CharField(max_length=7)
    bairro = models.CharField(max_length=50)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=20, choices=UF.choices)
    valor_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_pessoas = models.IntegerField()
    pets = models.BooleanField()
    quantidade_pets = models.IntegerField()

    def __str__(self):
        return f'{self.logradoro}, nº {self.numero}, {self.cidade}/{self.uf}'
