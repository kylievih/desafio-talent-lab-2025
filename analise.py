import zipfile
import os

zip_path = r"C:\Users\Netgi\Desktop\ProjetoX\Desafio Bemol\Brazilian E-Commerce Public Dataset by Olist.zip"
extract_path = r"C:\Users\Netgi\Desktop\ProjetoX\Desafio Bemol\Brazilian E-Commerce Public Dataset by Olist"

os.makedirs(extract_path, exist_ok=True)

try:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print(f"✅ Banco de dados extraído para: {extract_path}")
    
    print("\n📁 --- Conteúdo da pasta extraída ---")
    conteudo_da_pasta = os.listdir(extract_path)
    if conteudo_da_pasta:
        for item in conteudo_da_pasta:
            print("📄", item)
    else:
        print(f"A pasta '{extract_path}' está vazia ou não contém arquivos visíveis.")
    print("-----------------------------------")

    subpasta_path = os.path.join(extract_path, "Brazilian E-Commerce Public Dataset by Olist")

    print("\n📂 --- Conteúdo REAL da subpasta com os arquivos CSV ---")
    if os.path.exists(subpasta_path):
        arquivos_csv = os.listdir(subpasta_path)
        if arquivos_csv:
            for arquivo in arquivos_csv:
                print("🧾", arquivo)
        else:
            print(f"A subpasta '{subpasta_path}' está vazia.")
    else:
        print(f"A subpasta '{subpasta_path}' não foi encontrada.")
    print("-----------------------------------")

except FileNotFoundError:
    print(f"❌ Erro: O arquivo ZIP não foi encontrado em '{zip_path}'. Verifique se o nome e o caminho estão corretos.")
except zipfile.BadZipFile:
    print(f"❌ Erro: O arquivo '{zip_path}' não é um ZIP válido ou está corrompido.")
except Exception as e:
    print(f"⚠️ Ocorreu um erro inesperado durante a extração: {e}")
