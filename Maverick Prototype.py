#!/usr/bin/env python
# coding: utf-8

# # WELCOME TO MAVERICK
# # AN INTERACTIVE RPG THAT GIVES THE USER A THRILLING EXPERIENCE.
# # DO LEAVE US A FEEDBACK;)

# In[ ]:


name = input("Type your name: ")
print("Welcome", name, "on this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ")

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

    if answer == "swim":
        print("You swam acrross and the current flowed you to the shore. where you met a girl, whom you fell inn love with and then married and lived at the island with her until you died by slipping on the soap while taking a shower at 21.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. Start Again.')

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the stanger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended, they smack you in the head with a big rock, You died.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for playing", name)



# In[ ]:





# In[ ]:





# In[ ]:




