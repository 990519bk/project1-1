import random
def misty_forest():
    player_position = 0
    zombie_positon = -5
    goal = 30
    items = ["torch","compas","pitfall","windstorm"]
    torch_position = random.choice(3,25)
    compass_positon = random.choice(5,35)
    pitfall_positon = random.choice(10,39)
    windstorm_positon = random.choice(15,39)
     
    print("Escape from the Misty Forest")
    print("You will: avoid zombies and reach the destination")
    print("Be sure not to take more than 3 steps at a time!!!")

    while player_position < goal:
          print(f"You position:{player_position}")
          computer_choice = random.choice(["1","2","3"])
          move = input("How many steps are you going to take?")
         
          if move == computer_choice:
               print(f"You walked safely for {move} steps")
               player_position += move
          else:
               print("You have been detained.")
        
          if player_position in items: