class DocumentDetails:

    def __init__(self, name: str, category: str):
        self.__name = name
        self.__category = category

    def get_name(self) -> str:
        return self.__name

    def get_category(self) -> str:
        return self.__category
