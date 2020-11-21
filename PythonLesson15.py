print('=== Errors handling ===')

import sys

questsForKnights = 0

try:
    quests = 20
    knightsStr = input('How many knights are in the team?\n')
    knights = int(knightsStr)

    questsForKnights = quests/knights

except ValueError as e:
    print('You need to enter an intiger number', e)

except ZeroDivisionError as e:
    print("You need to enter value higher than zero.\nYou can't divide by zero", e)

except:
    print('Something went wrong :-(', sys.exc_info()[0])

print("Every knight should have around", questsForKnights, "quests")