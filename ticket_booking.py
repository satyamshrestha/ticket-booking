from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
options = Options()
options.add_argument("--headless")

driver.get("https://bigmovies.com.np/")
popup = driver.find_element(By.ID, "HtmlPopUpclose")
popup.click()

time.sleep(1)

movie = driver.find_element(By.XPATH, "/html/body/form/div[6]/div/div[2]/div[1]/div[2]/ul/div/div/div[1]")
driver.execute_script("window.scrollTo(0, 600);")
movie.click()

time.sleep(1)

# Audi and Show Time Selection
driver.execute_script("window.scrollTo(0, 560);")
audi_element = driver.find_elements(By.CSS_SELECTOR, "div.audi-time")
audi = int(input("Enter the audi you want to watch the movie in: "))
shows_element = audi_element[audi-1].find_elements(By.CSS_SELECTOR, "a.available")
shows = len(shows_element)
print("Available no. of shows = {} at:".format(shows))
for i in range(shows):
    j = 1
    print(f"{j}.", shows_element[i].text)
show = int(input("Which show do you want to watch?\n"))
shows_element[show-1].click()
driver.find_element(By.ID, "lytA_ctl08_UserName").send_keys("youremail@gmail.com")  # Fill email
driver.find_element(By.ID, "lytA_ctl08_Password").send_keys("yourpassword") #Fill password
submit = driver.find_element(By.ID, "lytA_ctl08_LoginButton")
submit.click()
time.sleep(7)

#Ticketing
required = int(input("Enter the no. of seats you want: "))
n = 1
print("Available seats are:")
for id in range(7, 20):
    seat = driver.find_element(By.ID, "tdSeat_D{}".format(id))
    seat_span = seat.find_element(By.TAG_NAME, "span")
    class_name = seat_span.get_attribute("class")
    if class_name == "sfAvailableSeat cineSeats ":
        print("{}. {}".format(n, seat_span.text))
        n+=1

booked = []
for i in range(required):
    book = int(input("Enter the seat you want to book:\n"))
    booked.append(book)
print(booked)

for i in range(len(booked)):
    book_seat = driver.find_element(By.ID, "tdSeat_D{}".format(booked[i]))
    book_span = book_seat.find_element(By.TAG_NAME, "span")
    book_span.click()

    proceed = driver.find_element(By.CSS_SELECTOR, "span#btnReserveTicket")
    proceed.click()
    method = driver.find_element(By.XPATH, "/html/body/form/div[6]/div/div/div[2]/div/div/div/div[1]/div[4]/ul/li[1]/span")
    driver.execute_script("arguments[0].click();", method)
    time.sleep(7)
    
    username = driver.find_element(By.CSS_SELECTOR, "input.p-inputtext p-component p-element input-group__field ng-untouched ng-pristine ng-valid ng-star-inserted")
    pw = driver.find_element(By.CSS_SELECTOR, "input.p-inputtext p-component p-element ng-tns-c41-5 p-password-input")
    username.send_keys("9800000000") #Phone no. of esewa id
    pw.send_keys("1234") #MPIN

    captcha = driver.find_element(By.CSS_SELECTOR, "div.recaptcha-checkbox-border")
    captcha.click()

    login = driver.find_element(By.CSS_SELECTOR, "button.p-ripple p-element btn btn--primary btn--full-width p-button p-component")
    login.click()
    print("Successfully booked your ticket!")

driver.quit()
