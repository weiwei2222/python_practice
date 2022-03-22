from typing import Tuple, Any
import re
print("What would you like for dinner? 1,Chinese food  2,Salad  3,Ice cream")
# dinner = 0
#
# while dinner not in [1, 2, 3]:
#     try:
#         dinner = int(input("Please choose which one? Please input 1,2 or 3 !"))
#         if dinner not in [1, 2, 3]:
#             print("You only can chose 1,2 or 3.")
#     except ValueError:
#         print("You only can chose 1,2 or 3.")


def choose_dinner():
    dinner = input("Please choose which one? Please input 1,2 or 3 !")
    if not re.match(r'^[123]$', dinner):
        print('You can only choose 1, 2, or 3.')
        return choose_dinner()
    else:
        return int(dinner)


dinner = choose_dinner()

if dinner == 1:
    chose = "Chinese food! good choose!"
elif dinner == 2:
    chose = "Salad! good for your health"
elif dinner == 3:
    chose = "No, don't even think about!"


print(chose)
