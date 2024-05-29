from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import time


options = Options()
options.add_argument("--enable-chrome-browser-cloud-management")

driver = webdriver.Edge(options=options)
driver.maximize_window()
time.sleep(1.0)



print("-------------------------------------------------")
print("        INICIO DOS TESTES AUTOMATIZADOS          ")
print("-------------------------------------------------")


def checkUrl():
    try:
        driver.get("https://sso.fps.edu.br/realms/academico/protocol/openid-connect/auth?client_id=clientPainel&redirect_uri=https%3A%2F%2Fminhafps.fps.edu.br%2F%23%2F&state=b7449b72-e04b-4492-973b-be6316436a43&response_mode=fragment&response_type=code&scope=openid&nonce=a740fa15-f630-4e39-80c3-d28ab85147ad")
        time.sleep(1.5)
        print("-----------------------------------------")
        print("     Teste CHECK URL: Sucesso!!!         ")
        print("-----------------------------------------")
    except:
        print("-----------------------------------------")
        print("     Teste CHECK URL: Falha!!!           ")
        print("-----------------------------------------")


def insertUserpassword():
    try:
        insert_user = driver.find_element(By.ID, "username")
        insert_user.click()
        time.sleep(1.5)
        insert_user.send_keys("03152024003")
        time.sleep(1.5)

        insert_password = driver.find_element(By.ID, "password")
        time.sleep(1.5)
        insert_password.send_keys("123")
        time.sleep(1.5)

        print("-----------------------------------------")
        print("     Teste CPF SENHA: Sucesso!!!         ")
        print("-----------------------------------------")
    except:
        print("-----------------------------------------")
        print("     Teste CPF SENHA: Falha!!!           ")
        print("-----------------------------------------")



def clickEnter():
    try:
        click_bottom_enter = driver.find_element(By.NAME, "login")
        time.sleep(1.5)
        click_bottom_enter.click()
        time.sleep(1.5)
        print("-----------------------------------------")
        print("     Teste LOGIN: Sucesso!!!             ")
        print("-----------------------------------------")
    except:
        print("-----------------------------------------")
        print("     Teste LOGIN: Falha!!!               ")
        print("-----------------------------------------")


def termsConditions():
    try:
        terms_box = driver.find_element(By.CLASS_NAME, "form-check")
        time.sleep(1.5)
        terms_box.click()
        time.sleep(2.0)

        click_accept = driver.find_element(By.ID, "aceitarTermos")
        time.sleep(1.5)
        click_accept.click()
        time.sleep(2.0)
        print("-----------------------------------------")
        print("     Teste TERMOS: Sucesso!!!            ")
        print("-----------------------------------------")
    except:
        print("-----------------------------------------")
        print("     Teste TERMOS: Falha!!!              ")
        print("-----------------------------------------")


def scroll():
    try:
        driver.execute_script(f"window.scrollTo(0, 600)")
        time.sleep(2.0)
        print("-----------------------------------------")
        print("     Teste BARRA DE ROLAGEM: Sucesso!!!  ")
        print("-----------------------------------------")
    except:
        print("-----------------------------------------")
        print("     Teste BARRA DE ROLAGEM: Falha!!!    ")
        print("-----------------------------------------")


#Campo cadastro facial
def link():
    try:
        link = driver.find_element(By.LINK_TEXT, "Cadastro Facial")
        time.sleep(1.5)
        link.click()
        time.sleep(2.0)
        print("-----------------------------------------")
        print("     Teste LINK CADASTRO: Sucesso!!!     ")
        print("-----------------------------------------")
    except:
        print("-----------------------------------------")
        print("     Teste LINK CADASTRO: Falha!!!       ")
        print("-----------------------------------------")


