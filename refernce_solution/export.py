import sys
import reports


def get_text_for_count_games(file_name):
    return str(reports.count_games(file_name))


def get_text_for_decide(file_name, year):
    return str(reports.decide(file_name, year))


def get_text_for_latest_title(file_name):
    return str(reports.get_latest(file_name))


def get_text_for_count_by_genre(file_name, genre):
    return str(reports.count_by_genre(file_name, genre))


def get_text_for_line_number_by_title(file_name, title):
    try:
        return str(reports.get_line_number_by_title(file_name, title))
    except ValueError:
        return f"There's no such title as '{title}''."


def get_text_for_sorted_titles(file_name):
    return ", ".join(reports.sort_abc(file_name))


def get_text_for_sorted_genres(file_name):
    return ", ".join(reports.get_genres(file_name))


def get_text_for_year_of_top_sold_fps(file_name):
    try:
        return str(reports.when_was_top_sold_fps(file_name))
    except ValueError:
        return "No 'First-person shooter' games in the database!"


def get_cli_args():
    cli_args = {}

    if len(sys.argv) != 6:
        print("Wrong number of arguments. " +
              "Usage: python3 export.py source_file_name target_file_name input_year input_genre input_title")
        exit()

    cli_args["source_file_name"] = sys.argv[1]
    cli_args["target_file_name"] = sys.argv[2]
    try:
        cli_args["input_year"] = int(sys.argv[3])
    except ValueError:
        print("Input year has to be an integer!")
        exit()
    cli_args["input_genre"] = sys.argv[4]
    cli_args["input_title"] = sys.argv[5]

    return cli_args


def main():
    cli_args = get_cli_args()

    try:
        with open(cli_args["target_file_name"], "w") as file:
            file.write(get_text_for_count_games(cli_args["source_file_name"]) + "\n")
            file.write(get_text_for_decide(cli_args["source_file_name"], cli_args["input_year"]) + "\n")
            file.write(get_text_for_latest_title(cli_args["source_file_name"]) + "\n")
            file.write(get_text_for_count_by_genre(cli_args["source_file_name"], cli_args["input_genre"]) + "\n")
            file.write(get_text_for_line_number_by_title(cli_args["source_file_name"], ["input_title"]) + "\n")
            file.write(get_text_for_sorted_titles(cli_args["source_file_name"]) + "\n")
            file.write(get_text_for_sorted_genres(cli_args["source_file_name"]) + "\n")
            file.write(get_text_for_year_of_top_sold_fps(cli_args["source_file_name"]) + "\n")
    except FileNotFoundError:
        print("The data file is not found.")
        exit()


if __name__ == "__main__":
    main()
