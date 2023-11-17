import requests
import pandas as pd
import os
import csv
import time

def create_csv(name):
        """this method creates a template csv file by creating a pandas dataframe with 
        each column for result data and appends 'empty' lists so that pandas create the
        template file without raising an error"""

        new_data = pd.DataFrame({'home_team_name':[],'away_team_name':[],'HT_score':[],
        'AT_score':[],'date':[],'HT_couch_name':[],'AT_couch_name':[],'HT_substitues_names':[],      
        'AT_substitues_names':[],'HT_ball_possesion':[],'AT_ball_possesion':[],'HT_Expected_goals_xG':[],    
        'AT_Expected_goals_xG':[],'HT_Total_Shots': [],'AT_Total_Shots': [],'HT_Shots_on_target':[],        
        'AT_Shots_on_target':[],'HT_Big_chances':[],'AT_Big_chances':[],'HT_Big_chances_missed':[],  
        'AT_Big_chances_missed':[],'HT_Accurate_passes':[],'HT_Accurate_passes_per':[],
        'AT_Accurate_passes':[],'AT_Accurate_passes_per':[],'HT_Fouls_committed':[],
        'AT_Fouls_committed':[],'HT_Corners':[],'AT_Corners':[],'HT_Shots_off_target':[],
        'AT_Shots_off_target':[],'HT_Blocked_shots':[],'AT_Blocked_shots':[],'HT_Hit_woodwork':[],
        'AT_Hit_woodwork':[],'HT_Shots_inside_box':[],'AT_Shots_inside_box':[],'HT_Shots_outside_box':[],
        'AT_Shots_outside_box':[],'HT_xG_open_play':[],'AT_xG_open_play':[],'HT_xG_set_play':[],
        'AT_xG_set_play':[],'HT_Non_penalty_xG':[],'AT_Non_penalty_xG':[],'HT_xG_on_target_xGOT':[],
        'AT_xG_on_target_xGOT':[],'HT_Own_half':[],'AT_Own_half':[],'HT_Opposition_half':[],
        'AT_Opposition_half':[],'HT_Accurate_long_balls':[],'HT_Accurate_long_balls_per':[],
        'AT_Accurate_long_balls':[],'AT_Accurate_long_balls_per':[],'HT_Accurate_crosses':[],
        'HT_Accurate_crosses_per':[],'AT_Accurate_crosses':[],'AT_Accurate_crosses_per':[],'HT_Throws':[],
        'AT_Throws':[],'HT_Touches_in_opposition_box':[],'AT_Touches_in_opposition_box':[],'HT_Offsides':[],
        'AT_Offsides':[],'HT_Yellow_cards':[],'AT_Yellow_cards':[],'HT_Red_cards':[],'AT_Red_cards':[],
        'HT_Tackles_won':[],'HT_Tackles_won_per':[],'AT_Tackles_won':[],'AT_Tackles_won_per':[],
        'HT_Interceptions':[],'AT_Interceptions':[],'HT_Blocks':[],'AT_Blocks':[],'HT_Clearances':[],
        'AT_Clearances':[],'HT_Keeper_saves':[],'AT_Keeper_saves':[],'HT_Duels_won':[],
        'AT_Duels_won':[],'HT_Ground_duels_won':[],'HT_Ground_duels_won_per':[],'AT_Ground_duels_won':[],
        'AT_Ground_duels_won_per':[],'HT_Aerial_duels_won':[],'HT_Aerial_duels_won_per':[],
        'AT_Aerial_duels_won':[],'AT_Aerial_duels_won_per':[],'HT_Successful_dribbles':[],
        'HT_Successful_dribbles_per':[],'AT_Successful_dribbles':[],'AT_Successful_dribbles_per':[]})
        new_data.to_csv(f"{name}.csv",index=False)

