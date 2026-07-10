from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError
from pathlib import Path
import configparser, sys

def carregar_informacoes():
    caminho_ini = Path(__file__).with_name("JDGoogleDrive.ini")
    if not caminho_ini.exists():
        raise ValueError(f"Arquivo de configuração não encontrado: {caminho_ini}")        

    config = configparser.ConfigParser()
    if not config.read(caminho_ini, encoding="utf-8"):
        raise ValueError(f"Não foi possível ler o arquivo de configuração: {caminho_ini}")        

    if "GOOGLE" not in config:
        raise ValueError("Seção [GOOGLE] não encontrada no arquivo de configuração.")
        
    campos_obrigatorios = [
        "CLIENT_ID",
        "CLIENT_SECRET",
        "REFRESH_TOKEN"
    ]

    array_configuracoes = {}
    for campo in campos_obrigatorios:
        valor = config["GOOGLE"].get(campo, "").strip()
        if not valor:
            raise ValueError(f"O parâmetro '{campo}' não foi informado no arquivo de configurações.") 
        array_configuracoes[campo] = valor
    
    return array_configuracoes

def validar_parametros():
    #Validando o número máximo de parâmetros necessários para execução da função.
    if len(sys.argv) != 3:
        raise ValueError(
            "Este programa precisa de 02 parâmetros para execução! \n" 
            "Parâmetro 01: Arquivo para Upload \n" 
            "Parâmetro 02: Pasta do google drive.")      

    arquivo = Path(sys.argv[1])
    if not arquivo.exists():
        raise FileNotFoundError(f"Arquivo não encontrado para envio ao google drive. Arquivo: {arquivo}")

    if not arquivo.is_file():
        raise ValueError(f"O caminho informado não é um arquivo: {arquivo}")
    
    if not arquivo.stat().st_size:
        raise ValueError(f"O arquivo está vazio: {arquivo}")
    
    pasta = sys.argv[2].strip()
    if not pasta:
        raise ValueError(f"O ID da pasta do google drive está inválido. ID: {pasta}")
    
    return arquivo, pasta
    
def conectar_google_drive(config):
    
    credencial = Credentials(
        None,
        refresh_token=config["REFRESH_TOKEN"],
        token_uri="https://oauth2.googleapis.com/token",
        client_id=config["CLIENT_ID"],
        client_secret=config["CLIENT_SECRET"]
    )
    
    return build("drive", "v3", credentials=credencial)
        
def enviar_arquivo(conexao, arquivo, pasta):
    
    dados_do_arquivo = {
        "name": arquivo.name,
        "parents": [pasta]
    }

    midia = MediaFileUpload(str(arquivo), resumable=False)

    retorno = conexao.files().create(
        body=dados_do_arquivo,
        media_body=midia,
        fields="id,name"
    ).execute()

    return retorno

def main():
    
    configuracoes = carregar_informacoes()

    arquivo, pasta = validar_parametros()

    conexao = conectar_google_drive(configuracoes)

    upload = enviar_arquivo(conexao, arquivo, pasta)

    print(upload["id"])
    
if __name__ == "__main__":
    
    try:
        main()
        sys.exit(0)

    except HttpError as e:
        print(f"Erro do Google Drive ({e.status_code}): {e.reason}")
        sys.exit(30)

    except Exception as e:
        print(str(e))
        sys.exit(99)