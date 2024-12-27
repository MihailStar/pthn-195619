# 1
def print_results(subjects_and_grades: list[tuple[str, int]]) -> None:
    for subject_and_grade in sorted(
        subjects_and_grades, key=lambda subject_and_grade: subject_and_grade[1]
    ):
        print(*subject_and_grade)


# 2
def print_results(subjects_and_grades: list[tuple[str, int]]) -> None:
    for subject_and_grade in sorted(
        subjects_and_grades,
        key=lambda subject_and_grade: subject_and_grade[1],
        reverse=True,
    ):
        print(*subject_and_grade)


# 3
def print_results(subjects_and_grades: list[tuple[str, int]]) -> None:
    for subject_and_grade in sorted(
        subjects_and_grades,
        key=lambda subject_and_grade: (
            -subject_and_grade[1],
            subject_and_grade[0].upper(),
        ),
    ):
        print(*subject_and_grade)


# 4
def print_results(subjects_and_grades: list[tuple[str, int]]) -> None:
    for subject_and_grade in sorted(
        sorted(
            subjects_and_grades,
            key=lambda subject_and_grade: subject_and_grade[0].upper(),
            reverse=True,
        ),
        key=lambda subject_and_grade: -subject_and_grade[1],
    ):
        print(*subject_and_grade)

# 4
def print_results(subjects_and_grades: list[tuple[str, int]]) -> None:
    for subject_and_grade in sorted(
        subjects_and_grades,
        key=lambda subject_and_grade: (
            subject_and_grade[1],
            subject_and_grade[0].upper(),
        ),
        reverse=True,
    ):
        print(*subject_and_grade)


# 5
def get_sort_lines(lines: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return sorted(lines, key=lambda line: (abs(line[1] - line[0]), line))


# 6
from typing import TypedDict


class Good(TypedDict):
    make: str
    model: int
    color: str


def print_goods(goods: list[Good]) -> None:
    for good in sorted(goods, key=lambda good: (good["color"].upper(), -good["model"])):
        print(
            f"Производитель: {good['make']}, модель: {good['model']}, цвет: {good['color']}"
        )


# 7
from typing import NamedTuple


class Good(NamedTuple):
    name: str
    price: float


def parse_goods(lines: list[str]) -> list[Good]:
    goods: list[Good] = []

    for line in lines:
        name, price = line.split(": ")
        goods.append(Good(name, float(price)))

    return goods


def print_goods(lines: list[str]) -> None:
    for good in sorted(
        parse_goods(lines), key=lambda good: (-good.price, good.name.upper())
    ):
        print(f"{round(good.price, 2):.2f} - {good.name}")


# 8
from collections import Counter


def print_best_and_worst_laureate(d: dict[str, str]) -> None:
    values_to_counts = Counter(d.values()).most_common()

    print(*values_to_counts[0], sep=", ")
    print(*values_to_counts[-1], sep=", ")


# 9
from collections import defaultdict
from statistics import mean


def print_order_rating(drivers_and_ratings: list[tuple[str, int]]) -> None:
    driver_to_ratings: dict[str, list[int]] = defaultdict(list)

    for driver, rating in drivers_and_ratings:
        driver_to_ratings[driver].append(rating)

    driver_to_avg_rating = {
        driver: float(mean(ratings)) for driver, ratings in driver_to_ratings.items()
    }

    drivers_and_avg_ratings = sorted(
        driver_to_avg_rating.items(),
        key=lambda driver_and_avg_rating: (
            -driver_and_avg_rating[1],
            driver_and_avg_rating[0].upper(),
        ),
    )

    for driver, avg_rating in drivers_and_avg_ratings:
        print(driver, avg_rating)


# 10
def print_statistic(authors_and_commentators: list[tuple[str, str]]) -> None:
    author_to_commentators: dict[str, list[str]] = {}

    for author, commentator in authors_and_commentators:
        author_to_commentators.setdefault(author, []).append(commentator)

    authors_to_number_of_unique_comments = sorted(
        {
            author: len(set(author_to_commentators[author]))
            for author in author_to_commentators
        }.items(),
        key=lambda author_and_number_of_unique_comment: (
            -author_and_number_of_unique_comment[1],
            author_and_number_of_unique_comment[0].lower(),
        ),
    )

    for author, number_of_unique_comment in authors_to_number_of_unique_comments:
        print(
            f"Количество уникальных комментаторов у {author} - {number_of_unique_comment}"
        )


# 10
def print_statistic(authors_and_commentators: list[tuple[str, str]]) -> None:
    author_to_unique_comments: dict[str, set[str]] = {}

    for author, commentator in authors_and_commentators:
        author_to_unique_comments.setdefault(author, set()).add(commentator)

    authors_to_number_of_unique_comments = sorted(
        {
            author: len(author_to_unique_comments[author])
            for author in author_to_unique_comments
        }.items(),
        key=lambda author_and_number_of_unique_comment: (
            -author_and_number_of_unique_comment[1],
            author_and_number_of_unique_comment[0].lower(),
        ),
    )

    for author, number_of_unique_comment in authors_to_number_of_unique_comments:
        print(
            f"Количество уникальных комментаторов у {author} - {number_of_unique_comment}"
        )
