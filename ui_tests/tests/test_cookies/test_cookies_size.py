from d14_base.data_reader import DataReader
from d14_ui_framework.browser.browser import Browser
from d14_ui_framework.elements.label import Label
from d14_ui_framework.elements.base.element_state import ElementState
from d14_ui_framework.pages.base_page import BasePage
from d14_ui_framework.utils.links_checker_util import LinksCheckerUtil
from d14_ui_framework.waits.web_driver_wait_for import wait_for


class TestCookies:

    DEPTH = 6
    EXTENSIONS_TO_IGNORE = ["ico", "css", "js", "png", "css", "svg", "jpg"]
    CORRECT_PART_OF_URL = '.abudhabi'

    def test_cookies(self):
        start_url = DataReader()._get_env_config()['start_url']
        depth_and_url = {0: [start_url]}
        all_urls = {start_url}
        for current_depth in range(TestCookies.DEPTH + 1):
            depth_and_url[current_depth + 1] = []
            for url in depth_and_url[current_depth]:
                Browser.set_url(url)
                Browser.wait_for_page_to_load()
                Label("//*[contains(@class, 'spinner')]", "Spinner")\
                    .soft_wait_for_element_state(ElementState.NOT_VISIBLE)

                wait_for(Browser.get_driver(),
                         lambda: len(LinksCheckerUtil.get_links(all_urls)) == len(LinksCheckerUtil.get_links(all_urls)))
                BasePage(Label("//body", url))
                for link in LinksCheckerUtil.get_links(all_urls):
                    if TestCookies.CORRECT_PART_OF_URL in link \
                            and link.split(".")[-1] not in TestCookies.EXTENSIONS_TO_IGNORE:
                        all_urls.add(link)
                        depth_and_url[current_depth + 1].append(link)
