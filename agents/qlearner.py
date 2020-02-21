from player import Player
import numpy as np
import os
import pickle
from datetime import datetime

class QLearningPlayer(Player):
    """ 
    Clase para implementar al jugador QLearner. Usa Reinforcement Learning iterativo.
    """
    
    INITIALQVALUE = 0.5 # Valor con el que se inicializan los Q-values
    
    def __init__(self, name, lr=0.4, df=0.8, Qfile=None):
        super().__init__(name)
        self.lr = lr # learning rate
        self.df = df # discount factor
        self.numQUpdated = 0 # Dato para la obtención de métricas. Número de valores de Q actualizados tras aplicar la ecuación de Bellman
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
        Función softmax para convertir una lista de valores numéricos en una distribución de probabilidad.
        PARAMETER:
            x: lista de valores numéricos.
        RETURN:
            players: Distribución de probabilidad. Los valores devueltos están comprendidos entre 0 y 1 y la suma de todos ellos es 1.
        """
        
        obtiene una distribución de probabilidad, de forma que los valores están  comprendidos entre 0 y 1 y la suma de todos ellos es 1.
        
        return np.exp(x) / np.sum(np.exp(x), axis=0)
    
    
    def setQ(self, state, action, qValue=INITIALQVALUE):
        """
        Función que inicializa todos los Q-values con INITIALQVALUE y se actualizan los Q-values existentes tras aplicarles la ecuación de Bellman.
        PARAMETERS:
            state, action: clave de Q(state, action)
            qValue: valor que se le asigna a Q. Por defecto INITIALQVALUE.
        RETURN:
            qValue: valor que se le ha asignado a Q.
        """
        # 
        qPrevValue = self.getQ(state, action)
        if not qPrevValue: # Nuevo Q-value
            self.q[state, tuple(action)] = qValue
            return qValue
        elif qPrevValue == self.INITIALQVALUE: # Se actualiza Q existente con el valor obtenido de la ecuación de Bellman
            self.q[state, tuple(action)] = qValue
            self.numQUpdated += 1
            return qValue
        elif qValue == self.INITIALQVALUE: # Se intenta inicializar pero ya tenía un valor. Prevalece en Q el valor que tenía anteriormente
            return qPrevValue
        else: # Se actualiza Q existente con el valor obtenido de la ecuación de Bellman
            self.q[state, tuple(action)] = qValue
            return qValue


    def getQ(self, state, action):
        """
        Función que obtiene un Q-value.
        PARAMETERS:
            state, action: clave del Q-value.
        RETURN:
            Valor de Q(state, action).
        """

        return self.q.get((state, tuple(action)))
    
    
    def getMove(self, gameState, train=True, *args, **kwargs):
        """
        Función que juega el turno del agente QLearner. Obtiene todas las acciones que el agente puede realizar y ejecuta la mejor de ellas.
        PARAMETERS:
            gameState: estado actual del juego.
            train: True --> Se trata de un entrenamiento. Se ejecuta en modo exploración.
                   False --> Se ejecuta en modo explotación.
        """
        
        if gameState.gameOver:
            otherPlayer = [p for p in gameState.players if p.name != 'QLearner'][0]
            reward = gameState.finalPointCount(self)[0] - gameState.finalPointCount(otherPlayer)[0]
            i = 0
            for log in self.game_log[::-1]:
                if i == 0:
                    self.nextState = '0'
                    self.nextAction = '0'
                # Ecuación de Bellman
                bellman = (1 - self.lr) * self.getQ(log[0], log[1]) + self.lr * (reward + self.df * self.getQ(self.nextState, self.nextAction))
                self.setQ(log[0], log[1], bellman)
                i += 1
                self.nextState = log[0]
                self.nextAction = log[1]
                
            gameState.endProperly = True
            self.game_log = []
            
        else:
            state = gameState.getState(self)
            possibleActions =  gameState.getActions(self)
            qValues = [self.setQ(state, a) for a in possibleActions]

            if train: # Exploración
                softQValues = self.softmax(qValues) # Se ponderan los Q-values. Valores entre 0 y 1 y cuya suma es 1.
                action = possibleActions[int(np.random.choice(len(possibleActions), p=softQValues))]
            else: # Explotación
                maxQ = max(qValues)
                if qValues.count(maxQ) > 1: # Si existe una acción con el valor máximo se escoge una aleatoriamente
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
        Función que guarda la Q-table en un fichero .pkl.
        """
        
        file_name = datetime.now().strftime('qtable_%Y_%m_%d_%H_%M.pkl')  # fichero .pkl para almecenar la Q-table
        q_dir = 'qfiles'
        if not os.path.exists(q_dir):
            os.mkdir(q_dir)
        
        print('Se guardan los {} valores de Q en el fichero {}.\n'.format(len(self.q), file_name))
        with open(os.path.join(q_dir, file_name), 'wb') as file:
            pickle.dump(self.q, file)
       
          
    def load_Q(self, file_name):
        """
        Función que carga la Q-table desde un fichero.
        PARAMETER:
            file_name: fichero.
        RETURN:
            qSaved: Q-table almacenada en el fichero.
        """
        print('Obteniendo valores de Q del fichero {} para el agente QLearner.......'.format(os.path.join('qfiles', file_name)))
        with open(os.path.join('qfiles', file_name), 'rb') as file:
            qSaved = pickle.load(file)
            print('{} valores de Q leídos.'.format(len(qSaved)))
        return qSaved
        
        