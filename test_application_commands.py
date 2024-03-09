from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.saucedemo.com/')

# title
print("Titulo da pagina é: ", browser.title)

# current_url
print("A URL da pagina é: ", browser.current_url)

# page_source
print("O codigo fonte da pagina é: ", browser.page_source)
