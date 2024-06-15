from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

app = Flask(__name__)
url = "http://www.bianca.com"

opts = Options()
opts.headless = True

def scraping():
    driver = webdriver.ChromiumEdge(options=opts)
    try:
        driver.get(url)
        content = driver.find_elements(By.XPATH, '/html/body/h1')
        return content[0].text
    
    finally:
        driver.quit()

@app.route('/scrape')
def scrape():
    scraped_content = scraping()
    return scraped_content

if __name__ == '__main__':
    app.run(debug=True)
