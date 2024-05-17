#This dictionary will hold the individual competitors and the events they have entered into.
event_participants = {}

#This dictionary will store the event eligible for individual competitors.
individualevents = {"spelling bee":0,"chess":0,"800m race":0, "javelin":0,"shotput":0}

#This dictionary will store the event eligible for team competitors.
teamevents = {"basketball":0,"tennis":0,"sciencetest":0,"spellingbee":0,"hockey":0}

#This dictionary will hold the scores for team competitors and the events they will participate in.
eventteamparticipants = {}

#This dictionary will hold the teams and their members.
teams = {}

import json

# File paths for data storage
individual_data_file = "individual_data.json"

try:
    with open(individual_data_file, 'r') as f:
        data = json.load(f)
        event_participants = data if isinstance(data, dict) else {}
except FileNotFoundError:
    event_participants = {}

import json
# Global variables
team_data_file = "MEWteam_data.json"
team_members = {}
team_event_scores = {}

def save_individual_data():
    try:
        with open(individual_data_file, 'w') as f:
            json.dump(event_participants, f)
        print("Individual data saved successfully!")
    except Exception as e:
        print("Error occurred while saving individual data:", e)


def load_team_data():
    global team_event_scores
    try:
        with open(team_data_file, 'r') as f:
            team_event_scores = json.load(f)
            print("Team data loaded successfully!")
    except FileNotFoundError:
        print("Team data file not found. Starting with an empty dictionary.")
    except json.JSONDecodeError:
        print("Error decoding team data file. Starting with an empty dictionary.")
        team_event_scores = {}

def save_team_data():
    try:
        with open(team_data_file, 'w') as f:
            json.dump(team_event_scores, f)
        print("Team data saved successfully!")
    except Exception as e:
        print("Error occurred while saving team data:", e)

# Call the function to load team data at the beginning of your script
load_team_data()

# Now you can use team_event_scores dictionary to access the team data throughout your script

# Function to update team scores
def update_team_scores(team_name, event, points):
    if team_name in team_event_scores:
        if event in team_event_scores[team_name]:
            team_event_scores[team_name][event] = points
            save_team_data()  # Save team data after updating scores
            print("Scores updated successfully for team:", team_name)
        else:
            print("Invalid event for the team:", team_name)
    else:
        print("Team not found:", team_name)
#This code will add a indivudal to each event.
def addcompetitor():
    for x in range(3):

    #This will ask if the user is a an indivudal competitor or apart of a team.
        question = input("Are you a indivudal or team: ")
        if question.lower() == "individual":

            #A validation to see if all indivudal spaces are free.
            if len(event_participants) < 20:
                name = input("Enter name: ")
                event_participants[name]= {}

                #This gives the user the option to enter in one event.
                question = input("Do you want to enter in one event only? ")
                if question.lower()=="yes":

                    #This will inform the user of the events.
                    print("The events are:")
                    for y in individualevents:
                        print(y)
                    event = input("Enter event you want to enter :")
                    if event.lower() in individualevents:
                        event_participants[name] = {event.lower():0}
                        print("Thank you for registering!")
                        return event_participants

                        break
                    else:
                        print("Invalid!")

                #This will automatically enter the indivudal in all events.
                elif question.lower()=="no":
                    event_participants[name] = individualevents
                    return event_participants
                    break
                else:
                    print("Invalid!")
            else:
                print("Sorry but all individual spaces have been filled up.")
                break

        elif question.lower() == "team":
            num_members = int(input("Enter number of team members (must be 5): "))
            if num_members == 5:
                team_name = input("Enter team name: ")
                if team_name not in team_members:  # Check if team already exists
                    team_members[team_name] = []
                    team_event_scores[team_name] = {event: 0 for event in teamevents}
                    for i in range(1, 6):
                        member_name = input(f"Enter team member {i}: ")
                        team_members[team_name].append(member_name)  # Add the member to the team's list of members
                    save_team_data()  # Save team data after registration
                else:
                    print("Team name already exists!")
            else:
                print("You must have exactly five members.")
            break
        else:
            print("Invalid input!")


