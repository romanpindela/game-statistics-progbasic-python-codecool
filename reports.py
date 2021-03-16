import csv

def open_file(file_name) -> list:
    list_of_elements = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        for row in csv_reader:
            list_of_elements.append(row)
    return list_of_elements

def count_games(file_name) -> int:
    # 1. "How many games are in the file?" - asks Judy. Implement `count_games(file_name)` that answers this question. The expected output of the function is a number.
    # - The function returns the number of games (as a number) based on the given data file
    games = open_file(file_name)
    counter = 0
    for game in games:
        counter += 1
    return counter


def decide(file_name, year):
    pass


def get_latest(file_name):
    pass


def count_by_genre(file_name, genre):
    pass


def get_line_number_by_title(file_name, title):
    # 5. "What is the line number of a given title?" - asks Judy. Implement `get_line_number_by_title(file_name, title)` that answers this question based on the given data file. The expected output of the function is a number. If the title is not found then it should raise a `ValueError` exception.
    #     - The function returns the number of games of the given (as a number) based on the given data file
    #     - The function raises a `ValueError` exception if the title is not found in the given data file
    games = open_file(file_name)
    title_id_column = 0
    line_number = 0
    line_counter = 0
    found_title_line_number = 0
    for game in games:
        line_counter += 1
        if game[title_id_column].lower() == title.lower():
            found_title_line_number = line_counter
    if found_title_line_number == 0:
        raise ValueError
    else:
        return found_title_line_number


def sort_abc(file_name):
    pass


def get_genres(file_name):
    pass


def when_was_top_sold_fps(file_name):
    pass


print(count_games('game_stat.txt'))
print(get_line_number_by_title('game_stat.txt', 'Counter-Strike'))
