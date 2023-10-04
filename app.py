from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import openpyxl
import selenium
import time

sleep = time.sleep 

start01 = "********************"
start02 = "*                  *"
start03 = "*    JSYSTEM       *"
start04 = "*  PROGRAMA TESTE  *"
start05 = "*  VERSÃO 1.0.1    *"
start06 = "*                  *"
print(start01)
print(start02)
print(start03)
print(start04)
print(start05)
print(start06)
print(start01)

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

workbook = openpyxl.load_workbook('arquivo.xlsx')



try:

    workbook = openpyxl.Workbook

    #ADD dentro do excel ou calc
    pagina_processo = workbook[numero_processo]

    excel1['A1'].value = "Numero Processo"
    excel2['A2'].value = "Situação Processo"
    excel3['A3'].value = "Ultima data"

    pagina_processo['A2'].value = [numero_processo]
    
    #Movimentação de Linhas
    for index, linhas in enumerate(pagina_processo.iter_rows(min_row=2, max_row=len(lista_processo), min_col=3, max_col=3)):
        for celula in linha:
            celula.value=lista[index]

workbook.save(arquivo)
driver.close()
sleep(5)

driver.switch_to.window(driver.window_handles)

end01 = "********************"
end02 = "*                  *"
end03 = "*    JSYSTEM       *"
end04 = "*  DESLIGANDO OS   *"
end05 = "*  VERSÃO 1.0.1    *"
end06 = "*                  *"
print(end01)
print(end02)
print(end03)
print(end04)
print(end05)
print(end06)
print(end01)

except Exception as error
#SE ACONTECER ERROR 
print(F"OCORREU UM ERROR{error}")