#Function to add points.
def addpoints():
    for x in range(3):
        question = input("Do you want to enter points for team or individual: ")
        if question.lower() == "individual":
            username = input("Enter individual name: ")
            if username in event_participants:
                print("Events for individuals are:")
                for event in event_participants[username]:
                    print(event)
                event = input("Enter event you want to enter points to: ")
                if event.lower() in event_participants[username]:
                    points = int(input("Enter points for " + event.lower() + ": "))
                    event_participants[username][event.lower()] = points
                    save_individual_data()  # Save individual data after adding points
                    print("Points added successfully for individual:", username)
                    return
                else:
                    print("Invalid event!")
            else:
                print("Individual not found!")
        elif question.lower() == "team":
            team_name = input("Enter team name: ")
            if team_name in team_event_scores:  # Check if team already exists
                for event in teamevents:
                    print(event)
                event = input("Enter event you want to enter points for: ")
                if event in teamevents:
                    points = int(input("Enter points for " + event + ": "))
                    update_team_scores(team_name, event, points)  # Call the function to update team scores
                    break
                else:
                    print("Invalid event!")
            else:
                print("Team not found!")
        else:
            print("Invalid!")







def leaderboard():
    for x in range(3):
        question = input("Do you want to see the leaderboard for team or individual: ")

        if question.lower() == 'individual':
            # Create a 2D array to store individual names and their scores
            individual_scores = []

            # Iterate over event participants and populate the 2D array
            for competitor, scores in event_participants.items():
                # Check if scores is None or empty
                if scores is None or not scores:
                    continue

                total_score = sum(scores.values())  # Calculate total score for the competitor
                individual_scores.append([competitor, total_score])  # Add competitor and total score to the array

            # Sort the array based on total scores
            individual_scores.sort(key=lambda x: x[1], reverse=True)

            # Display top 3 ranked individuals
            print("Top 3 Ranked Individuals:")
            for i, (competitor, total_score) in enumerate(individual_scores[:3], start=1):
                print(f"{i}. {competitor}: {total_score} points")

            break  # Exit the loop after displaying the leaderboard
        elif question.lower() == 'team':
            # Call the existing function to display the top 3 teams
            display_top_3_teams()
            break
        elif question.lower() == "team":
            # Dictionary to store total scores for each team
            total_points_team = {}

            # Iterate over events
            for event in teamevents:
                # Iterate over teams and calculate total score for the event
                for team_name, scores in team_event_scores.items():
                    if event in scores:
                        total_points_team.setdefault(team_name, 0)
                        total_points_team[team_name] += scores[event]

            # Sort teams based on total scores
            sorted_teams = sorted(total_points_team.items(), key=lambda x: x[1], reverse=True)

            # Display top 3 teams
            print("Top 3 Teams:")
            for i, (team_name, total_score) in enumerate(sorted_teams[:3], start=1):
                print(f"{i}. {team_name}: {total_score} points")
            break
        else:
            print("Invalid input!")

#The variable "loginsystem" will store the username and passwords of admins.
loginsystem = {"Abdi123":"123&sgH","Patty456":"456£Sac","Patrick789":"789#Asd","Kelly912":"912fGh"}

#The for loop will allows three for data entry.
for y in range(3):

#The variables "password" and "username" will be used to input the data entry details.
    username = input("Enter username: ")
    password = input("Enter password: ")

#The code validates that the username & password.
    print("Main menu:")
    if username in loginsystem and loginsystem[username] == password:

        option = 0
        while option != 4:
            print("Welcome back " + username + "!")
            print("Enter 1 to add a comptitor.")
            print("Enter 2 to add scores for a competitor.")
            print("Enter 3 to display leaderboard: ")
            print("Enter 4 to quit scoring system.")
            option = int(input("Enter number: "))
            if option == 1:
                addcompetitor()
            elif option == 2:
                addpoints()
            elif option == 3:
                leaderboard()
            else:
                print("You have now existed the scoring system.")
        break
    else:
        print("Invalid!")
