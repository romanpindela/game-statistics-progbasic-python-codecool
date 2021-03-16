import reports


def ask_integer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter an integer!")
            continue


def print_count_games(file_name):
    number_of_games = reports.count_games(file_name)
    print(f"How many games are in the file? {number_of_games}")


def print_decide(file_name):
    input_year = ask_integer("Enter a year: ")
    is_game_from_year = reports.decide(file_name, input_year)
    print(f"Is there a game from year ({input_year})? {is_game_from_year}")


def print_latest_title(file_name):
    latest_title = reports.get_latest(file_name)
    print(f"The latest game is: {latest_title}")


def print_count_by_genre(file_name):
    input_genre = input("Enter a genre: ")
    number_of_games_by_genre = reports.count_by_genre(file_name, input_genre)
    print(f"The number of games of genre '{input_genre}': {number_of_games_by_genre}")


def print_line_number_by_title(file_name):
    while True:
        input_title = input("Enter a title: ")
        try:
            line_number = reports.get_line_number_by_title(file_name, input_title)
            break
        except ValueError:
            print("There's no such title. Please enter another one!")
            continue

    print(f"The line number of '{input_title}': {line_number}")


def print_sorted_titles(file_name):
    sorted_titles = "\n\t".join(reports.sort_abc(file_name))
    print(f"The alphabetically ordered list of the titles:\n\t{sorted_titles}")


def print_sorted_genres(file_name):
    sorted_genres = "\n\t".join(reports.get_genres(file_name))
    print(f"The genres in this file in alphabetical order:\n\t{sorted_genres}")


def print_year_of_top_sold_fps(file_name):
    try:
        year_of_top_sold_fps = reports.when_was_top_sold_fps(file_name)
    except ValueError:
        year_of_top_sold_fps = "No 'First-person shooter' game in the database!"
    print(f"The release year of the top sold 'First-person shooter' game: {year_of_top_sold_fps}")


def main():
    while True:
        file_name = input("Enter the name of a data file: ")
        try:
            print_count_games(file_name)
            print_decide(file_name)
            print_latest_title(file_name)
            print_count_by_genre(file_name)
            print_line_number_by_title(file_name)
            print_sorted_titles(file_name)
            print_sorted_genres(file_name)
            print_year_of_top_sold_fps(file_name)
            break
        except FileNotFoundError:
            print("File not found!")
            continue


if __name__ == "__main__":
    main()
