from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import time


driver = webdriver.Firefox()
time.sleep(1.0)
driver.maximize_window()

# Inicialize o driver do Chrome usando o WebDriverManager
#executable_path="C:/Users/david.barros/Documents/chromedriver_win64-125/chromedriver.exe"

#cService=webdriver.ChromeService()
#options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=cService, options=options)

print("------------------------------------------------------")
print("           INICIO DOS TESTES AUTOMATIZADOS            ")
print("------------------------------------------------------")

def checkUrl():
    try:
        driver.get("https://sso.fps.edu.br/realms/academico/protocol/openid-connect/auth?client_id=clientPainel&redirect_uri=https%3A%2F%2Fminhafps.fps.edu.br%2F&state=204f708e-f5c4-48c1-8005-211abec45d90&response_mode=fragment&response_type=code&scope=openid&nonce=26f9f433-f988-4b4c-9e67-59e36beacb45")
        print("------------------------------------------------------")
        print("     Teste VALIDANDO URL: Sucesso!!!                  ")
        print("------------------------------------------------------")
    except:
        print("------------------------------------------------------")
        print("     Teste VALIDANDO URL: Falha!!!                    ")
        print("------------------------------------------------------")


def insertDatas():
    try:
        digitando_usuario = driver.find_element(By.ID, "username")
        time.sleep(1.5)
        digitando_usuario.click()
        time.sleep(1.5)
        digitando_usuario.send_keys("03152024003")
        time.sleep(1.5)

        digitando_senha = driver.find_element(By.ID, "password")
        time.sleep(1.5)
        digitando_senha.click()
        time.sleep(1.5)
        digitando_senha.send_keys("123")
        time.sleep(1.5)


        print("-----------------------------------------------------")
        print("     Teste DIGITAR USUARIO E SENHA: SUCESSO!!!       ")
        print("-----------------------------------------------------")
    
    except:
        print("-----------------------------------------------------")
        print("     Teste DIGITAR USUARIO E SENHA: FALHA!!!         ")
        print("-----------------------------------------------------")



def clickSignin():
    try:
        teste_botao = driver.find_element(By.ID, "kc-login")
        time.sleep(1.5)
        teste_botao.click()
        time.sleep(1.5)
        print("------------------------------------------------------")
        print("     Teste BOTÃO: Sucesso!!!                          ")
        print("------------------------------------------------------")

    except:
        print("------------------------------------------------------")
        print("     Teste BOTÃO: Falha!!!                            ")
        print("------------------------------------------------------")


# Aceitando termos e condições:
def termsAndconditions():
    try:
        termos_e_condicoes = driver.find_element(By.CLASS_NAME, "form-check-label")
        time.sleep(1.5)
        termos_e_condicoes.click()
        time.sleep(1.5)

        botao_aceitar_termos = driver.find_element(By.ID, "aceitarTermos")
        time.sleep(1.5)
        botao_aceitar_termos.click()
        time.sleep(1.5)

        print("------------------------------------------------------")
        print("     Teste TERMOS: Sucesso!!!                        ")
        print("------------------------------------------------------")
    except:
        print("------------------------------------------------------")
        print("     Teste TERMOS: Falha!!!                        ")
        print("------------------------------------------------------")


# Barra de rolagem:
def scrollBar():
    try:
        driver.execute_script("window.scrollTo(0, 850);")
        time.sleep(1.5)
        print("------------------------------------------------------")
        print("     Teste DESCENDO PAGINA: Sucesso!!!                ")
        print("------------------------------------------------------")
    except:
        print("------------------------------------------------------")
        print("     Teste DESCENDO PAGINA: Falha!!!                  ")
        print("------------------------------------------------------")


