from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import time


options = Options()
options.add_argument("--enable-chrome-browser-cloud-management")

driver = webdriver.Edge(options=options)
driver.maximize_window()
time.sleep(1.0)
wait = WebDriverWait(driver, 12.0)


# Inicialize o driver do Chrome usando o WebDriverManager
#executable_path="C:/Users/david.barros/Documents/chromedriver_win64-125/chromedriver.exe"

#cService=webdriver.ChromeService()
#options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=cService, options=options)

print("------------------------------------------------------")
print("           INICIO DOS TESTES AUTOMATIZADOS            ")
print("------------------------------------------------------")


def check_url():
    try:
        driver.get("http://192.168.45.60:8000/realms/academico/protocol/openid-connect/auth?client_id=clientPainel&redirect_uri=http%3A%2F%2Flocalhost%3A5173%2F&state=3862b5e8-fc67-49fe-8698-54075274eac2&response_mode=fragment&response_type=code&scope=openid&nonce=8576b837-76af-4eff-b17a-d4a73a678e52")
        print("------------------------------------------------------")
        print("     Teste VALIDANDO URL: Sucesso!!!                  ")
        print("------------------------------------------------------")
    except:
        print("------------------------------------------------------")
        print("     Teste VALIDANDO URL: Falha!!!                    ")
        print("------------------------------------------------------")


def insert_datas():
    try:
        digitando_usuario = driver.find_element(By.ID, "username")
        time.sleep(1.5)
        digitando_usuario.send_keys("08136535418")
        time.sleep(1.5)
        digitando_senha = driver.find_element(By.ID, "password")
        time.sleep(1.5)
        digitando_senha.send_keys("123")
        time.sleep(0.5)


        print("------------------------------------------------------")
        print("     Teste USUARIO E SENHA: Sucesso!!!                ")
        print("------------------------------------------------------")
    
    except:
        print("------------------------------------------------------")
        print("     Teste USUARIO E SENHA: Falha!!!                  ")
        print("------------------------------------------------------")


def click_enter():
    try:
        teste_botao = driver.find_element(By.ID, "kc-login")
        time.sleep(1.5)
        teste_botao.click()
        time.sleep(1.5)
        print("------------------------------------------------------")
        print("     Teste LOGIN: Sucesso!!!                          ")
        print("------------------------------------------------------")

    except:
        print("------------------------------------------------------")
        print("     Teste LOGIN: Falha!!!                            ")
        print("------------------------------------------------------")


# Aceitando termos e condições:
def terms_conditions():
    try:
        termos_e_condicoes = driver.find_element(By.CLASS_NAME, "form-check-label")
        time.sleep(1.0)
        termos_e_condicoes.click()
        time.sleep(1.0)

        botao_aceitar_termos = driver.find_element(By.ID, "aceitarTermos")
        time.sleep(1.0)
        botao_aceitar_termos.click()
        time.sleep(1.0)

        print("------------------------------------------------------")
        print("     Teste TERMOS: Sucesso!!!                        ")
        print("------------------------------------------------------")
    except:
        print("------------------------------------------------------")
        print("     Teste TERMOS: Falha!!!                        ")
        print("------------------------------------------------------")


# Barra de rolagem:
def scroll_bar():
    try:
        driver.execute_script("window.scrollTo(0, 550);")
        time.sleep(1.0)
        print("------------------------------------------------------")
        print("     Teste DESCENDO PAGINA: Sucesso!!!                ")
        print("------------------------------------------------------")
    except:
        print("------------------------------------------------------")
        print("     Teste DESCENDO PAGINA: Falha!!!                  ")
        print("------------------------------------------------------")


# Clicando no link FREQUÊNCIA:
def click_frequencia():
    try:
        clicar_frequencia = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[1]/div/div/div[2]/div/div/div[2]/a[1]')
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


