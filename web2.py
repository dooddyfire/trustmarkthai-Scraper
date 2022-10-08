import datetime
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Fix
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
#Insert file name
start_page = int(input("ใส่เลขหน้าเริ่มต้น: "))

#Insert result name
end_page = int(input("ใส่เลขหน้าสุดท้าย: "))




page = []

#Get bot selenium make sure you can access google chrome
driver = webdriver.Chrome(ChromeDriverManager().install())


cust_detail = []
count = 0
for i in range(start_page,end_page+1):

    url = "https://www.trustmarkthai.com/th/search?type_filter=0&total=100&page={}".format(i)
    
    driver.get(url)
    print(driver.page_source)

    soup = BeautifulSoup(driver.page_source,'html.parser')
    
    lis = [i for i in soup.find_all('td',{'class':'t-center2f'})]
    
   
    for i in lis: 
        try:
            cust_url = i.find('a')['href']
            print(i.find('a')['href'])
            print("------------------")
            cust_detail.append(cust_url)
        except:
            pass

time.sleep(1)

real_detail = []

name_th_lis = []
name_eng_lis = []
company_name_lis = []
identity_number_lis = []
online_store_lis = []
bussiness_lis = []
contact_place_lis = []
phone_lis = []
email_lis = []
fax_lis = []
dbd_register_lis = []
dbd_expire_lis = []

print(cust_detail)
for detail_url in cust_detail:
    driver.get(detail_url)

    
    name_th = driver.find_element(By.XPATH,"/html/body/div[1]/table/tbody/tr[6]/td[2]").text
    name_th_lis.append(name_th)
    print(name_th)

    
    name_eng = driver.find_element(By.XPATH,"/html/body/div[1]/table/tbody/tr[7]/td[2]").text 
    name_eng_lis.append(name_eng)
    print(name_eng)

    
    company_name = driver.find_element(By.XPATH,"/html/body/div[1]/table/tbody/tr[9]/td[2]").text 
    company_name_lis.append(company_name)
    print(company_name)

    
    identity_number = driver.find_element(By.XPATH,"/html/body/div[1]/table/tbody/tr[10]/td[2]").text
    identity_number_lis.append(identity_number)
    print(identity_number)

    try:
        online_store = driver.find_element(By.XPATH,"/html/body/div[1]/table/tbody/tr[11]/td[2]/a").text
        online_store_lis.append(online_store)
        print(online_store)
    except:
        online_store = ""
        online_store_lis.append(online_store)
        print(online_store)

    
    bussiness = driver.find_element(By.XPATH,"/html/body/div[1]/table/tbody/tr[12]/td[2]").text 
    bussiness_lis.append(bussiness)
    print(bussiness)

    
    contact_place = driver.find_element(By.XPATH,"/html/body/div[1]/table/tbody/tr[14]/td[2]").text 
    contact_place_lis.append(contact_place)
    print(contact_place)
    
    
    phone = driver.find_element(By.XPATH,"/html/body/div[1]/table/tbody/tr[16]/td[2]").text 
    phone_lis.append(phone)
    print(phone)

    
    email = driver.find_element(By.XPATH,"/html/body/div[1]/table/tbody/tr[18]/td[2]").text 
    email_lis.append(email)
    print(email)

    
    fax = driver.find_element(By.XPATH,"/html/body/div[1]/table/tbody/tr[17]/td[2]").text 
    fax_lis.append(fax)
    print(fax)


    
    dbd_register = driver.find_element(By.XPATH,"/html/body/div[1]/table/tbody/tr[20]/td[2]").text 
    dbd_register_lis.append(dbd_register)
    print(dbd_register)

    
    dbd_expire = driver.find_element(By.XPATH,"/html/body/div[1]/table/tbody/tr[21]/td[2]").text 
    dbd_expire_lis.append(dbd_expire)
    print(dbd_expire)

print(name_eng_lis,len(name_eng_lis))
driver.close()

df = pd.DataFrame()

df['ชื่อผู้ประกอบการ'] = name_th_lis
df['ชื่อผู้ประกอบการ อังกฤษ'] = name_eng_lis
df['Company Name'] = company_name_lis
df['เลขประจำตัวประชาชน'] = identity_number_lis
df['ชื่อร้านค้าออนไลน์'] = online_store_lis
df['ประเภทธุรกิจ'] = bussiness_lis
df['สถานที่ติดต่อ'] = contact_place_lis
df['เบอร์โทรศัพท์'] = phone_lis
df['Email'] = email_lis 
df['Fax'] = fax_lis 
df['วันที่ลงทะเบียน DBD'] = dbd_register_lis 
df['วันที่หมดอายุ DBD'] = dbd_expire_lis


df.to_excel("WEB3.xlsx")
print("All done!")