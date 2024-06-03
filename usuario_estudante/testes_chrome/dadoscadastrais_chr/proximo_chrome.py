# TESTE: REALIZANDO ATÉ A TELA ANTERIOR A DA CAPTURA DE FOTO
# POIS A AUTOMAÇÃO NÃO É CAPAZ DE EXECUTAR ESTA FUNÇÃO ESPECIFICA

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time


# Abrindo o Chrome
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2.0)


print("---------------------------------------------------------")
print("           INICIO DOS TESTES AUTOMATIZADOS               ")
print("---------------------------------------------------------")


# Digitando a URL
def validateUrl():
    try:
        driver.get("https://sso.fps.edu.br/realms/academico/protocol/openid-connect/auth?client_id=clientPainel&redirect_uri=https%3A%2F%2Fminhafps.fps.edu.br%2F&state=36f1fb39-09cc-48bb-8c04-34e6f33fcdac&response_mode=fragment&response_type=code&scope=openid&nonce=c40e00d9-64e4-469b-8b76-f6f58d34faa5")
        time.sleep(2.0)
        print("-------------------------------------------------------")
        print("     Teste VALIDAR URL: Sucesso!!!                     ")
        print("-------------------------------------------------------")

    except:
        print("-------------------------------------------------------")
        print("     Teste VALIDAR URL: Falha - URL não encontrada     ")
        print("-------------------------------------------------------")


# Digitando cpf e senha
def userandpassword():
    try:
        digitar_cpf = driver.find_element(By.ID, "username")
        digitar_cpf.click()
        time.sleep(1.0)
    
        digitar_cpf.send_keys("03152024003")
        digitar_cpf.send_keys(Keys.TAB)
        time.sleep(1.5)

        digitar_senha = driver.find_element(By.ID, "password")
        digitar_senha.click()
        time.sleep(1.0)

        digitar_senha.send_keys("123")
        time.sleep(1.5)
        print("-------------------------------------------------------")
        print("     Teste USUARIO E SENHA: SUCESSO!!!                 ")
        print("-------------------------------------------------------")

    except: 
        print("-------------------------------------------------------")
        print("     Teste USUARIO E SENHA: Falha!!!                   ")
        print("-------------------------------------------------------")


# Clicando em entrar
def enterHomepage():
    try:        
        clicar_botao_entrar = driver.find_element(By.NAME ,"login")
        time.sleep(1.5)
        clicar_botao_entrar.click()
        time.sleep(1.5)
        print("------------------------------------------------------")
        print("     Teste ENTRAR: Sucesso!!!                         ")
        print("------------------------------------------------------")
    except:
        print("------------------------------------------------------")
        print("     Teste ENTRAR: FALHA!!!                           ")
        print("------------------------------------------------------")


# Termos e Condições
def acceptTerms():
    try:
        caixa_termo = driver.find_element(By.CLASS_NAME, "form-check")
        time.sleep(1.0)
        caixa_termo.click()
        time.sleep(1.0)

        clicar_aceitar = driver.find_element(By.ID, "aceitarTermos")
        time.sleep(1.0)
        clicar_aceitar.click()
        time.sleep(1.0)
        print("------------------------------------------------------")
        print("     Teste TERMOS: Sucesso!!!                         ")
        print("------------------------------------------------------")
    except:
        print("------------------------------------------------------")
        print("     Teste TERMOS: Falha!!!                           ")
        print("------------------------------------------------------")


# 
def screenScroll():
    try:
        driver.execute_script(f"window.scrollTo(0, 600)")
        time.sleep(1.5)
        print("------------------------------------------------------")
        print("     Teste ROLAGEM DE PÁGINA: Sucesso!!!              ")
        print("------------------------------------------------------")
    except:
        print("------------------------------------------------------")
        print("     Teste ROLAGEM DE PÁGINA: Falha!!!                ")
        print("------------------------------------------------------")


# Campo cadastro facial
def linkCad():
    try:
        link_cadastro_facial = driver.find_element(By.LINK_TEXT, "Cadastro Facial")
        time.sleep(2.5)
        link_cadastro_facial.click()
        time.sleep(2.5)
        print("------------------------------------------------------")
        print("     Teste LINKCAD: Sucesso!!!                        ")
        print("------------------------------------------------------")

    except:
        print("------------------------------------------------------")
        print("     Teste LINKCAD: Falha!!!                          ")
        print("------------------------------------------------------")


