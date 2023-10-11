# Sistema de Raspagem de Dados do Portfólio

Este é um sistema de raspagem de dados que varre o meu site de portfólio pessoal e coleta informações sobre meus projetos, incluindo os links do GitHub associados a cada projeto. A raspagem de dados é realizada usando a biblioteca Scrapy em Python.

## Como Funciona

Este sistema de raspagem funciona da seguinte forma:

1. Começa em uma URL específica do meu site de portfólio, que lista meus projetos.
2. Usa Scrapy para fazer uma solicitação HTTP para a página e recuperar o conteúdo HTML.
3. Analisa o HTML em busca de elementos que contenham informações sobre meus projetos.
4. Extrai o nome do projeto, a descrição e o link do GitHub a partir do HTML.
5. Armazena as informações coletadas em um formato estruturado, como JSON ou CSV.

## Executando a Raspagem

Para executar a raspagem de dados, siga estas etapas:

1. Certifique-se de ter o Scrapy instalado no seu ambiente Python.
2. Clone este repositório em sua máquina.
3. Abra um terminal na pasta do projeto e execute o seguinte comando:

```bash
scrapy crawl ml -o projetos.json
```

Este comando executará a spider chamada "ml" e salvará os dados coletados em um arquivo JSON chamado "projetos.json". Você pode ajustar o nome do arquivo de saída e o nome da spider conforme necessário.

## Personalização

Este sistema de raspagem pode ser personalizado para se adequar às necessidades do seu próprio site de portfólio. Você pode ajustar as expressões XPath para corresponder à estrutura HTML do seu site e também adicionar informações adicionais que deseja coletar.

## Contribuições

Se você deseja contribuir para este projeto, sinta-se à vontade para enviar solicitações de pull com melhorias ou correções.
