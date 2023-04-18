import random
import string
from models.project import Project


def random_value():
    return ''.join(random.choices(string.ascii_letters, k=8))


def test_add_project(app):
    old_project_list = app.project.get_project_list()
    new_project = Project(name=random_value(), description=random_value())
    app.project.create_project(new_project)
    new_project_list = app.project.get_project_list()
    assert len(old_project_list) + 1 == len(new_project_list)
    old_project_list.append(new_project)
    assert sorted(old_project_list, key=Project.sort_by_name) == sorted(new_project_list, key=Project.sort_by_name)
