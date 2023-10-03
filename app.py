from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import openpyxl
import selenium
import time

sleep = time.sleep 

driver = webdriver.Chrome()
driver.get("https://www.jusbrasil.com.br/login?next_url=https%3A%2F%2Fwww.jusbrasil.com.br%2Fconsulta-processual%2Ftjrj%2F%3Futm_source%3Dgoogle%26utm_medium%3Dcpc%26utm_campaign%3Dlawsuit-search%26utm_term%3D%26utm_content%3Dpfmax-versao1")
sleep(5)

email = ""
email_colocar = driver.find_element(By.XPATH, "//input[@id='FormFieldset-email']")
email_colocar.send_keys(email)
sleep(2)

senha = ""
senha_colocar = driver.find_element(By.XPATH, "//input[@id='FormFieldset-password']")
senha_colocar.send_keys(senha)
sleep(2)

entrar = driver.find_element(By.XPATH, "//button[@class='SubmitButton btn btn--block btn--blue btn--lg']")
entrar.click()

sleep(15)


numero_processo_cpf = ""
consultar = driver.find_element(By.XPATH, "//input[@class='LawsuitSearchForm-textField form-control form-control--lg']")
consultar.send_keys(numero_processo_cpf)
sleep(3)

pesquisar = driver.find_element(By.XPATH, "//button[@class='LawsuitSearchForm-btn btn btn--blue']")
pesquisar.click()
sleep(2)

ver_processo = driver.find_element(By.XPATH, "//button[@class='btn btn--flat btn--blue']")
ver_processo.click

