from team_utils import NUMBER_OF_DRIVERS, NUMBER_OF_CONSTRUCTORS, Team
from itertools import combinations

def determine_best_team(
        drivers, 
        constructors, 
        budget: float, 
        previous_team_names,
        free_transfers: int
        ):

    drivers_combos = list(combinations(drivers, NUMBER_OF_DRIVERS))
    constructors_combos = list(combinations(constructors, NUMBER_OF_CONSTRUCTORS))

    best_team = Team([], [], 0)
    for drivers_combo in drivers_combos:
        for constructors_combo in constructors_combos:
            current_team = Team(drivers_combo.__add__(constructors_combo), previous_team_names, free_transfers)
            if budget < current_team.total_price:
                continue

            if current_team.total_points > best_team.total_points:
                best_team = current_team

    print(f"best team: \n{best_team}")
    return best_team