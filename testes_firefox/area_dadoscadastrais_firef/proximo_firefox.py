from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(1.0)


print("------------------------------------------------------------------")
print("                  INICIO DOS TESTES AUTOMATIZADOS                 ")
print("------------------------------------------------------------------")
print("\n")


driver.get("https://sso.fps.edu.br/realms/academico/protocol/openid-connect/auth?client_id=clientPainel&redirect_uri=https%3A%2F%2Fminhafps.fps.edu.br%2F&state=a4ea9f61-61e8-41b6-84ca-ad93f19d7f0e&response_mode=fragment&response_type=code&scope=openid&nonce=b27bf347-9ddc-4978-8c76-9cc0c9b134ef")
time.sleep(1.5)



def cpfandSenha():
    try:
        insert_cpf = driver.find_element(By.ID ,"username")
        time.sleep(1.5)
        insert_cpf.click()
        insert_cpf.send_keys("03152024003")
        time.sleep(1.5)

        insert_password = driver.find_element(By.ID ,"password") 
        time.sleep(1.5)
        insert_password.click()
        insert_password.send_keys("123")
        time.sleep(1.5)

        print("-----------------------------------------------------")
        print("     Teste INSERIR CPF SENHA: Sucesso!!!             ")    
        print("-----------------------------------------------------")
    except:
        print("-----------------------------------------------------")
        print("     Teste INSERIR CPF SENHA: Falha!!!               ")    
        print("-----------------------------------------------------")


def login():
    try:
        login_autenticator = driver.find_element(By.XPATH, "//*[@id=\"kc-login\"]")
        time.sleep(1.5)
        login_autenticator.click()
        time.sleep(1.5)

        print("-----------------------------------------------------")
        print("     Teste LOGIN: Sucesso!!!                         ")    
        print("-----------------------------------------------------")
    except:
        print("-----------------------------------------------------")
        print("     Teste LOGIN: Falha!!!                           ")    
        print("-----------------------------------------------------")



def enterHome():
    try:
        box_terms = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div/div/div[2]/div/label")
        time.sleep(1.5)
        box_terms.click()
        time.sleep(1.5)


        click_accept = driver.find_element(By.ID, "aceitarTermos")
        time.sleep(1.5)
        click_accept.click()
        time.sleep(1.5)


        print("-----------------------------------------------------")
        print("     Teste TERMOS: Sucesso!!!                        ")    
        print("-----------------------------------------------------")
    except:
        print("-----------------------------------------------------")
        print("     Teste TERMOS: Falha!!!                          ")    
        print("-----------------------------------------------------")


def scrollScreen():
    try:
        driver.execute_script(f"window.scrollTo(0, 600)")
        time.sleep(1.5)

        print("-----------------------------------------------------")
        print("     Teste DESCER TELA: Sucesso!!!                   ")
        print("-----------------------------------------------------")
    except:
        print("-----------------------------------------------------")
        print("     Teste DESCER TELA: Falha!!!                     ")
        print("-----------------------------------------------------")


def clickCadastrofacial():
    try:
        link_cadastro = driver.find_element(By.LINK_TEXT, "Cadastro Facial")
        time.sleep(1.5)
        link_cadastro.click()
        time.sleep(1.5)

        print("-----------------------------------------------------")
        print("     Teste LINK CADASTRO: Sucesso!!!                 ")
        print("-----------------------------------------------------")
    except:
        print("-----------------------------------------------------")
        print("     Teste LINK CADASTRO: Falha!!!                   ")
        print("-----------------------------------------------------")


def numberandEmail():
    try:
        insert_number = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div[1]/form/div[1]/input")
        insert_number.click()
        time.sleep(1.5)
        insert_number.clear()
        time.sleep(1.5)
        insert_number.send_keys("81999999999")
        time.sleep(2.0)
        insert_number.send_keys(Keys.TAB)

        insert_email = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div[1]/form/div[2]/input")
        insert_email.click()
        time.sleep(1.5)
        insert_email.clear()
        time.sleep(1.5)
        insert_email.send_keys("usuarioteste03@teste.com")
        time.sleep(2.0)


        print("--------------------------------------------------")
        print("     Teste NUMERO E EMAIL: Sucesso!!!             ")
        print("--------------------------------------------------")
    except:
        print("--------------------------------------------------")
        print("     Teste NUMERO E EMAIL: Falha!!!               ")
        print("--------------------------------------------------")


def bottomUpdate():
    try:
        update = driver.find_element(By.CSS_SELECTOR, "button.btn")
        time.sleep(2.5)
        update.click()
        time.sleep(2.0)


        print("--------------------------------------------------")
        print("     Teste ATUALIZAR: Sucesso!!!                  ")
        print("--------------------------------------------------")
    except:
        print("--------------------------------------------------")
        print("     Teste ATUALIZAR: Falha!!!                    ")
        print("--------------------------------------------------")


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
    cpfandSenha()
    login()
    enterHome()
    scrollScreen()
    clickCadastrofacial()
    numberandEmail()
    bottomUpdate()
    bottomNext()
    back()
    backHome()
    bottomExit()
    time.sleep(2.0)
    driver.quit()
    print("\n")
    print("------------------------------------------------")
    print("------------------------------------------------")
    print("              FIM DA AUTOMAÇÃO!!!               ")
    print("------------------------------------------------")
    print("------------------------------------------------")
    exit()
    input()

main()