# Area Dados Cadastrais
def numberAndemail():
    try:
        campo_numero = driver.find_element(By.XPATH, "//*[@id=\"updateForm\"]/div[1]/input")
        campo_numero.click()
        time.sleep(1.5)
        campo_numero.clear()
        time.sleep(2.0)
        campo_numero.send_keys("81999999999")
        time.sleep(1.5)
        campo_numero.send_keys(Keys.TAB)

        
        
        campo_email = driver.find_element(By.XPATH, "//*[@id=\"updateForm\"]/div[2]/input")
        campo_email.click()
        time.sleep(1.5)
        campo_email.clear()
        time.sleep(2.0)
        campo_email.send_keys("usuarioteste03@teste.com")
        time.sleep(1.5)
        print("-----------------------------------------")
        print("     Teste NUMERO E EMAIL: Sucesso!!!    ")
        print("-----------------------------------------")

    except:
        print("-----------------------------------------")
        print("     Teste NUMERO E EMAIL: Falha!!!      ")
        print("-----------------------------------------")


# botão Atualizar
def updateBottom():
    try:
        update = driver.find_element(By.XPATH, "//*[@id=\"updateForm\"]/div[3]/button")
        time.sleep(1.0)
        update.click()
        time.sleep(2.5)
        print("-----------------------------------------")
        print("     Teste BOTÃO ATUALIZAR: Sucesso!!!   ")
        print("-----------------------------------------")
    except:
        print("-----------------------------------------")
        print("     Teste BOTÃO ATUALIZAR: Falha!!!     ")
        print("-----------------------------------------")


def bottomNext():
    try:
        click_next = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div[1]/form/div[3]/a[2]")
        time.sleep(1.5)
        click_next.click()
        time.sleep(1.5)

        print("--------------------------------------------------")
        print("     Teste BOTÃO PROXIMO: Sucesso!!!              ")
        print("--------------------------------------------------")
    except:
        print("--------------------------------------------------")
        print("     Teste BOTÃO PROXIMO: Falha!!!                ")
        print("--------------------------------------------------")


# CONTINUAR OS TESTES DEPOIS DAS ATUALIZAÇÕES!!!!!
# CONTINUAR OS TESTES DEPOIS DAS ATUALIZAÇÕES!!!!!
# CONTINUAR OS TESTES DEPOIS DAS ATUALIZAÇÕES!!!!!
# CONTINUAR OS TESTES DEPOIS DAS ATUALIZAÇÕES!!!!!

def back():
    try:
        back_to_home = driver.find_element(By.LINK_TEXT, "Voltar")
        time.sleep(1.5)
        back_to_home.click()
        time.sleep(1.5)

        print("--------------------------------------------------")
        print("     Teste BOTÃO VOLTAR: Sucesso!!!                ")
        print("--------------------------------------------------")
    except:
        print("--------------------------------------------------")
        print("     Teste BOTÃO VOLTAR: Falha!!!                ")
        print("--------------------------------------------------")


def backHome():
    try:
        back_again = driver.find_element(By.XPATH ,"/html/body/div/div/main/div/div/div/div[1]/form/div[3]/a[1]")
        time.sleep(1.5)
        back_again.click()
        time.sleep(1.5)


        print("--------------------------------------------------")
        print("     Teste VOLTAR NOVAMENTE: Sucesso!!!           ")
        print("--------------------------------------------------")
    except:
        print("--------------------------------------------------")
        print("     Teste VOLTAR NOVAMENTE: Falha!!!             ")
        print("--------------------------------------------------")


def bottomExit():
    try:
        bottom_exit = driver.find_element(By.XPATH, "/html/body/div/div/nav/div/div/a")
        time.sleep(1.5)
        bottom_exit.click()
        time.sleep(1.5)

        print("--------------------------------------------------")
        print("     Teste SAIR: Sucesso!!!                       ")
        print("--------------------------------------------------")
    except:
        print("--------------------------------------------------")
        print("     Teste SAIR: Falha!!!                         ")
        print("--------------------------------------------------")

def main():
    checkUrl()
    insertUserpassword()
    clickEnter()
    termsConditions()
    scroll()
    link()
    numberAndemail()
    updateBottom()
    bottomNext()
    back()
    backHome()
    bottomExit()
    time.sleep(2.0)
    driver.quit()
    print("\n")
    print("-------------------------------------------------")
    print("-------------------------------------------------")
    print("               FIM DA AUTOMAÇÃO!!!               ")
    print("-------------------------------------------------")
    print("-------------------------------------------------")
    exit()
    input()

main()
