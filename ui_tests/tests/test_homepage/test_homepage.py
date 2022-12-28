from ui_tests.pages.homepage.homepage import Homepage


class TestHomepage:
    def test_homepage(self):
        homepage = Homepage()
        homepage.click_search_icon()
       # homepage.click_searchbox()

       #Homepage().click_searchbox()
        #Homepage().send_text(self,'Golden')



