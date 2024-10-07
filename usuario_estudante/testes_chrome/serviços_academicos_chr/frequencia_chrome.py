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
print("          INICIO DOS TESTES AUTOMATIZADOS         ")
print("--------------------------------------------------")


# Validar sucesso na URL:
def wait_url():
    try:
        driver.get("https://minhafps.fps.edu.br/")
        print("-------------------------------------------------")
        print("       Teste ESPERA URL: Sucesso!!!              ")
        print("-------------------------------------------------")
    except:
        print("-------------------------------------------------")
        print("       Teste ESPERA URL: Falha!!!                ")
        print("-------------------------------------------------")


# Digitando usuário e senha:
def user_password():
    try:
        campo_cpf = driver.find_element(By.ID, "username")
        time.sleep(1.5)
        campo_cpf.send_keys("03152024001")
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
def click_login():
    try:
        teste_botao = driver.find_element(By.ID, "kc-login")
        time.sleep(1.0)
        teste_botao.click()
        time.sleep(1.0)

        print("--------------------------------------------------")
        print("       Teste BOTÃO LOGIN: Sucesso!!!              ")
        print("--------------------------------------------------")

    except:
        print("--------------------------------------------------")
        print("       Teste BOTÃO LOGIN: Falha!!!                ")
        print("--------------------------------------------------")


# Aceitando termos e condições:
def conditions():
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
def scroll_bar():
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
def search_frequencia():
    try:

        clicar_frequencia = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/section[1]/div/div/div[2]/div/div/div[2]/a[1]')) 
        )
        
        clicar_frequencia.click()
        
        print("--------------------------------------------------")
        print("       Teste CLICAR FREQUÊNCIA: Sucesso!!!        ")
        print("--------------------------------------------------")
    except:
        print("--------------------------------------------------")
        print("       Teste CLICAR FREQUÊNCIA: Falha!!!          ")
        print("--------------------------------------------------")


# Filtrar por localidade
def clicar_filtro():
    try:
        local = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='filtroFrequenciaFacial']/span"))
        )
        local.click()
        
        clicar_novamente = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='filtroFrequenciaFacial']/span"))
        )
        clicar_novamente.click()
        print("--------------------------------------------------")
        print("       Teste Filtrar local: Sucesso!!!            ")
        print("--------------------------------------------------")
    except Exception:
        print("--------------------------------------------------")
        print("       Teste Filtrar local: Falha!!!              ")
        print("--------------------------------------------------")


# Descer tela:
def scroll_frequencia():
    try:
        wait.until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        driver.execute_script("window.scrollTo(0, 350);")
        time.sleep(1.5)
        print("--------------------------------------------------")
        print("       Teste DESCENDO PAGINA: Sucesso!!!          ")
        print("--------------------------------------------------")
    except:
        print("--------------------------------------------------")
        print("       Teste DESCENDO PAGINA: Falha!!!            ")
        print("--------------------------------------------------")


#  ordem crescente e decrescente
def order_frequencia():
    try:
        ordenar_data = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='main']/section/div/div/div/div/div[1]/table/thead/tr/th[1]"))
        )
        ordenar_data.click() 
        time.sleep(1.5) 
        ordenar_data.click()  
        

        ordenar_horario = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='main']/section/div/div/div/div/div[1]/table/thead/tr/th[2]"))
        )
        ordenar_horario.click()  
        time.sleep(1.5)
        ordenar_horario.click()  
        

        ordenar_local = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='main']/section/div/div/div/div/div[1]/table/thead/tr/th[3]"))
        )
        ordenar_local.click()  
        time.sleep(1.5)
        ordenar_local.click()  

        print("--------------------------------------------------")
        print("       Teste FILTRO DATA, HORA E LOCAL: Sucesso!!!")
        print("--------------------------------------------------")
    except Exception as e:

        print("--------------------------------------------------")
        print(f"      Teste FILTRO DATA, HORA E LOCAL: Falha!!!  ")
        print("--------------------------------------------------")


# Descer tela novamente:
def scroll_again():
    try:
        wait.until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        driver.execute_script("window.scrollTo(0, 900);")
        time.sleep(1.5)
        print("--------------------------------------------------")
        print("       Teste DESCENDO PAGINA: Sucesso!!!          ")
        print("--------------------------------------------------")
    except:
        print("--------------------------------------------------")
        print("       Teste DESCENDO PAGINA: Falha!!!            ")
        print("--------------------------------------------------")

# Testar Paginação
def test_paginacao():
    try:
        escolher_pagina2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='main']/section/div/div/div[2]/div/nav/div/div/span/button[2]"))
        )
        escolher_pagina2.click()
        time.sleep(1.5)

    
        print("--------------------------------------------------")
        print("       Teste PAGINAÇÃO: Sucesso!!!                ")
        print("--------------------------------------------------")

    except:
        print("--------------------------------------------------")
        print("       Teste PAGINAÇÃO: Falha!!!                  ")
        print("--------------------------------------------------")

# Clicando no botão MENU:
def bottom_menu():
    try:
        clicar_menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "pv_id_1_0"))
        )
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
def click_exit():
    try:
        clicar_sair = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sair"))
        )
        clicar_sair.click()
        time.sleep(1.5)
        
        print("---------------------------------------------------")
        print("       Teste CLICAR SAIR: Sucesso!!!               ")
        print("---------------------------------------------------")

    except:
        print("---------------------------------------------------")
        print("       Teste CLICAR SAIR: Falha!!!                 ")
        print("---------------------------------------------------")


def main():

    wait_url()
    user_password()
    click_login()
    conditions()
    scroll_bar()
    search_frequencia()
    clicar_filtro()
    scroll_frequencia()
    order_frequencia()
    scroll_again()
    test_paginacao()
    bottom_menu()
    click_exit()
    time.sleep(2.5)
    print("---------------------------------------------------")
    print("               FIM DA AUTOMAÇÃO!!!                 ")
    print("---------------------------------------------------")
    exit()
    input()

main()