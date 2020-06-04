#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import time
from datetime import datetime
from utils import drawPlayersOrder
from initializations import initializeAll
from player import Player
from agents.greedy import GreedyPlayer
from agents.random import RandomPlayer
from agents.qlearner import QLearningPlayer
from agents.minimax import MinimaxPlayer
from agents.human import HumanPlayer

NUM_GAMES = 100 # Number of games
CHECK_POINT = 100 # Number of games to stablish a check point, capturing the general data to inform about the evolution of the games

def playGame(players, gameSpace):
    """  
    Function that controls the turn of the players and ends de game.
    PARAMETERS:
        players: list of players.
        gameSpace.
    """
    while True:
        for player in players:
            if player.isTurn:
                if gameSpace.gameOver:
                    agents[player.name].getMove(gameSpace)
                    if gameSpace.endProperly:
                        return None
                    gameSpace.endProperly = True
                    break
                elif player.name == 'Human':
                    gameSpace.summary()
            
                agents[player.name].getMove(gameSpace)
                player.numTurns += 1
                break


def saveMetrics(file_name, time, games_played, players):
    """ 
    Function that stores and shows general data about the evolution of the games in the check point.
    PARAMETERS:
        file_name: file where the information is stored.
        time: time from previous check point.
        games_played: number of games played from the beginning to the check point.
        players: list of players.
    """
    print('*****************************')
    print('        CHECK POINT')
    print('*****************************')
    mean_time = time / games_played
    print('Games played: {}'.format(games_played))
    print(f'Average of time of the games:{mean_time: .2f}s')
    print('Average of turns used by each player: {}'.format(int(players[0].numTurns / games_played)))
    winsAny = 0
    nonMinimaxScore=0
    for player in players:
        print('Number of games that the agent {} wins: {}'.format(player.name, player.numWins))
        winsAny += player.numWins
        if player.name != 'Minimax':
            nonMinimaxScore += player.accumulatedScore
    print('Number of draws: {}'.format(games_played-winsAny))
    if any([p for p in players if p.name == 'QLearner']):
        print('Number of updated Q-values: {}'.format(agents['QLearner'].numQUpdated))
        print('Number of TOTALS Q-values in the Qfile: {}'.format(len(agents['QLearner'].q)))
    if any([p for p in players if p.name == 'Minimax']):
        print(f'Average of time for Minimax to decide its movement:{(check_time - start_all) / players[0].numTurns: .2f}s')
        print('Average of scores difference per game: {}'.format(int(agents['Minimax'].accumulatedScore - nonMinimaxScore) / games_played))
        print('Average of generated nodes per game: {}'.format(int(agents['Minimax'].numNodes / games_played)))
        
    with open(os.path.join(q_dir, file_name), 'a') as file:
        file.write(str(games_played) +','
        + str(mean_time) +','
        + str(agents['QLearner'].numWins) + ','
        + str(agents['Random'].numWins) + ','
        + str(agents['Greedy'].numWins) + ',' 
        + str(agents['Minimax'].numWins) + ',' 
        + str(games_played-agents['Random'].numWins - agents['Greedy'].numWins - agents['QLearner'].numWins - agents['Minimax'].numWins) + ','
        + str(agents['QLearner'].accumulatedScore / CHECK_POINT) + ',' 
        + str(agents['Random'].accumulatedScore / CHECK_POINT) + ',' 
        + str(agents['Greedy'].accumulatedScore / CHECK_POINT) + ','
        + str(agents['Minimax'].accumulatedScore / CHECK_POINT) + ','
        + str(agents['QLearner'].numQUpdated) + ','
        + str(len(agents['QLearner'].q)) + '\n')
    
        
if __name__=="__main__":
    start_all = time.time()
    
    # The dataset for the metrics is created
    file_name = datetime.now().strftime('iwoki_%Y_%m_%d_%H_%M.csv')  # dataset
    q_dir = 'datasets'
    if not os.path.exists(q_dir):
        os.mkdir(q_dir)
    with open(os.path.join(q_dir, file_name), 'a') as file:
        file.write('numGames,time,QLearnerWins,RandomWins,GreedyWins,MinimaxWins,draws,'
               'scoresQLearner,scoresRandom,scoresGreedy,scoresMinimax,updatedQ,totalQ\n')
        
    os.system('cls')          
    print ("\n-- Welcome to iwoki--\n")
    agents = {
    'Random' : RandomPlayer('Random'),
    'Greedy' : GreedyPlayer('Greedy'),
    'QLearner' : QLearningPlayer('QLearner', Qfile=None),
    'Minimax' : MinimaxPlayer('Minimax'),
    'Human' : HumanPlayer('Human'),
    }
    # Select the players fo the game:
    players = [agents['Random'], agents['QLearner']]

    previous_check_time = start_all
    for gameId in range(NUM_GAMES): # Number of games
        start = time.time()
        print('\nGame number {}:\n'.format(gameId+1))

        gameSpace = initializeAll(players)
        gameSpace.getAllInitialTiles(numSmall=9, numHexagonal=3)

        players = drawPlayersOrder(gameSpace.players)
        print("The game begins with the player " + players[0].name)
        print("\n-- The game begins --")
        playGame(players, gameSpace)

        end = time.time()
        print(f'\nGame duration:{end - start: .2f}s = {(end - start)/60:.2f} min = {(end - start)/3600:.2f} hours\n')
        if (gameId+1) % CHECK_POINT == 0:
            check_time = time.time()
            saveMetrics(file_name, check_time - previous_check_time, gameId+1, players)
            if not any([p for p in players if p.name == 'Minimax']): # None of the players is 'Minimax'
                for player in players:
                    player.accumulatedScore = 0

    if any([p for p in players if p.name == 'QLearner']):
        agents['QLearner'].save_Q()
    end_all = time.time()
    print(f'Total time:{end_all - start_all: .2f}s = {(end_all - start_all)/60:.2f} min = {(end_all - start_all)/3600:.2f} hours')

    