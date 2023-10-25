from model.group import Group


def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")

    #Подготовка пустой группы для изменения
    app.group.create(Group(name="", header="", footer=""))

    app.group.delete_first_group()
    app.session.logout()
