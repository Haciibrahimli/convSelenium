from django.shortcuts import render, redirect
from selenium import webdriver
from django.contrib.auth import authenticate, login, logout
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.chrome.service import Service



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
    context = {}

    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("home")



def home_view(request):
    if request.method == "POST":
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')        
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        service = Service(executable_path="chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("https://AZN.DAY.az")
        time.sleep(5)
        x = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'large-text')))
        elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "fc-button-label")))

# Check if any elements were found
        if elements:
    # Click the first element found (you may need to adjust this depending on your specific scenario)
             elements[0].click()
        else:
             print("No elements with class name 'fc-button-label' found within the timeout period.")
        # for i in range(len(x)):
        print(x[1].text)
        print(x[2].text)
        driver.close()


    # fc-button-label

    
    context = {
        
    }
    return render(request,'home.html',context)
