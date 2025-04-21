# Used to catch 3 testifies in a row
flag = False

def main():
    # List used to hold data from the file
    choices = []
    # Reading the data from the file and appending it to the list
    with open('moves.txt', 'r') as infile:
        line = infile.readline()
        while line != "":
            choices.append(line.rstrip('\n'))
            line = infile.readline()

    # List to hold friends choice
    updated_choices = []

    # Total amount of years and move history variables
    total_my_years = 0
    total_friends_years = 0
    my_moves = ""
    friends_moves = ""

    # Loop through each of the items in the file and perform these actions
    for item in range(0, len(choices)):
        # Each individual round move based on friends move
        my_move = three_chances_dilemma(updated_choices)
        # Update my move history list with my current move
        my_moves += my_move
        # Store the individual move
        friends_move = choices[item]
        # Update the friends move history list with the current move
        friends_moves += friends_move
        # Each the current move to the updated_choices list so my move can be based on my friends move history
        updated_choices.append(friends_move)
        # Storing the return of the years function into my years and friends years
        my_years, friends_years = years(my_move, friends_move)
        # Calculating the total years received
        total_my_years += my_years
        total_friends_years += friends_years

        print(f"""
        ---------------------------------
        My History: 
            {my_moves}
        
        
        Friends History: 
            {friends_moves}
        
        I {my_move} and got {my_years}. Friend {friends_move} and got {friends_years}.
        My total: {total_my_years} years
        Friends total: {total_friends_years} years
        """)

# NAME: Jordan Duff
# DESC: Copy friend, unless friend testifies 3x in a row.
# STRATEGY: Hold out on first round then copy friends choice until friend has testified 3x in a row.
#           If friend testifies 3x in a row, testify indefinitely.


def three_chances_dilemma(friends_choices):
    # Global variable used to indicate friend has testified 3x in a row
    global flag
    # Total testifies in a row count
    t_row_count = 0

    # If there are at least 3 items in the list...
    if len(friends_choices) >= 3:
        # Store the last three items by slicing the list...
        last_three_moves = friends_choices[-3:]
        # Loop to see if all the items are "T"...
        for item in last_three_moves:
            # If so add 1 to t_row_count
            if item == "T":
                t_row_count += 1
    # Hold out first
    if len(friends_choices) == 0:
        return "H"
    # If friend testifies 3x in a row, set the flag
    if t_row_count == 3:
        flag = True
    # If the flag is set, testify indefinitely otherwise copy friends choice which is the last item in the friends_choice list
    if flag == True:
        return "T"
    else:
        return friends_choices[-1]

# Function to return years
def years(my_choice, friends_choice):
    if my_choice == "T" and friends_choice == "T":
        return 4, 4

    if my_choice == "T" and friends_choice == "H":
        return 0, 5

    if my_choice == "H" and friends_choice == "T":
        return 5, 0

    if my_choice == "H" and friends_choice == "H":
        return 2, 2



if __name__ == "__main__":
    main()

