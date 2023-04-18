import random
from models.project import Project


def test_del_project(app):
    old_project_list = app.project.get_project_list()
    if len(old_project_list) == 0:
        app.project.create_project(Project(name="test"))
        old_project_list = app.project.get_project_list()
    random_project = random.choice(old_project_list)
    app.project.del_project(random_project.name)
    new_project_list = app.project.get_project_list()
    assert len(old_project_list) - 1 == len(new_project_list)
    old_project_list.remove(random_project)
    assert sorted(old_project_list, key=Project.sort_by_name) == sorted(new_project_list, key=Project.sort_by_name)
