from collections import Counter

name_list =['john','johnny','jackie','johnny','john','jackie','jamie','jamie','john'] 
name_list_sorted = sorted(name_list) #list is sorted in alphabetical order

def winner(name_list_of_people):
    '''
    1) Counter is changed to dictionary since Counter is an unordered Collection
    2) dictionary is changed into alphabetically sorted List with highest vote
    3) first element of sorted list is the winner
    4) If we have the name of winner , we can get the winner votes from dictionary
    '''
    people_vote_count = Counter(name_list_of_people)
    # print(people_vote_count)
    print("------------------")
    print("Vote Count of people: ", people_vote_count)
    print("------------------")
    
    votes_in_dictionary = dict(people_vote_count) # 1
    print(votes_in_dictionary)
    sorting_dict_to_list = sorted(votes_in_dictionary, key=votes_in_dictionary.get, reverse=True) #2
    print(sorting_dict_to_list)
    winner_name = sorting_dict_to_list[0] #3
    winner_vote = votes_in_dictionary.get(sorting_dict_to_list[0]) #4
    print("The winner is {winner_name} with total {winner_vote} votes".format(winner_name = winner_name, winner_vote = winner_vote) )

winner(name_list_sorted)   

