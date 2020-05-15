from poium import Page,PageElement
from page.orgapply import Joinorgpage

class Href(Page):
    def org(self):
        return Joinorgpage(self.driver)