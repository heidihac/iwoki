from player import Player
import numpy as np
import os
import pickle
import random
from datetime import datetime

class QLearningPlayer(Player):
    """ 
    Class to implement the QLearner player, by means of iterative Reinforcement Learning.
    """
    
    INITIAL_QVALUE = 0.5 # Initialization value of the Q-values
    EXPLORATION_RATE = 0.15 # Percentage in which the actions are executed in exploration mode. In exploitation mode: 1 - EXPLORATION_RATE
    LR = 0.4 # Learning Rate
    DF = 0.15 # Discount Factor
    
    def __init__(self, name, Qfile=None):
        super().__init__(name)
        self.numQUpdated = 0 # For metrics. Number of updated Q-values after applying the Bellman equation
        self.game_log = []
        self.nextState = '0'
        self.nextAction = '0'
        
        self.Qfile = Qfile
        if self.Qfile != None:
            self.q = self.load_Q(self.Qfile)
        else:
            self.q = {} # (state, action)
        
        self.setQ('0', '0', 0)
    
    
    def softmax(self, x):
        """
        Softmax function to convert a list of numerical values into a probability distribution.
        PARAMETER:
            x: list of numerical values.
        RETURN:
            players: Probability distribution. The returned values are between 0 and 1 and the sum of all of them is 1.
        """
        
        return np.exp(x) / np.sum(np.exp(x), axis=0)
    
    
    def setQ(self, state, action, qValue=INITIAL_QVALUE):
        """
        Function that initializes all Q-values with INITIAL_QVALUE and updates the existing Q-values after applying the Bellman equation to them
        PARAMETERS:
            state, action: Q(state, action) key.
            qValue: value assigned to Q. By default INITIAL_QVALUE.
        RETURN:
            qValue: value assigned to Q.
        """
        qPrevValue = self.getQ(state, action)
        if not qPrevValue: # New Q-value
            self.q[state, tuple(action)] = qValue
            return qValue
        elif qPrevValue == self.INITIAL_QVALUE: # Existing Q is updated with the value obtained from the Bellman equation
            self.q[state, tuple(action)] = qValue
            self.numQUpdated += 1
            return qValue
        elif qValue == self.INITIAL_QVALUE: # While initializing, it already had a value, which remains in Q
            return qPrevValue
        else: # Existing Q is updated with the value obtained from the Bellman equation
            self.q[state, tuple(action)] = qValue
            return qValue


    def getQ(self, state, action):
        """
        Function that gets a Q-value.
        PARAMETERS:
            state, action: Q-value key.
        RETURN:
            Value of Q(state, action).
        """

        return self.q.get((state, tuple(action)))
    

    def getMove(self, gameState, *args, **kwargs):
        """
        Function that plays the turn of Agent QLearner. It gets all the actions that the agent can do and executes the best one.
        PARAMETERS:
            gameState: current game state.
        """
        
        if gameState.gameOver or len(self.game_log) == 4:
            otherPlayer = [p for p in gameState.players if p.name != 'QLearner'][0]
            reward = gameState.finalPointTally(self)[0] - gameState.finalPointTally(otherPlayer)[0]
            i = 0
            for log in self.game_log[::-1]:
                if i == 0:
                    self.nextState = '0'
                    self.nextAction = '0'
                # Bellman equation
                bellman = (1 - self.LR) * self.getQ(log[0], log[1]) + self.LR * (reward + self.DF * self.getQ(self.nextState, self.nextAction))
                self.setQ(log[0], log[1], bellman)
                i += 1
                self.nextState = log[0]
                self.nextAction = log[1]
            
            self.game_log = []
            if gameState.gameOver:
                gameState.endProperly = True
        else:
            state = gameState.getState(self)
            possibleActions =  gameState.getActions(self)
            qValues = [self.setQ(state, a) for a in possibleActions]

            if random.random() <= self.EXPLORATION_RATE: # Exploration
                softQValues = self.softmax(qValues) # The Q-values are weighted. Values between 0 and 1 and whose sum is 1.
                action = possibleActions[int(np.random.choice(len(possibleActions), p=softQValues))]
            else: # Exploitation
                maxQ = max(qValues)
                if qValues.count(maxQ) > 1: # If there is more than one action with the maximum value, one is chosen randomly.
                    bestOptions = [i for i in range(len(possibleActions)) if qValues[i] == maxQ]
                    i = np.random.choice(bestOptions)
                else:
                    i = qValues.index(maxQ)
                action = possibleActions[i]
            gameState.move(action, self)
            if not gameState.gameOver:
                self.game_log = self.game_log + [(state, action)]
            
            gameState.changeTurn(self)
                
                
    def save_Q(self):
        """
        Function that saves the Q-table in a .pkl file.
        """
        
        file_name = datetime.now().strftime('qtable_%Y_%m_%d_%H_%M.pkl')  # .pkl file to store the Q-table
        q_dir = 'qfiles'
        if not os.path.exists(q_dir):
            os.mkdir(q_dir)
        
        print('The {} Q-values are stored in the file {}.\n'.format(len(self.q), file_name))
        with open(os.path.join(q_dir, file_name), 'wb') as file:
            pickle.dump(self.q, file)

        return None
       
          
    def load_Q(self, file_name):
        """
        Function that loads the Q-table from a file.
        PARAMETER:
            file_name: file.
        RETURN:
            qSaved: Q-table stored in the file.
        """
        print('Getting Q values from the file {} for Agent QLearner.......'.format(os.path.join('qfiles', file_name)))
        with open(os.path.join('qfiles', file_name), 'rb') as file:
            qSaved = pickle.load(file)
            print('{} Q-values read.'.format(len(qSaved)))
        return qSaved
        
        