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

NUM_GAMES = 100 # Número de partidas
CHECK_POINT = 10 # Número de partidas para capturar datos generales que informan sobre la evolución de las partidas

def playGame(players, gameSpace):
    """ 
    Función que controla el turno de los jugadores y finaliza la partida. 
    PARAMETERS:
        players: lista de jugadores.
        gameSpace: espacio de juego.
    """
    while True:
        for player in players:
            if player.isTurn:
                if gameSpace.gameOver:
                    agents[player.name].getMove(gameSpace, train=True)
                    if gameSpace.endProperly:
                        return None
                    gameSpace.endProperly = True
                    break
                elif player.name == 'Human':
                    gameSpace.summary()
            
                agents[player.name].getMove(gameSpace, train=True)
                player.numTurns += 1
                break


def saveMetrics(file_name, time, games_played, players):
    """ 
    Función que en el estado de Check Point almacena y muestra datos generales que sobre la evolución de las partidas. 
    PARAMETERS:
        file_name: fichero donde se almacena la información.
        time: tiempo desde el anterior check point.
        games_played: número de partidas jugadas desde el inicio hasta el check point.
        players: lista de jugadores
    """
    print('*****************************')
    print('        CHECK POINT')
    print('*****************************')
    mean_time = time / games_played
    print('Partidas jugadas: {}'.format(games_played))
    print(f'Tiempo medio de las partidas:{mean_time: .2f}s')
    print('Promedio turnos empleados por cada jugador: {}'.format(int(players[0].numTurns / games_played)))
    winsAny = 0
    nonMinimaxScore=0
    for player in players:
        print('Número de partidas que gana el agente {}: {}'.format(player.name, player.numWins))
        winsAny += player.numWins
        if player.name != 'Minimax':
            nonMinimaxScore += player.accumulatedScore
    print('Número de empates: {}'.format(games_played-winsAny))
    if any([p for p in players if p.name == 'QLearner']):
        print('Número de Q-values actualizados: {}'.format(agents['QLearner'].numQUpdated))
        print('Número de Q-values TOTALES en Qfile: {}'.format(len(agents['QLearner'].q)))
    if any([p for p in players if p.name == 'Minimax']):
        print(f'Tiempo medio que tarda Minimax en decidir su movimiento:{(check_time - start_all) / players[0].numTurns: .2f}s')
        print('Promedio de diferencia de puntos por partida: {}'.format(int(agents['Minimax'].accumulatedScore - nonMinimaxScore) / games_played))
        print('Promedio de nodos generados por partida: {}'.format(int(agents['Minimax'].numNodes / games_played)))
        
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
    
    # Se crea el dataset para las métricas
    file_name = datetime.now().strftime('iwoki_%Y_%m_%d_%H_%M.csv')  # dataset
    q_dir = 'datasets'
    if not os.path.exists(q_dir):
        os.mkdir(q_dir)
    with open(os.path.join(q_dir, file_name), 'a') as file:
        file.write('numGames,time,QLearnerWins,RandomWins,GreedyWins,MinimaxWins,draws,'
               'scoresQLearner,scoresRandom,scoresGreedy,scoresMinimax,updatedQ,totalQ\n')
        
    os.system('cls')          
    print ("\n-- Bienvenido al iwoki--\n")
    agents = {
    'Random' : RandomPlayer('Random'),
    'Greedy' : GreedyPlayer('Greedy'),
    'QLearner' : QLearningPlayer('QLearner', lr=0.5, df=0.8, Qfile=None),
    'Minimax' : MinimaxPlayer('Minimax'),
    'Human' : HumanPlayer('Human'),
    }
    players = [agents['Greedy'], agents['Minimax']]

    previous_check_time = start_all
    for gameId in range(NUM_GAMES): # Número de partidas
        start = time.time()
        print('\nPartida número {}:\n'.format(gameId+1))

        gameSpace = initializeAll(players)
        gameSpace.getAllInitialPieces(numSmall=9, numHexagonal=3)

        players = drawPlayersOrder(gameSpace.players)
        print("Empieza la partida el jugador " + players[0].name)
        print("\n-- Se inicia la partida --")
        playGame(players, gameSpace)

        end = time.time()
        print(f'\nDuración de la partida:{end - start: .2f}s = {(end - start)/60:.2f} min = {(end - start)/3600:.2f} hours\n')
        if (gameId+1) % CHECK_POINT == 0:
            check_time = time.time()
            saveMetrics(file_name, check_time - previous_check_time, gameId+1, players)
            if not any([p for p in players if p.name == 'Minimax']): # 'Minimax' no es ninguno de los jugadores
                for player in players:
                    player.accumulatedScore = 0

    if any([p for p in players if p.name == 'QLearner']):
        agents['QLearner'].save_Q()
    end_all = time.time()
    print(f'Tiempo total empleado:{end_all - start_all: .2f}s = {(end_all - start_all)/60:.2f} min = {(end_all - start_all)/3600:.2f} hours')

    