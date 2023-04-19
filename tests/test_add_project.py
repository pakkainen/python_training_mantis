import random
import string
from models.project import Project


def random_value():
    return ''.join(random.choices(string.ascii_letters, k=8))


def test_add_project(app, json_projects):
    new_project = json_projects
    old_project_list = app.soap.get_project_list()
    app.project.create_project(new_project)
    new_project_list = app.soap.get_project_list()
    assert len(old_project_list) + 1 == len(new_project_list)
    old_project_list.append(new_project)
    assert sorted(old_project_list, key=Project.sort_by_name) == sorted(new_project_list, key=Project.sort_by_name)
