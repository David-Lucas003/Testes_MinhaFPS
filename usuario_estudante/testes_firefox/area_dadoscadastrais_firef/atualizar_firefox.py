from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Firefox()
driver.maximize_window()
wait = WebDriverWait(driver, 12.0)


print("----------------------------------------------------")
print("          INICIO DOS TESTES AUTOMATIZADOS           ")
print("----------------------------------------------------")

# Digitando a URL
def insertUrl():
    try:
        driver.get("https://sso.fps.edu.br/realms/academico/protocol/openid-connect/auth?client_id=clientPainel&redirect_uri=https%3A%2F%2Fminhafps.fps.edu.br%2F&state=36f1fb39-09cc-48bb-8c04-34e6f33fcdac&response_mode=fragment&response_type=code&scope=openid&nonce=c40e00d9-64e4-469b-8b76-f6f58d34faa5")
        time.sleep(1.0)
        print("----------------------------------------------------")
        print("       Teste URL: Sucesso!!!                        ")
        print("----------------------------------------------------")
    except:
        print("----------------------------------------------------")
        print("       Teste URL: Falha!!!                          ")
        print("----------------------------------------------------")


def insertcpfAndsenha():
    try:
        digitar_cpf = driver.find_element(By.XPATH, "//*[@id=\"username\"]")
        time.sleep(1.5)
        digitar_cpf.send_keys("03152024003")
        time.sleep(1.5)
        digitar_cpf.send_keys(Keys.TAB)
        digitar_senha = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
        time.sleep(1.5)
        digitar_senha.send_keys("123")
        time.sleep(1.5)
        print("----------------------------------------------------")
        print("       Teste CPF SENHA: Sucesso!!!                  ")
        print("----------------------------------------------------")
    except:
        print("----------------------------------------------------")
        print("       Teste CPF SENHA: Falha!!!                    ")
        print("----------------------------------------------------")


def enter():
    try:
        click_enter = driver.find_element(By.NAME, "login")
        time.sleep(1.0)
        click_enter.click()
        time.sleep(1.0)

        print("----------------------------------------------------")
        print("       Teste BOTÃO ENTRAR: Sucesso!!!               ")
        print("----------------------------------------------------")
    except:
        print("----------------------------------------------------")
        print("       Teste BOTÃO ENTRAR: Falha!!!                 ")
        print("----------------------------------------------------")



def termsandConditions():
    try:
        clicar_termos = driver.find_element(By.CLASS_NAME, "form-check-label")
        time.sleep(1.0)
        clicar_termos.click()
        time.sleep(1.0)

        clicar_novamente = driver.find_element(By.ID, "aceitarTermos")
        time.sleep(1.0)
        clicar_novamente.click()
        time.sleep(1.0)

        print("----------------------------------------------------")
        print("       Teste TERMOS: Sucesso!!!                     ")
        print("----------------------------------------------------")

    except:
        print("----------------------------------------------------")
        print("       Teste TERMOS: Falha!!!                       ")
        print("----------------------------------------------------")


def scrollSceen():
    try:
        driver.execute_script(f"window.scrollTo(0, 600)")
        time.sleep(1.0)
        print("----------------------------------------------------")
        print("       Teste DESCER TELA: Sucesso!!!                ")
        print("----------------------------------------------------")
    except:
        print("----------------------------------------------------")
        print("       Teste DESCER TELA: Falha!!!                  ")
        print("----------------------------------------------------")


def linkCadastro():
    try:
        clicar_cadastro = driver.find_element(By.LINK_TEXT, "Cadastro Facial")
        time.sleep(2.0)
        clicar_cadastro.click()
        time.sleep(2.0)


        print("----------------------------------------------------")
        print("       Teste LINK CADASTRO: Sucesso!!!              ")
        print("----------------------------------------------------")
    except:
        print("----------------------------------------------------")
        print("       Teste LINK CADASTRO: Falha!!!                ")
        print("----------------------------------------------------")


def numberandEmail():
    try:
        campo_numero = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div[1]/form/div[1]/input")
        campo_numero.click()
        time.sleep(1.0)
        campo_numero.clear()
        time.sleep(1.0)

        digitando_numero = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div[1]/form/div[1]/input")
        digitando_numero.send_keys("81999999999")
        time.sleep(1.0)
        digitando_numero.send_keys(Keys.TAB)

        campo_email = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div[1]/form/div[2]/input")
        campo_email.click()
        time.sleep(1.0)
        campo_email.clear()
        time.sleep(1.0)
        campo_email.send_keys("usuarioteste03@teste.com")
        time.sleep(1.5)
        print("----------------------------------------------------")
        print("       Teste NUMERO E EMAIL: Sucesso!!!             ")
        print("----------------------------------------------------")
    except:
        print("----------------------------------------------------")
        print("       Teste NUMERO E EMAIL: Falha!!!               ")
        print("----------------------------------------------------")


def update():
    try:
        bottom_update = driver.find_element(By.CSS_SELECTOR, "button.btn")
        time.sleep(1.5)
        bottom_update.click()
        time.sleep(1.5)
        print("----------------------------------------------------")
        print("       Teste ATUALIZAR: Sucesso!!!                  ")
        print("----------------------------------------------------")
    except:
        print("----------------------------------------------------")
        print("       Teste ATUALIZAR: Falha!!!                    ")
        print("----------------------------------------------------")



def bottomMenu():
    try:
        clicar_menu = driver.find_element(By.ID, "pv_id_1_0")
        time.sleep(1.5)
        clicar_menu.click()
        time.sleep(1.5)

        print("----------------------------------------------")
        print("       Teste CLICAR MENU: Sucesso!!!          ")
        print("----------------------------------------------")

    except:
        print("----------------------------------------------")
        print("       Teste CLICAR MENU: Falha!!!            ")
        print("----------------------------------------------")


def clickExit():
    try:
        clicar_sair = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "p-submenu-list")))
        clicar_sair.click()

        print("----------------------------------------------")
        print("       Teste CLICAR SAIR: Sucesso!!!          ")
        print("----------------------------------------------")

    except:
        print("----------------------------------------------")
        print("       Teste CLICAR SAIR: Falha!!!            ")
        print("----------------------------------------------")




def main():
    insertUrl()
    insertcpfAndsenha()
    enter()
    termsandConditions()
    scrollSceen()
    linkCadastro()
    numberandEmail()
    update()
    bottomMenu()
    clickExit()
    time.sleep(2.0)
    driver.quit()
    print("\n")
    print("----------------------------------------------------")
    print("----------------------------------------------------")
    print("                FIM DA AUTOMAÇÃO!!!                 ")
    print("----------------------------------------------------")
    print("----------------------------------------------------")
    exit()
    input()

main()