# Clicando no link FREQUÊNCIA:
def clickinFrequencia():
    try:
        clicar_frequencia = driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/section[1]/div/div/div[2]/div/div/div[2]/a")
        time.sleep(1.0)
        clicar_frequencia.click()
        time.sleep(1.0)
        print("------------------------------------------------------")
        print("     Teste CLICAR FREQUÊNCIA: Sucesso!!!              ")
        print("------------------------------------------------------")
    except:
        print("------------------------------------------------------")
        print("     Teste CLICAR FREQUÊNCIA: Falha!!!                ")
        print("------------------------------------------------------")


def orderFrequencia():
    try:
        ordenar_data = driver.find_element(By.XPATH, '//*[@id="main"]/section/div/div/div/div/div[1]/table/thead/tr/th[1]/div')
        time.sleep(1.5)
        ordenar_data.click() # Clicar para filtra na ordem decrescente
        time.sleep(1.5)
        ordenar_data.click() # Clicar para filtra na ordem crescente
        time.sleep(1.5)

        ordenar_horario = driver.find_element(By.XPATH, '//*[@id="main"]/section/div/div/div/div/div[1]/table/thead/tr/th[2]/div')
        time.sleep(1.5)
        ordenar_horario.click() # Clicar para filtra na ordem decrescente
        time.sleep(1.5)
        ordenar_horario.click() # Clicar para filtra na ordem crescente
        time.sleep(1.5)

        ordenar_local = driver.find_element(By.XPATH, '//*[@id="main"]/section/div/div/div/div/div[1]/table/thead/tr/th[3]/div')
        time.sleep(1.5)
        ordenar_local.click() # Clicar para filtra na ordem decrescente
        time.sleep(1.5)
        ordenar_local.click() # Clicar para filtra na ordem crescente
        time.sleep(1.5)

        print("------------------------------------------------------")
        print("     Teste FILTRO DATA, HORA E LOCAL: Sucesso!!!      ")
        print("------------------------------------------------------")
    except:
        print("------------------------------------------------------")
        print("     Teste FILTRO DATA, HORA E LOCAL: Falha!!!        ")
        print("------------------------------------------------------")


# Navegando entre a área frequência:
def validatetheFrequencia():
    try:
        driver.execute_script("window.scrollTo(0, 650);")
        time.sleep(1.5)
        print("------------------------------------------------------")
        print("     Teste DESCENDO PAGINA: Sucesso!!!                ")
        print("------------------------------------------------------")
    except:
        print("------------------------------------------------------")
        print("     Teste DESCENDO PAGINA: Falha!!!                  ")
        print("------------------------------------------------------")
        

# Clicando no botão MENU:
def bottomMenu():
    try:
        clicar_menu = driver.find_element(By.ID, "pv_id_1_0")
        time.sleep(1.0)
        clicar_menu.click()
        time.sleep(1.0)

        print("------------------------------------------------------")
        print("     Teste CLICAR MENU: Sucesso!!!                    ")
        print("------------------------------------------------------")

    except:
        print("------------------------------------------------------")
        print("     Teste CLICAR MENU: Falha!!!                      ")
        print("------------------------------------------------------")        


# Clicando em SAIR:
def clickExit():
    try:
        clicar_sair = driver.find_element(By.CLASS_NAME, "p-submenu-list")
        time.sleep(1.0)
        clicar_sair.click()
        time.sleep(1.0)

        print("------------------------------------------------------")
        print("     Teste CLICAR SAIR: Sucesso!!!                   ")
        print("------------------------------------------------------")

    except:
        print("------------------------------------------------------")
        print("     Teste CLICAR SAIR: Falha!!!                      ")
        print("------------------------------------------------------") 


def main():
    checkUrl()
    insertDatas()
    clickSignin()
    termsAndconditions()
    scrollBar()
    clickinFrequencia()
    orderFrequencia()
    validatetheFrequencia()
    bottomMenu()
    clickExit()
    time.sleep(1.5)
    print("-----------------------------------------------------")
    print("                 FIM DA AUTOMAÇÃO!!!                 ")
    print("-----------------------------------------------------")
    exit()
    input()

main()

