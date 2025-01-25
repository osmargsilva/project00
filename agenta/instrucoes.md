# Modelo de Agenda de Contatos em Python

## Funcionalidades Principais

# Adicionar Contato:

Permite adicionar um novo contato à agenda.
Cada contato deve ter atributos como nome, telefone e email.
Buscar Contato:

Permite buscar um contato específico na agenda pelo nome.
Exibe as informações do contato se encontrado.
Remover Contato:

Permite remover um contato da agenda pelo nome.
Confirma se o contato foi removido com sucesso.
Listar Contatos:

Exibe todos os contatos armazenados na agenda.
Mostra os detalhes de cada contato (nome, telefone, email).
Estrutura do Código
Classe Contato:

Representa um contato individual.
Contém atributos como nome, telefone e email.
Classe Agenda:

Gerencia uma lista de contatos.
Contém métodos para adicionar, buscar, remover e listar contatos.
Descrição Detalhada das Funcionalidades
Adicionar Contato:

Crie um método adicionar_contato na classe Agenda.
Este método deve receber os parâmetros necessários (nome, telefone, email) e criar um novo objeto Contato.
Adicione o novo contato à lista de contatos da agenda.
Buscar Contato:

Crie um método buscar_contato na classe Agenda.
Este método deve receber um nome como parâmetro e procurar na lista de contatos.
Retorne o contato encontrado ou uma mensagem indicando que o contato não foi encontrado.
Remover Contato:

Crie um método remover_contato na classe Agenda.
Este método deve receber um nome como parâmetro e usar o método buscar_contato para localizar o contato.
Remova o contato da lista se encontrado e confirme a remoção.
Listar Contatos:

Crie um método listar_contatos na classe Agenda.
Este método deve iterar sobre a lista de contatos e exibir os detalhes de cada um.
Estrutura de Estudo
Definição das Classes:

Defina as classes Contato e Agenda.
Implemente os atributos e métodos descritos acima.
Testes e Exemplos:

Crie uma instância da classe Agenda.
Adicione alguns contatos usando o método adicionar_contato.
Busque e remova contatos para verificar o funcionamento dos métodos.
Liste todos os contatos para garantir que a agenda está armazenando e exibindo os dados corretamente.
Objetivo de Estudo
Este modelo fornece uma base sólida para entender conceitos como:

Criação e manipulação de classes e objetos em Python.
Implementação de métodos para gerenciar dados.
Práticas de programação orientada a objetos (OOP).
Com base neste modelo, você pode expandir a funcionalidade da agenda, adicionando recursos como a persistência de dados em arquivos, a interface gráfica, ou a integração com bancos de dados para tornar o projeto mais robusto e completo.