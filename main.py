from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

vaga = input("Digite O Nome Da Vaga : ")

navegador = webdriver.Chrome()
url = f"https://br.linkedin.com/jobs/search?keywords={vaga}"

navegador.maximize_window()
navegador.get(url)

vagas_disponiveis = []

try :
    espera = WebDriverWait(navegador,10)
    fechar_popup = espera.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal__dismiss.btn-tertiary")))
    navegador.execute_script("arguments[0].click();", fechar_popup)
except Exception as e :
    print("---Pop-Up não encontrado---")
    pass

for i in range(3):
    navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

caixa_emprego = navegador.find_elements(By.CLASS_NAME, "base-card")

for emprego in caixa_emprego :
    try : 
        titulo = emprego.find_element(By.CLASS_NAME,"base-search-card__title").text
        empresa = emprego.find_element(By.CLASS_NAME,"base-search-card__subtitle").text
        local = emprego.find_element(By.CLASS_NAME,"job-search-card__location").text
        link = emprego.find_element(By.CLASS_NAME,"base-card__full-link").get_attribute("href")

        try :
            publicacao = emprego.find_element(By.CLASS_NAME,"job-search-card__listdate--new").get_attribute("datetime")
        except:
            try:
                publicacao = emprego.find_element(By.CLASS_NAME,"job-search-card__listdate").get_attribute("datetime")
            except:
                publicacao = "Data Indisponível"

        vagas_disponiveis.append({"Título":titulo,"Empresa":empresa,"Local":local,"Link":link,"Publicação":publicacao})

    except Exception as e : 
        print(f"Uma vaga estava com o defeito {e}. Pulando para a próxima...")
        continue

navegador.quit()

df = pd.DataFrame(vagas_disponiveis)
df.to_excel("Vagas_Encontradas.xlsx", index=False)