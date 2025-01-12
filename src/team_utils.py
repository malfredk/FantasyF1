from enum import Enum

NUMBER_OF_DRIVERS = 5
NUMBER_OF_CONSTRUCTORS = 2
TEAM_SIZE = 7
TRANSFER_PENALTY_POINTS = -10

class TeamMemberType(Enum):
    DRIVER = 0
    CONSTRUCTOR = 1

class TeamMember:
    def __init__(
            self, 
            name: str, 
            type: TeamMemberType, 
            price: float, 
            points: int
            ):
        self.__name = name
        self.__type = type
        self.__price = price
        self.__points = points

    @property
    def name(self):
        return self.__name
    
    @property
    def type(self):
        return self.__type
    
    @property
    def points(self):
        return self.__points
    
    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"team member: type: {self.__type.name} - name: {self.__name} - price: {self.__price} - points: {self.__points}"
    
    def __eq__(self, other):
        return self.__name == other.__name
    
class Team:
    def __init__(
            self, 
            members, 
            previous_team_names, 
            free_transfers: int
            ):
        self.__members = members
        self.__transfer_count = self.calculate_number_of_transfers(previous_team_names)
        self.__total_points = self.calculate_total_points(free_transfers)
        self.__total_price = self.calculate_total_price()

    @property
    def total_points(self):
        return self.__total_points
    
    @property
    def total_price(self):
        return self.__total_price

    def __str__(self):
        return f"team: total points: {self.total_points} - number of transfers: {self.__transfer_count} - total price: {self.__total_price} - members: \n{',\n'.join(str(member) for member in self.__members)}"

    def calculate_number_of_transfers(self, previous_team_names):
        transfer_count = 0
        for team_member in self.__members:
            if team_member.name in previous_team_names:
                continue
            transfer_count += 1
        return transfer_count

    def calculate_total_points(self, free_transfers: int):
        drivers = list(filter(lambda member: member.type == TeamMemberType.DRIVER, self.__members))
        drs_points = max((driver.points for driver in drivers), default=0)
        return (
            sum(member.points for member in self.__members) 
            + drs_points
            + max(self.__transfer_count - free_transfers, 0) * TRANSFER_PENALTY_POINTS
        )
    
    def calculate_total_price(self):
        return sum(member.price for member in self.__members)