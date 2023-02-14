# Provas e Gabaritos Engenheiro Civil

Este é um script Python que realiza web scraping para coletar links para provas e gabaritos do cargo de Engenheiro Civil no site pciconcursos.com.br. O script segue os seguintes passos:

1. Cria uma lista com todos os links para as páginas de provas e gabaritos do cargo de Engenheiro Civil.
2. Filtra apenas os links relacionados ao cargo de Engenheiro Civil.
3. Coleta os links para as provas e gabaritos e cria um dicionário com ambos.
4. Cria uma lista final contendo todos os dicionários.
5. Salva a lista em um arquivo txt chamado "provas_gabaritos_engenheiro_civil.txt".

O objetivo deste script é facilitar a coleta de informações sobre provas e gabaritos para o cargo de Engenheiro Civil no site pciconcursos.com.br. Para usar o script, basta executá-lo e esperar o término da execução. O arquivo com a lista final será salvo na mesma pasta do arquivo Python. Certifique-se de ter as bibliotecas "requests" e "beautifulsoup4" instaladas antes de executar o script.

# Issues

Essa versão apresenta um tempo médio de execução muito alto e pode gerar arquivos duplicados devido a falta de verificação.

# Licença

Vide o arquivo license
