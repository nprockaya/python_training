from Models.group_class import Group
import random


def test_edit_group_name(app, db, check_ui):
    if app.group.count_groups() == 0:
        app.group.create(Group(_name="for_edit_test", _header="", _footer=""))
    # получаем список групп с БД
    old_groups = db.get_group_list()
    # выбираем из списка случайную группу
    group = random.choice(old_groups)
    # задаем новые данные для группы
    new_group_data = Group(_name="name_group_edit_test",
                           _header="header_group_edit_test",
                           _footer="footer_group_edit_test")
    # модифицируем группу
    app.group.edit_group_by_id(group.group_id, new_group_data)
    # получаем новый список групп
    new_groups = db.get_group_list()
    # ищем отредактированную группу по id
    new_group = next(x for x in new_groups if x.group_id == group.group_id)
    # в старом списке удаляем старую группу
    old_groups.remove(group)
    # на его место добавляем новую отредактированную
    old_groups.append(new_group)
    # сравниваем длины старого и нового списков
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
