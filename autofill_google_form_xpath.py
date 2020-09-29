from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument("-incognito")
#option.add_experimental_option("excludeSwitches", ['enable-automation']);
#option.add_argument("--headless")
#option.add_argument("disable-gpu")
browser = webdriver.Chrome(options=option)

browser.get("https://docs.google.com/forms/d/e/1FAIpQLSf9uFNd5Jnb5Av_97aD9-PU_7P9ElbSz_8k6F8xKC57WTcoFw/viewform")

textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
submitbutton = browser.find_element_by_xpath("""/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span""")

textboxes[0].send_keys("Hello World")

radiobuttons[2].click()

checkboxes[1].click()
checkboxes[3].click()
submitbutton.click()
