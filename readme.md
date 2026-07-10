## JDGoogleDrive
Utilitário para realizar upload de arquivos no Google Drive utilizando OAuth 2.0.

## Autores
- [@duartejd](https://github.com/DuarteJD)

## Requisitos

- Python 3.10 ou superior
- Conta Google com API Google Drive habilitada
- Credenciais OAuth 2.0 válidas

## Instalação

Instale as dependências com:

```bash
pip install google-api-python-client google-auth
```

## Dependências
| Biblioteca | Finalidade |
|------------|------------|
| google-api-python-client | Cliente oficial da API Google Drive |
| google-auth | Autenticação OAuth 2.0 |

As bibliotecas abaixo são utilizadas pelo programa, porém já fazem parte da instalação padrão do Python:
- configparser
- pathlib
- sys

## Arquivo de configuração
Crie um arquivo `JDGoogleDrive.ini` no mesmo diretório do executável.

Exemplo:

```ini
[GOOGLE]
CLIENT_ID=xxxxxxxxxxxxxxxxxxxxxxxx.apps.googleusercontent.com
CLIENT_SECRET=xxxxxxxxxxxxxxxxxxxxxxxx
REFRESH_TOKEN=1//xxxxxxxxxxxxxxxxxxxxxxxx
```

## Utilização

```bash
GoogleDrive.exe "C:\Arquivos\Relatorio.pdf" "ID_DA_PASTA_GOOGLE"
```

ou

```bash
python GoogleDrive.py "C:\Arquivos\Relatorio.pdf" "ID_DA_PASTA_GOOGLE"
```
