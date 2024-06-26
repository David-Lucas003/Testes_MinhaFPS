# Inicialize o driver do Chrome usando o WebDriverManager
#executable_path="C:/Users/david.barros/Documents/chromedriver_win64-125/chromedriver.exe"
#cService=webdriver.ChromeService()
#options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=cService, options=options)
# Comandos para o funcionamento do automatizador


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)


print("--------------------------------------------------")
print("          INICIO DOS TESTES AUTOMATIZADOS        ")
print("--------------------------------------------------")


# Validar sucesso na URL:
def waitUrl():
    try:
        driver.get("https://sso.fps.edu.br/realms/academico/protocol/openid-connect/auth?client_id=clientPainel&redirect_uri=https%3A%2F%2Fminhafps.fps.edu.br%2F&state=af0711d7-d894-44ca-8544-cda12249c31b&response_mode=fragment&response_type=code&scope=openid&nonce=1b553755-be39-4af9-844c-ac5c84f32ca6")
        print("-------------------------------------------------")
        print("       Teste ESPERA URL: Sucesso!!!              ")
        print("-------------------------------------------------")
    except:
        print("-------------------------------------------------")
        print("       Teste ESPERA URL: Falha!!!                ")
        print("-------------------------------------------------")


# Digitando usuário e senha:
def datas():
    try:
        campo_cpf = driver.find_element(By.ID, "username")
        time.sleep(1.5)
        campo_cpf.send_keys("03152024003")
        time.sleep(1.5)
        campo_senha = driver.find_element(By.ID, "password")
        time.sleep(1.5)
        campo_senha.send_keys("123")

        print("--------------------------------------------------")
        print("       Teste DIGITAR DADOS: Sucesso!!!            ")
        print("--------------------------------------------------")

    except:
        print("--------------------------------------------------")
        print("       Teste DIGITAR DADOS: Falha!!!              ")
        print("--------------------------------------------------")


# Clicando em entrar:
def clickEnter():
    try:
        teste_botao = driver.find_element(By.ID, "kc-login")
        time.sleep(1.0)
        teste_botao.click()
        time.sleep(1.0)

        print("--------------------------------------------------")
        print("       Teste CLICAR BOTÃO LOGIN: Sucesso!!!       ")
        print("--------------------------------------------------")

    except:
        print("--------------------------------------------------")
        print("       Teste CLICAR BOTÃO LOGIN: Falha!!!         ")
        print("--------------------------------------------------")


# Aceitando termos e condições:
def termsConditions():
    try:
        termos_e_condicoes = driver.find_element(By.CLASS_NAME, "form-check-label")
        time.sleep(1.0)
        termos_e_condicoes.click()
        time.sleep(1.0)

        botao_aceitar_termos = driver.find_element(By.ID, "aceitarTermos")
        time.sleep(1.0)
        botao_aceitar_termos.click()
        time.sleep(1.0)

        print("--------------------------------------------------")
        print("       Teste TERMOS: Sucesso!!!                   ")
        print("--------------------------------------------------")
    except:
        print("--------------------------------------------------")
        print("       Teste TERMOS: Falha!!!                     ")
        print("--------------------------------------------------")


# Barra de rolagem:
def scrollBar():
    try:
        driver.execute_script("window.scrollTo(0, 550);")
        time.sleep(1.0)
        print("--------------------------------------------------")
        print("       Teste DESCENDO PAGINA: Sucesso!!!          ")
        print("--------------------------------------------------")
    except:
        print("--------------------------------------------------")
        print("       Teste DESCENDO PAGINA: Falha!!!            ")
        print("--------------------------------------------------")


# Clicando no link FREQUÊNCIA:
def clickFrequencia():
    try:
        clicar_frequencia = driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/section[1]/div/div/div[2]/div/div/div[2]/a")
        time.sleep(1.0)
        clicar_frequencia.click()
        time.sleep(1.0)
        print("--------------------------------------------------")
        print("       Teste CLICAR FREQUÊNCIA: Sucesso!!!        ")
        print("--------------------------------------------------")
    except:
        print("--------------------------------------------------")
        print("       Teste CLICAR FREQUÊNCIA: Falha!!!          ")
        print("--------------------------------------------------")


# Ordenando em ordem crescente e decrescente: data, horario e local
def orderFrequencia():
    try:
        ordenar_data = driver.find_element(By.XPATH, '//*[@id="main"]/section/div/div/div/div/div[1]/table/thead/tr/th[1]/div')
        time.sleep(1.0)
        ordenar_data.click() # Filtrar Data
        time.sleep(1.0)
        ordenar_data.click() # Filtrar Data
        time.sleep(1.0)

        ordenar_horario = driver.find_element(By.XPATH, '//*[@id="main"]/section/div/div/div/div/div[1]/table/thead/tr/th[2]/div')
        time.sleep(1.0)
        ordenar_horario.click() # Filtrar Horario
        time.sleep(1.0)
        ordenar_horario.click() # Filtrar Horario
        time.sleep(1.0)

        ordenar_local = driver.find_element(By.XPATH, '//*[@id="main"]/section/div/div/div/div/div[1]/table/thead/tr/th[3]/div')
        time.sleep(1.0)
        ordenar_local.click() # Filtrar Local
        time.sleep(1.0)
        ordenar_local.click() # Filtrar Local
        time.sleep(1.0)

        print("--------------------------------------------------")
        print("       Teste FILTRO DATA, HORA E LOCAL: Sucesso!!!")
        print("--------------------------------------------------")
    except:
        print("--------------------------------------------------")
        print("       Teste FILTRO DATA, HORA E LOCAL: Falha!!!  ")
        print("--------------------------------------------------")


# Navegando entre a área frequência:
def navegateFrequencia():
    try:
        driver.execute_script("window.scrollTo(0, 1300);")
        time.sleep(1.5)
        print("--------------------------------------------------")
        print("       Teste DESCENDO PAGINA: Sucesso!!!          ")
        print("--------------------------------------------------")
    except:
        print("--------------------------------------------------")
        print("       Teste DESCENDO PAGINA: Falha!!!            ")
        print("--------------------------------------------------")


# Clicando no botão MENU:
def bottomMenu():
    try:
        clicar_menu = driver.find_element(By.ID, "pv_id_1_0")
        time.sleep(1.5)
        clicar_menu.click()
        time.sleep(1.5)

        print("--------------------------------------------------")
        print("       Teste CLICAR MENU: Sucesso!!!              ")
        print("--------------------------------------------------")

    except:
        print("--------------------------------------------------")
        print("       Teste CLICAR MENU: Falha!!!                ")
        print("--------------------------------------------------")


# Clicando em SAIR:
def clickExit():
    try:
        clicar_sair = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "p-submenu-list")))
        clicar_sair.click()

        print("---------------------------------------------------")
        print("       Teste CLICAR SAIR: Sucesso!!!               ")
        print("---------------------------------------------------")

    except:
        print("---------------------------------------------------")
        print("       Teste CLICAR SAIR: Falha!!!                 ")
        print("---------------------------------------------------")


def main():

    waitUrl()
    datas()
    clickEnter()
    termsConditions()
    scrollBar()
    clickFrequencia()
    orderFrequencia()
    #validateFrequencia()
    navegateFrequencia()
    bottomMenu()
    clickExit()
    time.sleep(1.5)
    print("---------------------------------------------------")
    print("               FIM DA AUTOMAÇÃO!!!                 ")
    print("---------------------------------------------------")
    exit()
    input()

main()