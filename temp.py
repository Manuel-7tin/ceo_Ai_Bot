import streamlit as st

"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

with st.echo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.core.os_manager import ChromeType

    @st.cache_resource
    def get_driver():
        return webdriver.Chrome(
            service=Service(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=options,
        )

    options = Options()
    # options.add_argument("--keep-alive")
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")

    driver = get_driver()
    driver.get("https://www.google.com/localservices/prolist?g2lbs=AIQllVwDiiGa9oOIUCw7gitIhAuGMOuomMVm8DHMGuksBpWpcWOVowKmkNa_LoQifno1JGyovc10bhqhQLA6DnaKdbhyuaxVYI-aqwgFIwXXITDjRC4gKD0%3D&hl=en-us&gl=us&ssta=1&oq=Roof%20Masters%2C%20LLC%20901%202nd%20Loop%20Road%0D%0AFlorence%2C%20SC%2029505&src=2&lrlstt=1714313142875&ved=0CAUQjdcJahcKEwjwqIOQiuWFAxUAAAAAHQAAAAAQSQ&q=United%20Roofing%20Systems%20Houston%2C%20TX%2077064&slp=MgBAAVIECAIgAIgBAA%3D%3D&spp=Cg0vZy8xMWg3NjRybWc0OvQBV2k4UUFCQUJFQUlpSjNWdWFYUmxaQ0J5YjI5bWFXNW5JSE41YzNSbGJYTWdhRzkxYzNSdmJpQjBlQ0EzTnpBMk5Lb0JnQUVLQ0M5dEx6QXpiREp1Q2dndmJTOHdOMkpmYkJBQktob2lGblZ1YVhSbFpDQnliMjltYVc1bklITjVjM1JsYlhNb0FESWZFQUVpRzIzTURlNEhsa2VCR3AzT242OEhGNmVpM2ZxTmJXZUdQMG0ySlRJckVBSWlKM1Z1YVhSbFpDQnliMjltYVc1bklITjVjM1JsYlhNZ2FHOTFjM1J2YmlCMGVDQTNOekEyTkE9PQ%3D%3D&scp=ChdnY2lkOnJvb2ZpbmdfY29udHJhY3RvchIAGgAqElJvb2ZpbmcgY29udHJhY3Rvcg%3D%3D")

    st.code(driver.page_source)