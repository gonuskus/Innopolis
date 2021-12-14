

class PagesAPI:
    """
    Класс-инициализатор объектов пользователей и генерации пакетов
    """

    def __init__(self, base_url):
        self.actions = Actions(base_url)

class Actions:

    def __init__(self, base_url):
        self.common = Common(base_url)




"""
Группа классов для генерации данных для сущностей платформы Фабрикант
"""
