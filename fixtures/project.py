from selenium.webdriver.common.by import By
from models.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_list(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Manage").click()
        wd.find_element(By.LINK_TEXT, "Manage Projects").click()

    def create_project(self, project):
        wd = self.app.wd
        self.open_project_list()
        # open the form for adding a project
        wd.find_element(By.CSS_SELECTOR, "input[value='Create New Project']").click()
        self.fill_project_form(project)
        # submit project adding
        wd.find_element(By.CSS_SELECTOR, "input[value='Add Project']").click()
        # fast transition to projects
        wd.find_element(By.LINK_TEXT, 'Proceed').click()
        self.project_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def del_project(self, project):
        wd = self.app.wd
        self.open_project_list()
        wd.find_element(By.LINK_TEXT, project).click()
        wd.find_element(By.CSS_SELECTOR, 'input[value="Delete Project"]').click()
        wd.find_element(By.CSS_SELECTOR, 'input[value="Delete Project"]').click()
        self.project_cache = None

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_list()
            self.project_cache = []
            rows = wd.find_elements(By.XPATH, "//table[3]/tbody/tr")[2:]
            for element in rows:
                cells = element.find_elements(By.CSS_SELECTOR, "td")
                name = cells[0].text
                description = cells[4].text
                self.project_cache.append(Project(name=name, description=description))
        return list(self.project_cache)
