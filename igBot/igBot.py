from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random 

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver =  webdriver.Firefox(executable_path="C:\geckodriver.exe")

    def login(self):
        driver = self.driver
         ##Aqui abri a Url do instagram
        driver.get("https://www.instagram.com/")               
    
  
        time.sleep(3)
        ##Aqui clica no campo de usuário e senha para poder preencher.
        ##Usuário aqui:
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        ##Aqui Senha:
        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        ##Aqui é a simulação da tecla 'Enter'
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(4)
         
          ##Aqui abri a url da Foto do sorteio com o código abaixo abaixo. 
        self.comente_na_foto_big_jow('p/Ccyd27bOS13')
        time.sleep(4)

       ##método para digitar com uma pessoa  
    @staticmethod 
    def digite_como_pessoa(frase, onde_digitar):  
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(50,50)/100) ## =>aqui defini o tempo de digitação, quanto mais lento melhor.

##Metodo para abrir url da foto  do sorteio 
    def comente_na_foto_big_jow(self,perfil):
        driver = self.driver
        driver.get("https://www.instagram.com/"+ perfil +"/")
        time.sleep(4)
      
      
    
        ##Comentar no campo da foto sorteio  como um apessoa. 
      
        comentarios = ["Lucas", "Gomes", "Lima", "Deus", "bolsonaro","empatia", "embuste", "exceção", "exceto", "efêmero", "escrúpulo", "equidade", "essência", "extrovertido", "estória", "essencial", "eminente", "extensão", "empírico", "esdrúxulo", "encarecidamente", "extraordinário", "expectativa", "esperança", "escopo", "estigma", "estável", "eminência", "exortar", "escória", "entretanto", "excêntrico",
         "emergir", "eclesiástico", "explícito", "equivocado", "exequível", "exímio", "esmo", "elegível", "experiência", "escárnio", "espectro", "escrutínio", "excelência", "excerto", "expressão", "execrável", "endêmico", "estrupo", "expedido", "epifania", 
         "emulação", "excesso", "espontâneo", "ensejo", "esplêndido", "eficaz", "estúpido", "eloquente", "erudito", "embora", "exótico", "escroto", "estereótipo", "empecilho", "exilado", "escusa", "especulação", "estagnado", "etnia", "exílio",
          "excelente", "enxergar", "excitado", "elucubração", "emotivo", "estirpe", "entediado", "exacerbado", "excedente", "exortação", "ego", "enfadonho",
           "epistemologia", "esporádico", "escrever", "expor", "etéreo", "estabelecer", "empáfia", "estupefato", "ermo", "excludente", "eximir", "etimologia", "escasso", "elucidar", "efeminado", 
           "espairecer", "emergente", "então", "excepcional", "espúrio", "extasiado","lucaslima_98","Deus","Fluminense","Gama","Eu quero","Eu vou ganhar"]

        
        for comentario in comentarios: 
            try:
                driver.find_element_by_xpath(' /html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea').click()
                campo_comentario = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
                time.sleep(random.randint(2,5))
                self.digite_como_pessoa(random.choice(comentarios), campo_comentario)
                time.sleep(random.randint(50,150)) 
                driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button").click()
                time.sleep(random.randint(30))

            except Exception as e:
                print(e)
                time.sleep(5)



     
          


lucasBot = InstagramBot('lucasgl_98', '180598.lima')     
lucasBot.login()



##Está fzd  o comentario, porem tem que deixar mais lento e fazer atribuições para deixar mais top.





