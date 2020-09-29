from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument("-incognito")
#option.add_experimental_option("excludeSwitches", ['enable-automation']);
#option.add_argument("--headless")
#option.add_argument("disable-gpu")
browser = webdriver.Chrome(options=option)

browser.get("https://forms.gle/FoAoauz53Xy7A4n68")

textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
submitbutton = browser.find_element_by_xpath("""/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span""")

textboxes[0].send_keys("Hello World")

radiobuttons[2].click()

checkboxes[1].click()
checkboxes[3].click()
submitbutton.click()
