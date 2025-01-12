from file_utils import create_list_from_file, merge_price_and_prediction_files, read_team_members_from_file
from best_team_finder import determine_best_team

constructor_prediction_path = "./src/data/constructor-prediction.txt"
driver_prediction_path = "./src/data/driver-prediction.txt"

constructor_price_path = "./src/data/constructor-price.txt"
driver_price_path = "./src/data/driver-price.txt"

driver_path = "./src/data/driver.txt"
constructor_path = "./src/data/contructor.txt"

previous_team_path = "./src/data/previous_team.txt"

merge_price_and_prediction_files(constructor_prediction_path, constructor_price_path, constructor_path)
merge_price_and_prediction_files(driver_prediction_path, driver_price_path, driver_path)

drivers = read_team_members_from_file(driver_path)
constructors = read_team_members_from_file(constructor_path)
previous_team_names = create_list_from_file(previous_team_path)

determine_best_team(drivers, constructors, 100, previous_team_names, 2)