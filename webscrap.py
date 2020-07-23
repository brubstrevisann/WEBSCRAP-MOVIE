from selenium import webdriver
import pyautogui
import time
from qbittorrent import Client
from os import system,name
from tkinter import *
from tkinter.ttk import Combobox

from webdriver_manager.chrome import ChromeDriverManager



qb = Client("http://127.0.0.1:8080/")
qb.login("admin", "adminadmin")

# driver = webdriver.Chrome('C:\Users\bruno\Desktop\chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Chrome(executable_path=r"C:\PROJETOS\SCRAPS\chromedriver.exe")
x = 0

def browser(url): 
    driver.minimize_window()
    driver.get(url)
 

cat = ["LANÇAMENTOS","ACÃO","TERROR","COMÉDIA","FICCÃO"]
# def createWindow():
#     window = Tk()


#     lbl = Label(window,text="Welcome to WEBSCRAPING OF BRUBS", fg="black", font=("Arial", 17), anchor = CENTER)
#     lbl.place(x=34,y=30)
#     lbl2 = Label(window,text="Escolha uma categoria: ", fg="black",font=("Sans",14))
#     lbl2.place(x=40, y=90)
#     combo = Combobox(values=cat, width=13)
#     combo.place(x=260, y=96)
#     lbl3 = Label(window,text="Número de pages:", fg="black",font=("Sans",14))
#     entry_page = Entry(window)
#     lbl3.place(x=40, y=50)
#     lbl3.grid(x=260,y=107)
#     entry_page.grid(row=0,column=1)
 

#     window.title("WEBSCRAPING OF BRUBS")

#     window.geometry("500x500+100+200")
#     window.mainloop()


element2 = "string"
element3 = "string"
uriMagnets = []


# pyautogui.keyDown('alt')
# pyautogui.keyDown('space')
# pyautogui.press('n')
# pyautogui.keyUp('space')
# pyautogui.keyUp('alt')
# # +str(i)+
# boo = True
        
xpath = '/html/body/div[3]/div[2]/div/div[1]/div[1]/div[1]/div[2]/table[1]/tbody/tr[3]/td[7]/a'


def hasXpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False


def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
# createWindow()


contIMBD = 1
cont = 1
while cont < 2:
    clear()
    cont = cont+cont
    
print("===============================BEM VINDO AO PORTAL DO BRUBS-FILMES============================================")
print("\n\n\n\n ======ESCOLHA A CATEGORIA DESEJADA========")
categoria = int(input("\n <1> LANÇAMENTOS\n <2> AÇÃO\n <3> TERROR \n <4> COMÉDIA \n <5> FICÇÃO\n Digite uma das opções acima......\n"))

urlIMDB = "https://www.baixarfilmetorrenthd.com/genero/filmes/?orderby=lancamento"

if(categoria == 1):
    urlIMDB = "https://www.baixarfilmetorrenthd.com/genero/filmes/?orderby=lancamento"
elif(categoria == 2):
    urlIMDB = "https://www.baixarfilmetorrenthd.com/genero/filmes/acao-filmes/?orderby=lancamento"   
elif(categoria == 3):
    urlIMDB = "https://www.baixarfilmetorrenthd.com/genero/filmes/terror-filmes/?orderby=lancamento"
elif(categoria == 4):
    urlIMDB = "https://www.baixarfilmetorrenthd.com/genero/filmes/comedia-filmes/?orderby=lancamento"
elif(categoria == 5):
    urlIMDB = "https://www.baixarfilmetorrenthd.com/genero/filmes/ficcao-cientifica-filmes/?orderby=lancamento"

num_Pages = int(input("\n Escolha o numero de pages: "))

num_Pages = num_Pages*18

browser(urlIMDB)

movies_name = []
page = 2
notaIMDB = str(input("\n Digite a nota minima IMDB: "))
# clear()
num_Pages = int(input("\n NÚMERO DE PAGES: "))
num_Pages = num_Pages*19
time.sleep(2)