# Area Dados Cadastrais
# Botão Atualizar
def updateData():
    try:
        botao_atualizar = driver.find_element(By.XPATH, "//*[@id=\"updateForm\"]/div[3]/button")
        time.sleep(2.0)
        botao_atualizar.click()
        time.sleep(2.0)
        print("------------------------------------------------------")
        print("     Teste ATUALIZAR DADOS: Sucesso!!!                ")
        print("------------------------------------------------------")

    except:
        print("------------------------------------------------------")
        print("     Teste ATUALIZAR DADOS: Falha!!!                  ")
        print("------------------------------------------------------")


# Botão Proximo
def clickNext():
    try:
        botao_proximo = driver.find_element(By.LINK_TEXT, "Próximo")
        time.sleep(2.0)
        botao_proximo.click()
        time.sleep(2.0)

        proximo_novamente = driver.find_element(By.LINK_TEXT, "Próximo")
        time.sleep(1.5)
        proximo_novamente.click()
        time.sleep(1.5)
        print("------------------------------------------------------")
        print("     Teste CLICAR PROXIMO: Sucesso!!!                 ")
        print("------------------------------------------------------")
    except:
        print("------------------------------------------------------")
        print("     Teste CLICAR PROXIMO: Falha!!!                   ")
        print("------------------------------------------------------")


# CONTINUAR OS TESTES DEPOIS DAS ATUALIZAÇÕES!!!!!
# CONTINUAR OS TESTES DEPOIS DAS ATUALIZAÇÕES!!!!!
# CONTINUAR OS TESTES DEPOIS DAS ATUALIZAÇÕES!!!!!
# CONTINUAR OS TESTES DEPOIS DAS ATUALIZAÇÕES!!!!!


def backUpdate():
    try:
        voltar_atualizar = driver.find_element(By.XPATH, "//*[@id=\"main\"]/section/div/div/div[1]/div/a[1]")
        time.sleep(1.5)
        voltar_atualizar.click()
        time.sleep(1.5)

        voltar_atualizar_novamente = driver.find_element(By.XPATH, "//*[@id=\"main\"]/section/div/div/div[1]/div/a[1]")
        time.sleep(1.5)
        voltar_atualizar_novamente.click()
        time.sleep(1.5)
    except:
        print("------------------------------------------------------")
        print("     Teste CLICAR VOLTAR HOME: Falha!!!               ")
        print("------------------------------------------------------")


# AGUARDANDO ATUALIZAÇÔES PARA NOVOS TESTES:
# VISUALIZAÇÃO DA FOTO NO CADASTRO FACIAL
# ALÉM DA FOTO, INFORMAÇÔES COMO DATA E HORA EXATA DO CADASTRO


def backHomepage():
    try:
        voltar_home = driver.find_element(By.XPATH, "//*[@id=\"updateForm\"]/div[3]/a[1]")
        time.sleep(1.5)
        voltar_home.click()
        time.sleep(1.5)

        print("------------------------------------------------------")
        print("     Teste VOLTAR HOME: Sucesso!!!                    ")
        print("------------------------------------------------------")

    except: 
        print("------------------------------------------------------")
        print("     Teste VOLTAR HOME: Falha!!!                      ")
        print("------------------------------------------------------")


# AGUARDANDO ATUALIZAÇÔES PARA NOVOS TESTES:
# VISUALIZAÇÃO DA FOTO NO CADASTRO FACIAL
# ALÉM DA FOTO, INFORMAÇÔES COMO DATA E HORA EXATA DO CADASTRO


def bottomExit():
    try:
        clicar_sair = driver.find_element(By.LINK_TEXT,"Sair")
        time.sleep(3.0)
        clicar_sair.click()
        time.sleep(3.0)
        print("------------------------------------------------------")
        print("     Teste SAIR: Sucesso!!!                           ")
        print("------------------------------------------------------")

    except:
        print("------------------------------------------------------")
        print("     Teste SAIR: Falha!!!                             ")
        print("------------------------------------------------------")

 
# AGUARDANDO ATUALIZAÇÔES PARA NOVOS TESTES:
# VISUALIZAÇÃO DA FOTO NO CADASTRO FACIAL
# ALÉM DA FOTO, INFORMAÇÔES COMO DATA E HORA EXATA DO CADASTRO


def main():
    validateUrl()
    userandpassword()
    enterHomepage()
    acceptTerms()
    screenScroll()
    linkCad()
    updateData()
    clickNext()
    backUpdate()
    backHomepage()
    #bottomExit()
    time.sleep(2.0)
    driver.quit()
    print("\n")
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("                   FIM DA AUTOMAÇÃO!!!                   ")
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    
    input()

main()

