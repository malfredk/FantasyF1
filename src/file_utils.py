from team_utils import TeamMember, TeamMemberType

def read_team_members_from_file(file_path: str):
    team_members = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split(';')
        member_type = TeamMemberType[header[0].upper()]

        for line in lines[1:]:
            name, price, prediction = line.strip().split(';')
            team_member = TeamMember(
                name=name,
                type=member_type,
                price=float(price),
                points=int(prediction)
            )
            team_members.append(team_member)

    return team_members

def create_list_from_file(file_path: str):
    elements = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            element = line.strip()
            elements.append(element)
    return elements

def merge_price_and_prediction_files(prediction_file_path: str, price_file_path: str, merged_file_path: str):
    with open(prediction_file_path, 'r') as prediction_file:
        lines = prediction_file.readlines()
        prediction_data = [line.strip().split(';') for line in lines]
        team_member_type = lines[0].strip().split(';')[0]
    prediction_dict = {line[0]: line[1] for line in prediction_data[1:]}

    with open(price_file_path, 'r') as price_file:
        price_data = [line.strip().split(';') for line in price_file.readlines()]
    price_dict = {line[0]: line[1] for line in price_data[1:]}

    merged_data = [f"{team_member_type};price;prediction"]
    for key in prediction_dict:
        if key in price_dict:
            merged_data.append(f"{key};{price_dict[key]};{prediction_dict[key]}")

    with open(merged_file_path, 'w') as f_out:
        f_out.write('\n'.join(merged_data))