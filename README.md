# ADS Libras

**Feito pelos alunos:**
- [Beatriz Querubim Batista](https://www.linkedin.com/in/beatriz-querubim-943840217/)
- [Caroline Smarzaro](https://www.linkedin.com/in/carolinesmarzaro/)
- [Gustavo Pinto da Silva]()

**Instituto Federal de Educação, Ciência e Tecnologia de São Paulo**  
Câmpus Bragança Paulista

### Descrição do Projeto

O projeto **ADS Libras** é um glossário de termos técnicos do curso de Tecnologia em Análise e Desenvolvimento de Sistemas, disponível em Libras-Português. O objetivo é facilitar o acesso de alunos surdos às terminologias e conteúdos do curso, proporcionando uma melhor compreensão e aprendizado.

### Agradecimentos

Gostaríamos de agradecer a todas as pessoas que, de uma forma ou de outra, colaboraram para que este trabalho fosse realizado. Em especial:

- [**Professor Rafael da Silva Muniz**](https://www.linkedin.com/in/rafael-muniz-57949456/): por sua compreensão, competência e orientação durante todo o desenvolvimento desta monografia.
- [**Profª Talita de Paula Cypriano de Souza**](https://www.linkedin.com/in/talita-cypriano/): pela coorientação.
- [**Profa. Dra. Ana Paula Müller Giancoli**](https://www.linkedin.com/in/ana-paula-müller-giancoli/) Ao apoio nas orientações do projeto e documentações. 
- [**Letícia Leite Batista Nascimento**](https://www.linkedin.com/in/leticia-leite-batista-nascimento-37896a323/): tradutora e intérprete de Libras, pela colaboração e atenção.
- Nossos **pais, familiares e amigos**, com ênfase aos pais, Lilian Maria Pinto da Silva e José Ilzan Cavalcante Damasceno, e ao amigo [Paulo Basalces](https://www.linkedin.com/in/basalces/), pelo suporte e apoio.

### Importância do Projeto

A graduação é uma etapa crucial na formação de um indivíduo, especialmente considerando o aumento da participação de alunos surdos no ensino superior. Este trabalho visa oferecer recursos que ajudem na inclusão e acessibilidade, como a utilização de intérpretes de Libras, materiais didáticos e atividades adaptadas.

O glossário de termos técnicos em Libras será uma ferramenta importante para acadêmicos surdos, professores e tradutores intérpretes, permitindo um acesso mais claro e rápido às informações relevantes.

**Palavras-chave:** Libras; Glossário; Tecnologia.

## Índice

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instruções para Instalação](#instruções-para-instalação)
- [Instruções para quem baixar o projeto](#instruções-para-quem-baixar-o-projeto)
- [Contribuição](#contribuição)

## Tecnologias Utilizadas

- Figma
- Workbench
- SQL Client
- Python
- Django
- HTML
- CSS
- overleaf (para documentação)

## Instruções para Instalação

1. **Clonar o repositório:**
    ```bash
    git clone https://github.com/Bea-Querubim/TCC-GlossarioLibras.git
    cd TCC-GlossarioLibras
    ```

2. **Criar um ambiente virtual e ativá-lo:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/Mac
    venv\Scripts\activate     # No Windows
    ```

3. **Instalar as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configurar o banco de dados:**
    - Rodar as migrações:
    ```bash
    python manage.py migrate
    ```

    - Se você compartilhou o arquivo `db.json`, pode carregá-lo:
    ```bash
    python manage.py loaddata db.json
    ```

5. **Rodar o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas.