def details(url,file_name):
    home_team_name,away_team_name,HT_score,AT_score,date,HT_coach_name,AT_coach_name = " "," "," "," "," "," "," "
    HT_substitutes_names,AT_substitutes_names,HT_ball_possession,AT_ball_possession,HT_Expected_goals_xG = " "," "," "," "," "
    AT_Expected_goals_xG,HT_Total_shots,AT_Total_shots,HT_Shots_on_target,AT_Shots_on_target = " "," "," "," "," "
    HT_Big_chances,AT_Big_chances,HT_Big_chances_missed,AT_Big_chances_missed,HT_Accurate_passes, = " "," "," "," "," "
    HT_Accurate_passes_per,AT_Accurate_passes,AT_Accurate_passes_per,HT_Fouls_committed, = " "," "," "," "
    AT_Fouls_committed,HT_Corners,AT_Corners,HT_Shots_off_target,AT_Shots_off_target, = " "," "," "," "," "
    HT_Blocked_shots,AT_Blocked_shots,HT_Hit_woodwork,AT_Hit_woodwork,HT_Shots_inside_box = " "," "," "," "," "
    AT_Shots_inside_box,HT_Shots_outside_box,AT_Shots_outside_box,HT_xG_open_play,AT_xG_open_play, = " "," "," "," "," "
    HT_xG_set_play,AT_xG_set_play,HT_Non_penalty_xG,AT_Non_penalty_xG,HT_xG_on_target_xGOT = " "," "," "," "," "
    AT_xG_on_target_xGOT,HT_Own_half,AT_Own_half,HT_Opposition_half,AT_Opposition_half = " "," "," "," "," "
    HT_Accurate_crosses,HT_Accurate_crosses_per,AT_Accurate_crosses,AT_Accurate_crosses_per = " "," "," "," "
    HT_Throws,AT_Throws,HT_Touches_in_opposition_box,AT_Touches_in_opposition_box = " "," "," "," "
    HT_Offsides,AT_Offsides,HT_Yellow_cards,AT_Yellow_cards,HT_Red_cards,AT_Red_cards = " "," "," "," "," "," "
    HT_Tackles_won,HT_Tackles_won_per,AT_Tackles_won,AT_Tackles_won_per,HT_Interceptions = " "," "," "," "," "
    AT_Interceptions,HT_Blocks,AT_Blocks,HT_Clearances,AT_Clearances,HT_Keeper_saves = " "," "," "," "," "," "
    AT_Keeper_saves,HT_Duels_won,AT_Duels_won,HT_Ground_duels_won,HT_Ground_duels_won_per = " "," "," "," "," "
    AT_Ground_duels_won,AT_Ground_duels_won_per,HT_Aerial_duels_won,HT_Aerial_duels_won_per = " "," "," "," "
    AT_Aerial_duels_won,AT_Aerial_duels_won_per,HT_Successful_dribbles,HT_Successful_dribbles_per = " "," "," "," "
    AT_Successful_dribbles,AT_Successful_dribbles_per = " "," "
    HT_Accurate_long_balls , HT_Accurate_long_balls_per = " "," "
    AT_Accurate_long_balls , AT_Accurate_long_balls_per =" "," "


    match_id = url.split("#")[1]
    response = requests.get(f"https://www.fotmob.com/api/matchDetails?matchId={match_id}")
    if response.status_code == 200:
        data = response.json()
    else:
        raise "response is unavailable to fetch : response code is not <200>"
        

    # names, score, and date
    
    # name and score

    # HOME TEAM
    teams = data["header"]["teams"]
    home_team_name  = teams[0]["name"]
    HT_score = teams[0]["score"]

    # AWAY TEAM
    away_team_name  = teams[1]["name"]
    AT_score = teams[1]["score"]
    
    # date
    date_value = data["header"]["status"]["utcTime"]
    date = date_value.split("T")[0]

    try:
        # coaches
        coaches = data["content"]["lineup"]["coaches"]["coachesArr"]
    
        # HT coach
        HT_coach_name = coaches[0][0]["name"]["fullName"]
        
        # AT coach
        AT_coach_name = coaches[1][0]["name"]["fullName"]
    except:
        pass

    try:
        # HT_substitutes
        HT_substitutes_names = []
        ht_subs_names = data["content"]["lineup"]["lineup"][0]["bench"]
        for i in ht_subs_names:
            HT_substitutes_names.append(i["name"]["fullName"])
        
        # AT_substitutes
        AT_substitutes_names = []
        at_subs_names = data["content"]["lineup"]["lineup"][1]["bench"]
        for i in at_subs_names:
            AT_substitutes_names.append(i["name"]["fullName"])
    except:
        pass
    
    



    # stats
    try:
        stats = data["content"]["stats"]["Periods"]["All"]["stats"]
    except:
        stats = []


    # top states
    for i in stats:
        states = i["stats"]
        for j in states:
            if j["title"] == "Ball possession":
                HT_ball_possession = str(j["stats"][0]) + "%"
                AT_ball_possession = str(j["stats"][1]) + "%"
            
            elif j["title"] == "Expected goals (xG)":
                HT_Expected_goals_xG = j["stats"][0]
                AT_Expected_goals_xG = j["stats"][1]
            
            elif j["title"] == "Total shots":
                HT_Total_shots = j["stats"][0]
                AT_Total_shots = j["stats"][1]
            
            elif j["title"] == "Shots on target":
                HT_Shots_on_target = j["stats"][0]
                AT_Shots_on_target = j["stats"][1]
            
            elif j["title"] == "Big chances":
                HT_Big_chances = j["stats"][0]
                AT_Big_chances = j["stats"][1]

            elif j["title"] == "Big chances missed":
                HT_Big_chances_missed = j["stats"][0]
                AT_Big_chances_missed = j["stats"][1]
            
            elif j["title"] == "Accurate passes":
                HT_Accurate_passes,HT_Accurate_passes_per = j["stats"][0].split(" ")
                AT_Accurate_passes,AT_Accurate_passes_per = j["stats"][1].split(" ")

            elif j["title"] == "Fouls committed":
                HT_Fouls_committed = j["stats"][0]
                AT_Fouls_committed = j["stats"][1]

            elif j["title"] == "Corners":
                HT_Corners = j["stats"][0]
                AT_Corners = j["stats"][1]

            elif j["title"] == "Shots off target":
                HT_Shots_off_target = j["stats"][0]
                AT_Shots_off_target = j["stats"][1]
            
            elif j["title"] == "Blocked shots":
                HT_Blocked_shots = j["stats"][0]
                AT_Blocked_shots = j["stats"][1]

            elif j["title"] == "Hit woodwork":
                HT_Hit_woodwork = j["stats"][0]
                AT_Hit_woodwork = j["stats"][1]

            elif j["title"] == "Shots inside box":
                HT_Shots_inside_box = j["stats"][0]
                AT_Shots_inside_box = j["stats"][1]
            
            elif j["title"] == "Shots outside box":
                HT_Shots_outside_box = j["stats"][0]
                AT_Shots_outside_box = j["stats"][1]


            elif j["title"] == "xG open play":
                HT_xG_open_play = j["stats"][0]
                AT_xG_open_play = j["stats"][1]

            elif j["title"] == "xG set play":
                HT_xG_set_play = j["stats"][0]
                AT_xG_set_play = j["stats"][1]

            elif j["title"] == "xG non-penalty":
                HT_Non_penalty_xG = j["stats"][0]
                AT_Non_penalty_xG = j["stats"][1]

            elif j["title"] == "xG on target (xGOT)":
                HT_xG_on_target_xGOT = j["stats"][0]
                AT_xG_on_target_xGOT = j["stats"][1]

            elif j["title"] == "Own half":
                HT_Own_half = j["stats"][0]
                AT_Own_half = j["stats"][1]

            elif j["title"] == "Opposition half":
                HT_Opposition_half = j["stats"][0]
                AT_Opposition_half = j["stats"][1]
            
            elif j["title"] == "Accurate long balls":
                HT_Accurate_long_balls,HT_Accurate_long_balls_per = j["stats"][0].split(" ")
                AT_Accurate_long_balls,AT_Accurate_long_balls_per = j["stats"][1].split(" ")

            elif j["title"] == "Accurate crosses":
                HT_Accurate_crosses,HT_Accurate_crosses_per = j["stats"][0].split(" ")
                AT_Accurate_crosses,AT_Accurate_crosses_per = j["stats"][1].split(" ")

            elif j["title"] == "Throws":
                HT_Throws = j["stats"][0]
                AT_Throws = j["stats"][1]

            elif j["title"] == "Touches in opposition box":
                HT_Touches_in_opposition_box = j["stats"][0]
                AT_Touches_in_opposition_box = j["stats"][1]

            elif j["title"] == "Offsides":
                HT_Offsides = j["stats"][0]
                AT_Offsides = j["stats"][1]
            
            elif j["title"] == "Tackles won":
                HT_Tackles_won,HT_Tackles_won_per = j["stats"][0].split(" ")
                AT_Tackles_won,AT_Tackles_won_per = j["stats"][1].split(" ")

            elif j["title"] == "Interceptions":
                HT_Interceptions = j["stats"][0]
                AT_Interceptions = j["stats"][1]

            elif j["title"] == "Blocks":
                HT_Blocks = j["stats"][0]
                AT_Blocks = j["stats"][1]

            elif j["title"] == "Clearances":
                HT_Clearances = j["stats"][0]
                AT_Clearances = j["stats"][1]

            elif j["title"] == "Keeper saves":
                HT_Keeper_saves = j["stats"][0]
                AT_Keeper_saves = j["stats"][1]

            elif j["title"] == "Duels won":
                HT_Duels_won = j["stats"][0]
                AT_Duels_won = j["stats"][1]

            elif j["title"] == "Ground duels won":
                HT_Ground_duels_won,HT_Ground_duels_won_per = j["stats"][0].split(" ")
                AT_Ground_duels_won,AT_Ground_duels_won_per = j["stats"][1].split(" ")
            
            elif j["title"] == "Aerial duels won":
                HT_Aerial_duels_won,HT_Aerial_duels_won_per = j["stats"][0].split(" ")
                AT_Aerial_duels_won,AT_Aerial_duels_won_per = j["stats"][1].split(" ")

            elif j["title"] == "Successful dribbles":
                HT_Successful_dribbles,HT_Successful_dribbles_per = j["stats"][0].split(" ")
                AT_Successful_dribbles,AT_Successful_dribbles_per = j["stats"][1].split(" ")

            elif j["title"] == "Yellow cards":
                HT_Yellow_cards = j["stats"][0]
                AT_Yellow_cards = j["stats"][1]

            elif j["title"] == "Red cards":
                HT_Red_cards = j["stats"][0]
                AT_Red_cards = j["stats"][1]

    data_to_append = [home_team_name , away_team_name , HT_score , AT_score , date ,
                                HT_coach_name , AT_coach_name , HT_substitutes_names , AT_substitutes_names ,
                                HT_ball_possession , AT_ball_possession , HT_Expected_goals_xG ,
                                AT_Expected_goals_xG , HT_Total_shots , AT_Total_shots , 
                                HT_Shots_on_target , AT_Shots_on_target , HT_Big_chances ,
                                AT_Big_chances , HT_Big_chances_missed , AT_Big_chances_missed , 
                                HT_Accurate_passes , HT_Accurate_passes_per , AT_Accurate_passes , 
                                AT_Accurate_passes_per , HT_Fouls_committed , AT_Fouls_committed , 
                                HT_Corners , AT_Corners , HT_Shots_off_target , AT_Shots_off_target , 
                                HT_Blocked_shots , AT_Blocked_shots , HT_Hit_woodwork , AT_Hit_woodwork , 
                                HT_Shots_inside_box , AT_Shots_inside_box , HT_Shots_outside_box , 
                                AT_Shots_outside_box , HT_xG_open_play , AT_xG_open_play , HT_xG_set_play , 
                                AT_xG_set_play , HT_Non_penalty_xG , AT_Non_penalty_xG , 
                                HT_xG_on_target_xGOT , AT_xG_on_target_xGOT , HT_Own_half , 
                                AT_Own_half , HT_Opposition_half , AT_Opposition_half , 
                                HT_Accurate_long_balls , HT_Accurate_long_balls_per , 
                                AT_Accurate_long_balls , AT_Accurate_long_balls_per , 
                                HT_Accurate_crosses , HT_Accurate_crosses_per , AT_Accurate_crosses , 
                                AT_Accurate_crosses_per , HT_Throws , AT_Throws , 
                                HT_Touches_in_opposition_box , AT_Touches_in_opposition_box , 
                                HT_Offsides , AT_Offsides , HT_Yellow_cards , AT_Yellow_cards , 
                                HT_Red_cards , AT_Red_cards , HT_Tackles_won , HT_Tackles_won_per , 
                                AT_Tackles_won , AT_Tackles_won_per , HT_Interceptions , 
                                AT_Interceptions , HT_Blocks , AT_Blocks , HT_Clearances , 
                                AT_Clearances , HT_Keeper_saves , AT_Keeper_saves , HT_Duels_won ,
                                AT_Duels_won , HT_Ground_duels_won , HT_Ground_duels_won_per ,
                                AT_Ground_duels_won , AT_Ground_duels_won_per , HT_Aerial_duels_won , 
                                HT_Aerial_duels_won_per , AT_Aerial_duels_won , AT_Aerial_duels_won_per ,
                                HT_Successful_dribbles , HT_Successful_dribbles_per , 
                                AT_Successful_dribbles , AT_Successful_dribbles_per]
            
        # checking if file already exists. if it does then append the data, if doesn't then create 
        # new one

    if os.path.exists(f"{file_name}.csv"):
        file = open(f"{file_name}.csv","a",newline="")
        writer = csv.writer(file)
        writer.writerow(data_to_append)
        file.close()
    else:
        create_csv(f"{file_name}")
        file = open(f"{file_name}.csv","a",newline="")
        writer = csv.writer(file)
        writer.writerow(data_to_append)
        file.close()
    
    print("one row is completed!")

def get_links(session,id): 
    links_list = []
    url = f"https://www.fotmob.com/api/leagues?id={id}&ccode3=PAK&season={session[0]}%2F{session[1]}"
    response = requests.get(url)
    data = response.json()
    
    matches = data["matches"]["allMatches"]

    for i in matches:
        links_list.append(i["pageUrl"])

    return links_list

def main_scrap(lis,file_name):
    start = time.time()
    for i in lis:
        details(i,file_name)
    print("this process took : ",time.time() - start," seconds")

session_list = [(2015,2016),
                (2016,2017),
                (2017,2018),
                (2018,2019),
                (2019,2020),
                (2020,2021),
                (2021,2022),
                (2022,2023),
                (2023,2024)]

if __name__ == "__main__":
    league_name = input("enter league name : ")
    id = int(input("enter the id of league : "))
    if league_name == "" or id == "":
        raise "enter the parameters correctly!"

    start = time.time()
    for pos,session in enumerate(session_list):
        link_list = get_links(session,id)
        print(f"{pos} session of {league_name} is done!")
        main_scrap(link_list,f"{league_name} - {session[0]} - {session[1]}")

    print("total time : ",time.time() - start)

