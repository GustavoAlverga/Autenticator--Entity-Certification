# Autenticator--Entity-Certification
Projeto complementar do projeto autenticador
Adiciona uma entidade certificadora para retirar a responsabilidade dos services de ter as chaves privadas dos serviços concentrando em uma entidade que tem todas as chaves
dois serviços vão se autenticar e delega essa responsabilidade de fazer a comparação dos hash`s para a entidade que tem todas as chaves dos serviços legitimos se a entidade tem a a chave do serviço retorna true e libera a autenticação caso contrário nega com false e falha a autenticação

Para rodar o projeto
python3 main.py
