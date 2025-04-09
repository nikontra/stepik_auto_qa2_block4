from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(driver):
    page = MainPage(driver, link)
    page.open()
    page.go_to_login_page()


