from postprocessor import postprocess
from best_team_finder import determine_best_team

drivers, constructors, previous_team_names = postprocess()
determine_best_team(drivers, constructors, 100, previous_team_names, 2)