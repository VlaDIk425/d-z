class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f"Сотрудник: {self.name}, Должность: {self.position}")

emp = Employee("Биба", "Боба")
emp.display_info()


class Team:
    def __init__(self):
        self.team_members = []

    def add_member(self, name, position):
        self.team_members.append((name, position))

    def show_team(self):
        if not self.team_members:
            print("В команде пока нет сотрудников")
            return

        print("Состав команды:")
        for name, position in self.team_members:
            print(f"{name} - {position}")


team = Team()
team.add_member("Алена", "Прогер")
team.add_member("Максимка", "игроман")
team.show_team()



class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Название: {self.name}, Автор: {self.author} Год выпуска: {self.year}")

my_book = Book("Боба", "Биба", 2026)
my_book.display_info()


class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value


if __name__ == "__main__":
    book = Book(": Расказы о рыбалке", "Рыбак", 2025)

    print(f"Название: {book.title}")
    print(f"Автор: {book.author}")

    book.title = "Оунь"
    book.year = 2024

    print(f"\nНовое название: {book.title}")
    print(f"Новый год: {book.year}")