# Buscador de Vagas

Este é um script em Python que automatiza a busca de vagas de emprego no LinkedIn de acordo com a palavra-chave informada. Ele coleta informações como Título da vaga, Empresa, Local, Link e Data de Publicação, e exporta tudo para um arquivo Excel.

## Tecnologias e Bibliotecas Utilizadas
- **Python 3**
- **Selenium**: Para automação do navegador web e interação com a página do LinkedIn.
- **Pandas**: Para organização dos dados coletados em formato de tabela.
- **Openpyxl**: Dependência necessária para o Pandas conseguir exportar os dados para o formato Excel (`.xlsx`).

## Como instalar as dependências
Para que o código funcione corretamente, você precisa instalar as bibliotecas citadas acima. Abra o terminal (ou prompt de comando) no seu computador e execute o seguinte comando:

```bash
pip install selenium pandas openpyxl
```

**Nota:** O Selenium utilizado neste projeto abre o Google Chrome. Certifique-se de ter o navegador Chrome instalado na sua máquina.

## Como utilizar

1. Execute o arquivo `main.py` no seu terminal ou ambiente de desenvolvimento:
   ```bash
   python main.py
   ```
2. O programa irá perguntar: `Digite O Nome Da Vaga :`
3. Digite o cargo ou vaga que deseja procurar (ex: `Python Developer`) e pressione **Enter**.
4. Uma janela do Google Chrome se abrirá de forma automática, buscará pela vaga pesquisada e coletará os dados.
5. Ao finalizar o processo, a janela se fechará sozinha e o script irá gerar um arquivo chamado `Vagas_Encontradas.xlsx` na mesma pasta do projeto, contendo todos os dados encontrados.
