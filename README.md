#Projeto API para Gerenciar Operações de Imoveis

###Para esse projeto:
- Crie um virtual enviroment, ative o mesmo e utilize o seguinte comando para instalar as dependência do projeto. `pip install -r requirements.txt`
- Foi utilizado Docker-Compose para este projeto, então para utilizar este projeto segue passo:
            - No terminal, vá até o diretorio deste projeto:
            - Digitar o seguinte comando -> docker-compose build
            - docker-compose run api python manage.py migrate
            - docker-compose run api python manage.py createsuperuser (caso queira utilizar o painel admin)
            - docker-compose up
            - abra o navegador e digite localhost:8000/admin/
- Caso tenha necessida de resetar o banco de dados:
            - docker-compose down
            - docker-compose rm
            - docker volume rm gerenciador-imoveis_database


###Contexto:
Em um empresa que gerencia operações de seus imóveis, é necessario estar o acompanhamento das operações, a figura principal é do anfitrião, responsável por realizar presencialmente o check in, checkout, limpeza e manutenção do imovel.
Como é de muita importãncia a visualização das da agenda de maneira fácil e rápido foi o projeto foi implementado da seguinte forma:
  
models:
    - Anfitrião;
    - Hospede;
    - Imovel;
    - Reserva;
    - ToDo; (onde é gerenciado a agenda do Anfitrião) -> criado validadores para não ser possível incluir a fazeres no mesmo horário para um anfitrião

views:
    - Anfitrião;
    - Hospede;
    - Imovel;
    - Reserva;
    - ToDo; -> Nesta view foi incluida duas classe com o metodo GET que visualiza todos os anfitriões com sua lista da agenda e é possível pegar individualmente pelo id;

serializers:
    - Anfitrião;
    - Hospede;
    - Imovel;
    - Reserva;
    - ToDo; (onde é gerenciado a agenda do Anfitrião)


###Obs.: 
- Painel admin está pronto para uso;
- Caso prefira usar o sqlite pode ser alterado o banco de dados que já está configurado no arquivo setting.py
        ''' 
            """DATABASES = {
                    'default': {
                            'ENGINE': 'django.db.backends.sqlite3',
                            'NAME': BASE_DIR / 'db.sqlite3',
                      }
                }"""

           DATABASES = {
                        'default': {
                        'ENGINE': 'django.db.backends.postgresql_psycopg2',
                        'NAME': 'postgres',
                        'USER': 'postgres',
                        'PASSWORD': 'postgres',
                        'HOST': 'database',
                        'PORT': '5432',
                           }
                        }
        '''

