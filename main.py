from selenium import webdriver
import time
import easygui

url = "https://www.cdiscount.com/informatique/ecran-pc/pack-2-ecrans-pc-gamer-iiyama-g-master-black-haw/f-10710-bungmasterbh.html"
savefile = "price.txt"

def GetPrice():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)

    result = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/div[2]/div[2]/div/div[2]/form[1]/div[1]/span[2]").text

    driver.close()
    return result

def Alerte(old, new):
    easygui.msgbox("Nouveau prix! \n Ancien prix: {}\n Nouveau prix : {}".format(old, new), title="Changement de prix CDiscount")

print("Démarrage...")

while True:
    price = GetPrice()
    print("Prix trouvé : " + price)
    save_price = open(savefile, "r").readline()
    if save_price != price:
        open(savefile, "w").write(price)
        Alerte(save_price, price)
    time.sleep(180)
