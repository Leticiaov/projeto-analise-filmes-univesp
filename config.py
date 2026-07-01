"""
Configurações do projeto de análise exploratória.
Centraliza parâmetros para facilitar manutenção.
"""

# Configurações de visualização
FIGSIZE_DEFAULT = (10, 6)
FIGSIZE_WIDE = (12, 5)
FIGSIZE_LARGE = (12, 6)

# Cores dos gráficos
COLOR_PRIMARY = 'skyblue'
COLOR_SECONDARY = 'coral'
COLOR_SUCCESS = 'lightgreen'
COLOR_DANGER = 'red'
COLOR_WARNING = 'orange'

# Configurações de dados
DATA_URL = "https://raw.githubusercontent.com/danielgrijalva/movie-stats/master/movies.csv"
CACHE_PATH = "data/movies.csv"

# Colunas necessárias para validação
REQUIRED_COLUMNS = ['score', 'genre', 'year', 'name']

# Configurações de estilo
PLOT_STYLE = "whitegrid"
DPI_DEFAULT = 300
