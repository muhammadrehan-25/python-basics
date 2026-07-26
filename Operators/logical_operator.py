# ========== Logical operator ==========

#Q1:Create two variables:
# Print whether the person can drive.

"""age = 20
has_license=True

print("Person can drive:",age and has_license)"""


#Q2:Check if a number is between 1 and 100.
"""
number=57
print(number>1 and number<100)"""

#Q3:Check if today is Saturday or Sunday.

"""today="Saturday"
print(today=="Saturday" or today== "Sunday")"""

#Q4:Use not with a boolean variable.

"""have_bananas=True
print(not have_bananas)"""

#Q5:Create three boolean variables and combine them using and and or

"""has_license=True
can_drive_truck=False
drive_car=True

print(has_license and drive_car or  can_drive_truck )"""

#Challenge 1

"""A student passes only if:

Marks ≥ 50
Attendance ≥ 75

Print the result

marks=87
Attendance=82

pass_if=(marks>=50 and Attendance>=75)
print(pass_if)"""

#Challenge 2

"""A website allows login if:

Email is correct or
Phone number is correct.

Represent this with boolean variables.

email_is_correct=True
phone_number_correct=True

login=(email_is_correct or phone_number_correct)
print(login)"""

#Challenge 3

"""A game starts only if:

Player is online.
Player has enough coins.
Player selected a character.

Use logical operators to determine if the game can start.

is_online=True
has_enough_coins=True
selected_a_player=True

game_start=(is_online and has_enough_coins) and selected_a_player

print(game_start)"""