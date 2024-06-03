from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys


driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(1.0)


def checkUrl():
    try:
        driver.get("https://sso.fps.edu.br/realms/academico/protocol/openid-connect/auth?client_id=clientPainel&redirect_uri=https%3A%2F%2Fminhafps.fps.edu.br%2F&state=a4ea9f61-61e8-41b6-84ca-ad93f19d7f0e&response_mode=fragment&response_type=code&scope=openid&nonce=b27bf347-9ddc-4978-8c76-9cc0c9b134ef")
        time.sleep(1.5)

        print("---------------------------------------------------------------------")
        print("     Teste VALIDAR URL: Sucesso!!!                                   ")
        print("---------------------------------------------------------------------")
    except:
        print("---------------------------------------------------------------------")
        print("     Teste VALIDAR URL: Falha!!!                                     ")
        print("---------------------------------------------------------------------")

def main():
    checkUrl()
    exit()
    input()

main()