for i  in range(1,num_Pages):                      
    imdb = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[1]/div[2]/div['+str(contIMBD)+']/a/div[1]/span')
    text = imdb.text

    # print(imdb.text)
    if(text == "N/A"):
        text = "9.0"
    if(float(text) >= float(notaIMDB)):
        xpathDUBLADO = '/html/body/div[3]/div[2]/div/div[1]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[7]/a'
        xpathDUAL = '/html/body/div[3]/div[2]/div/div[1]/div[1]/div[1]/div[2]/table[1]/tbody/tr[3]/td[7]/a'     
        xpathDUAL1 = '/html/body/div[3]/div[2]/div/div[1]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[7]/a'               
        element = driver.find_element_by_xpath(' /html/body/div[3]/div[1]/div/div[1]/div[2]/div['+str(contIMBD)+']/a ').click()
        tag = driver.find_element_by_class_name('tbl-mv-tit')                             
        movies_name.append(tag.text)

        if "DUAL ÁUDIO" in tag.text:
            dual = hasXpath(xpathDUAL)  
            dual1 = haxXpath(xpathDUAL1)
            # print(dual)
            if(dual == True):
                element2 = driver.find_element_by_xpath(' /html/body/div[3]/div[2]/div/div[1]/div[1]/div[1]/div[2]/table[1]/tbody/tr[3]/td[7]/a').get_attribute('href')
                uriMagnets.append(element2)
            elif(dual1 == True):
                element4 = driver.find_element_by_xpath(' /html/body/div[3]/div[2]/div/div[1]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[7]/a').get_attribute('href')
            driver.back()
                
        elif("DUBLADO" in tag.text):
            dublado = hasXpath(xpathDUBLADO)
            # print(dublado)
            if(dublado == True):                        
                element3 = driver.find_element_by_xpath(' /html/body/div[3]/div[2]/div/div[1]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[7]/a').get_attribute('href')
                uriMagnets.append(element3)                
            driver.back()
           
        else:   
            driver.back()
    if(contIMBD == 18):                         
       element = driver.find_element_by_xpath('//*[@title="Page '+str(page)+'"]').click()
       page = page+1
    #    (' /html/body/div[3]/div[1]/div/div[2]/a['+str(page)+']').click()
    
       contIMBD=0
       time.sleep(2)
    # print("loop: "+str(i),"contIMBD: "+ str(contIMBD))        
    # print("page: "+str(page))
    contIMBD = contIMBD+1
    # i == 18 or i == 37 or i == 54

print("\n\n======Filmes=====\n")
for g in range(len(movies_name)) :  
    res = movies_name[g].split(' ', 1)[1].replace("DUAL ÁUDIO Torrent","")
    res.replace("DUBLADO Torrent","")

    print(str(res))    




# for z in range(len(uriMagnets)) :
#     text_file = open("Magnets.txt",'w')
#     text_file.write(uriMagnets[z])

with open('Magnets.txt', 'w') as f:
    for item in uriMagnets:
        f.write("%s\n" % item)

# for x in range(len(uriMagnets)) :  
#     print(uriMagnets[x])    



for a in range(len(uriMagnets)):
    qb.download_from_link(uriMagnets[a])
print("\n \n=========================FILMES SENDO BAIXADOS==========================")
    # if(a == 3):
    #     time.sleep(900)





# def get_size_format(b, factor=1024, suffix="B"):
#     """
#     Scale bytes to its proper byte format
#     e.g:
#         1253656 => '1.20MB'
#         1253656678 => '1.17GB'
#     """
#     for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
#         if b < factor:
#             return f"{b:.2f}{unit}{suffix}"
#         b /= factor
#     return f"{b:.2f}Y{suffix}"

# # return list of torrents
# torrents = qb.torrents()

# for torrent in torrents:
#     print("Torrent name:", torrent["name"])
#     print("hash:", torrent["hash"])
#     print("Seeds:", torrent["num_seeds"])
#     print("File size:", get_size_format(torrent["total_size"]))
#     print("Download speed:", get_size_format(torrent["dlspeed"]) + "/s")

