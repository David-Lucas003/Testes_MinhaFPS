# TESTE: ATUALIZANDO OS DADOS
# NUMERO E EMAIL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Abrindo o Chrome
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

print("-----------------------------------------")
print("     INICIO DOS TESTES AUTOMATIZADOS     ")
print("-----------------------------------------")



# Digitando a URL
def insertUrl():
    try:
        driver.get("https://sso.fps.edu.br/realms/academico/protocol/openid-connect/auth?client_id=clientPainel&redirect_uri=https%3A%2F%2Fminhafps.fps.edu.br%2F&state=36f1fb39-09cc-48bb-8c04-34e6f33fcdac&response_mode=fragment&response_type=code&scope=openid&nonce=c40e00d9-64e4-469b-8b76-f6f58d34faa5")
        time.sleep(1.0)
        print("-----------------------------------------")
        print("       Teste URL: Sucesso!!!             ")
        print("-----------------------------------------")
    except:
        print("-----------------------------------------")
        print("       Teste URL: Falha!!!               ")
        print("-----------------------------------------")



# Digitando cpf e senha
def cpfAndpassword():
    try:

        insert_cpf = driver.find_element(By.ID, "username")
        time.sleep(1.5)
        insert_cpf.click()
        time.sleep(1.5)
        insert_cpf.send_keys("03152024003")
        time.sleep(1.5)
        insert_cpf.send_keys(Keys.TAB)
        
        insert_password = driver.find_element(By.ID, "password")
        time.sleep(1.5)
        insert_password.click()
        time.sleep(1.5)
        insert_password.send_keys("123")
        time.sleep(1.5)

        
        
        print("-----------------------------------------")
        print("       Teste CPF E SENHA: Sucesso!!!     ")
        print("-----------------------------------------")
    except:
        print("-----------------------------------------")
        print("       Teste CPF E SENHA: Falha!!!       ")
        print("-----------------------------------------")



# Clicando em entrar
def enter():
    try:
        bottom_enter = driver.find_element(By.NAME ,"login")
        time.sleep(1.0)
        bottom_enter.click()
        time.sleep(1.0)
        print("-----------------------------------------")
        print("       Teste LOGIN: Sucesso!!!           ")
        print("-----------------------------------------")
    except:
        print("-----------------------------------------")
        print("       Teste LOGIN: Erro no login!!!     ")
        print("-----------------------------------------")



# Termos e Condições
def acceptTerms():
    try:

        terms_box = driver.find_element(By.CLASS_NAME, "form-check")
        terms_box.click()
        time.sleep(1.0)

        click_accept = driver.find_element(By.ID, "aceitarTermos")
        click_accept.click()
        time.sleep(1.0)

        print("-----------------------------------------")
        print("       Teste TERMOS: Sucesso!!!          ")
        print("-----------------------------------------")
    except:
        print("-----------------------------------------")
        print("       Teste TERMOS: Falha!!!            ")
        print("-----------------------------------------")



def scrollScreen():
    try:
        driver.execute_script(f"window.scrollTo(0, 650)")
        time.sleep(1.0)
        print("-----------------------------------------")
        print("       Teste BARRA DE ROLAGEM: Sucesso!!!")
        print("-----------------------------------------")
    except:
        print("-----------------------------------------")
        print("       Teste BARRA DE ROLAGEM: Falha!!!  ")
        print("-----------------------------------------")



#Campo cadastro facial
def clickLink():
    try:
        link_cadastro = driver.find_element(By.LINK_TEXT, "Cadastro Facial")
        time.sleep(1.0)
        link_cadastro.click()
        time.sleep(1.0)
        print("-----------------------------------------")
        print("       Teste LINK CADASTRO: Sucesso!!!   ")
        print("-----------------------------------------")
    except:
        print("-----------------------------------------")
        print("       Teste LINK CADASTRO: Falha!!!     ")
        print("-----------------------------------------")



# Area Dados Cadastrais
def insertnumberEmail():
    try:
        campo_numero = driver.find_element(By.XPATH, "//*[@id=\"updateForm\"]/div[1]/input")
        campo_numero.click()
        time.sleep(1.0)
        campo_numero.clear()
        time.sleep(1.0)
        campo_numero.send_keys("81999999999")
        time.sleep(1.0)
        campo_numero.send_keys(Keys.TAB)

        
        
        campo_email = driver.find_element(By.XPATH, "//*[@id=\"updateForm\"]/div[2]/input")
        campo_email.click()
        time.sleep(1.0)
        campo_email.clear()
        time.sleep(1.0)
        campo_email.send_keys("usuarioteste03@teste.com")
        time.sleep(1.0)
        print("-----------------------------------------")
        print("       Teste NUMERO E EMAIL: Sucesso!!!  ")
        print("-----------------------------------------")

    except:
        print("-----------------------------------------")
        print("       Teste NUMERO E EMAIL: Falha!!!    ")
        print("-----------------------------------------")



# AGUARDANDO ATUALIZAÇÕES PARA NOVOS TESTES :
# ATUALIZAÇÕES DE DADOS (DOCENTE): EMAIL E NÚMERO;
# Botão Atualizar
def updateBottom():
    try:
        update = driver.find_element(By.XPATH, "//*[@id=\"updateForm\"]/div[3]/button")
        time.sleep(1.0)
        update.click()
        time.sleep(2.5)
        print("-----------------------------------------")
        print("       Teste BOTÃO ATUALIZAR: Sucesso!!! ")
        print("-----------------------------------------")
    except:
        print("-----------------------------------------")
        print("       Teste BOTÃO ATUALIZAR: Falha!!!   ")
        print("-----------------------------------------")



# AGUARDANDO ATUALIZAÇÕES PARA NOVOS TESTES :
# ATUALIZAÇÕES DE DADOS (DOCENTE): EMAIL E NÚMERO;
# Clicando no botão MENU:
def bottomMenu():
    try:
        clicar_menu = driver.find_element(By.ID, "pv_id_1_0")
        time.sleep(1.0)
        clicar_menu.click()
        time.sleep(1.0)

        print("-----------------------------------------")
        print("       Teste CLICAR MENU: Sucesso!!!     ")
        print("-----------------------------------------")

    except:
        print("-----------------------------------------")
        print("       Teste CLICAR MENU: Falha!!!       ")
        print("-----------------------------------------")


# Clicando em SAIR:
def clickExit():
    try:
        clicar_sair = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "p-submenu-list")))
        clicar_sair.click()

        print("-----------------------------------------")
        print("       Teste CLICAR SAIR: Sucesso!!!     ")
        print("-----------------------------------------")

    except:
        print("-----------------------------------------")
        print("       Teste CLICAR SAIR: Falha!!!       ")
        print("-----------------------------------------")



def main():
    insertUrl()
    cpfAndpassword()
    enter()
    acceptTerms()
    scrollScreen()
    clickLink()
    insertnumberEmail()
    updateBottom()
    bottomMenu()
    clickExit()
    time.sleep(2.0)
    print("\n")
    print("-----------------------------------------")
    print("-----------------------------------------")
    print("           FIM DA AUTOMAÇÃO!!!           ")
    print("-----------------------------------------")
    print("-----------------------------------------")
    exit()
    input()

main()



