# Get the mode of interaction from the user
# Params: none
# Returns: an integer indicating one of reward, punish, joke, or threaten

def introduction():
    print("Hey, I'm an AI and I'm feeling happy!")

def primaryLoop():
    currEmotion = 3
    while True:
        userAction = getInteraction()
        if userAction == 6:
            break
        currEmotion = lookupEmotion(currEmotion, userAction)
        showEmotion(currEmotion, userAction)

def getInteraction():
    userAction = int(input("Specify an action(0-Reward, 1-Punish, 2-Threaten, 3-Joke, 5-Quit):"))# TODO prompt user to choose an action
    return userAction # return a corresponding integer

# Based on a given emotion and action, determine the next emotional state
# Params:
# currEmotion - a current emotion
# userAction - a user interaction
# Returns: an emotion

def lookupEmotion(currEmotion, userAction):
    emotionMatrix = [[0,2,3,1,5,4], # Change all of this
                     [1,3,0,1,1,2],
                     [1,2,4,5,3,2],
                     [2,3,4,5,1,0]] # TODO do the matrix lookup
    return emotionMatrix[userAction][currEmotion] # return an integer corresponding to an emotion

def showEmotion(currEmotion, userAction):
    responses = ["Anger","Disgust","Fear","Happiness","Sadness","Surprised"]
    print(responses[currEmotion])

def main():
    introduction()
    primaryLoop()
    #ending()

main()
