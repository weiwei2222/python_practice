from typing import Tuple, Any

print("What would you like for dinner? 1,Chinese food  2,Salad  3,Ice cream")
dinner = 0

while dinner not in [1, 2, 3]:
    try:
        dinner = int(input("Please choose which one? Please input 1,2 or 3 !"))
        if dinner not in [1, 2, 3]:
            print("You only can chose 1,2 or 3.")
    except ValueError:
        print("You only can chose 1,2 or 3.")


if dinner == 1:
    chose = "Chinese food! good choose!"
elif dinner == 2:
    chose = "Salad! good for your health"
elif dinner == 3:
    chose = "No, don't even think about!"


print(chose)
