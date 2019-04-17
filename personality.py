# Get the mode of interaction from the user
# Params: none
# Returns: an integer indicating one of reward, punish, joke, or threaten

import random

def introduction():
    print("Hey, I'm an AI!")
    print("Right now I'm feeling...")

def ending():
    print("Nice chatting...")
    print("Until next time!")

def primaryLoop():
    currEmotion = 0
    while True:
        userAction = getInteraction()
        if userAction == 4:
            ending()
        currEmotion = lookupEmotion(currEmotion, userAction)
        showEmotion(currEmotion, userAction)

def getInteraction():
    userAction = int(input("Specify an action(0-Reward, 1-Punish, 2-Threaten, 3-Joke, 4-Quit):"))# TODO prompt user to choose an action
    return userAction # return a corresponding integer

# Based on a given emotion and action, determine the next emotional state
# Params:
# currEmotion - a current emotion
# userAction - a user interaction
# Returns: an emotion

def lookupEmotion(currEmotion, userAction):
    emotionMatrix = [[3,0,2,5,3,3], # TODO do the matrix lookup
                     [0,1,4,4,1,4],
                     [1,0,2,2,2,2],
                     [1,0,1,3,3,3]]
    return emotionMatrix[userAction][currEmotion] # return an integer corresponding to an emotion

def showEmotion(currEmotion, userAction):
        response = [["Anger 1","Anger 2","Anger 3"],
                    ["Disgust 1","Disgust 2","Disgust 3"],
                    ["Fear 1","Fear 2","Fear 3"],
                    ["Happiness 1","Happiness 2","Happiness 3"],
                    ["Sadness 1","Sadness 2","Sadness 3"],
                    ["Surprised 1", "Surprised 2","Surprised 3"]]
        print(random.choice(response[currEmotion]))
    
def main():
    introduction()
    primaryLoop()

main()