# Ordenando em ordem crescente e decrescente: data, horário e local
def order_frequencia():
    try:
        ordenar_data = driver.find_element(By.XPATH, "//*[@id='main']/section/div/div/div/div/div[1]/table/thead/tr/th[1]")
        time.sleep(1.0)                              
        ordenar_data.click() # Filtrar Data
        time.sleep(1.0)
        ordenar_data.click() # Filtrar Data
        time.sleep(1.0)

        ordenar_horario = driver.find_element(By.XPATH, "//*[@id='main']/section/div/div/div/div/div[1]/table/thead/tr/th[2]")
        time.sleep(1.0)
        ordenar_horario.click() # Filtrar Horário
        time.sleep(1.0)
        ordenar_horario.click() # Filtrar Horário
        time.sleep(1.0)

        ordenar_local = driver.find_element(By.XPATH, "//*[@id='main']/section/div/div/div/div/div[1]/table/thead/tr/th[3]")
        time.sleep(1.0)
        ordenar_local.click() # Filtrar Local
        time.sleep(1.0)
        ordenar_local.click() # Filtrar Local
        time.sleep(1.0)

        print("------------------------------------------------------")
        print("     Teste FILTRO DATA, HORA E LOCAL: Sucesso!!!      ")
        print("------------------------------------------------------")
    except:
        print("------------------------------------------------------")
        print("     Teste FILTRO DATA, HORA E LOCAL: Falha!!!        ")
        print("------------------------------------------------------")


# Navegando entre a área frequência:
def validate_frequencia():
    try:
        driver.execute_script("window.scrollTo(0, 400);")
        time.sleep(1.0)
        print("------------------------------------------------------")
        print("     Teste DESCENDO PAGINA: Sucesso!!!                ")
        print("------------------------------------------------------")
    except:
        print("------------------------------------------------------")
        print("     Teste DESCENDO PAGINA: Falha!!!                  ")
        print("------------------------------------------------------")
        

# navegando entre as paginas com as frequencias
def test_pages():
    try:
        escolher_pagina2 = driver.find_element(By.XPATH, "//*[@id='main']/section/div/div/div/div/nav/div/span/button[1]")
        time.sleep(1.0)
        escolher_pagina2.click()
        time.sleep(1.5)

        escolher_pagina3 = driver.find_element(By.XPATH, "//*[@id='main']/section/div/div/div/div/nav/div/span/button[2]")
        time.sleep(1.0)
        escolher_pagina3.click()
        time.sleep(1.5)

        escolher_pagina4 = driver.find_element(By.XPATH, "//*[@id='main']/section/div/div/div/div/nav/div/span/button[3]")
        time.sleep(1.0)
        escolher_pagina4.click()
        time.sleep(1.5)

        escolher_pagina5 = driver.find_element(By.XPATH, "//*[@id='main']/section/div/div/div/div/nav/div/span/button[4]")
        time.sleep(1.0)
        escolher_pagina5.click()
        time.sleep(1.5)

        print("--------------------------------------------------")
        print("      Teste PAGINAÇÃO: Sucesso!!!                 ")
        print("--------------------------------------------------")

    except:
        print("--------------------------------------------------")
        print("      Teste PAGINAÇÃO: Falha!!!                   ")
        print("--------------------------------------------------")


# clicando no menu
def bottom_menu():
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
def click_exit():
    try:
        clicar_sair = driver.find_element(By.LINK_TEXT, "Sair")
        time.sleep(1.5)
        clicar_sair.click()
        time.sleep(1.5)

        print("-----------------------------------------------------")
        print("     Teste CLICAR SAIR: Sucesso!!!                   ")
        print("-----------------------------------------------------")

    except:
        print("-----------------------------------------------------")
        print("     Teste CLICAR SAIR: Falha!!!                     ")
        print("-----------------------------------------------------") 


def main():
    check_url()
    insert_datas()
    click_enter()
    terms_conditions()
    scroll_bar()
    click_frequencia()
    order_frequencia()
    validate_frequencia()
    test_pages()
    bottom_menu()
    click_exit()
    time.sleep(1.5)
    print("------------------------------------------------------")
    print("                  FIM DA AUTOMAÇÃO!!!                 ")
    print("------------------------------------------------------")
    exit()
    input()

main()