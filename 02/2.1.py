# 1
def say_hello(name: str) -> None:
    print(f"Привет, {name}!")


def choose_profession(profession: str) -> None:
    print(f"Я хочу стать {profession}ом")


say_hello("Артем")
choose_profession("Разработчик")


# 2
def welcome_to_course(course_name: str) -> None:
    print("Приветствую")
    print(f'Добро пожаловать на курс "{course_name}"')


welcome_to_course("Функции в Python")


# 3
def repeat_n_times(n: int) -> None:
    print(*["Я стану программистом"] * n, sep="\n")


# 4
def repeat_phrase_n_times(phrase: str, n: int) -> None:
    print(*(phrase,) * n, sep="\n")
