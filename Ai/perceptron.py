import sys
import os
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'game'))

from game_engine import FlappyBirdEnv

class Perceptron:
    def __init__(self, n_inputs=5):
        self.weights = np.random.uniform(-1, 1, n_inputs)
        self.weights[3] = 0
        self.bias = np.random.uniform(-1, 1)


    def forward(self, x):
        z = np.dot(self.weights, x) + self.bias
        return np.tanh(z)

    def decide(self, x):
        return 1 if self.forward(x) > 0 else 0


def run(n_games=10):
    env = FlappyBirdEnv()
    net = Perceptron()
    scores = []

    for i in range(n_games):
        state = env.reset()
        done = False
        while not done:
            action = net.decide(state)
            state, reward, done = env.step(action)
        scores.append(env.score)
        print(f"Partie {i + 1} : score = {env.score}")

    print(f"\nScore moyen sur {n_games} parties : {sum(scores) / len(scores):.1f}")


def tanh_perceptron(n_games) : 
    env = FlappyBirdEnv()
    net = Perceptron()
    scores = []

    best_score = -1
    best_weights = None
    best_bias = None

    for _ in range(n_games):
        net = Perceptron()
        state = env.reset()
        done = False
        while not done :
            action = net.decide(state)
            state, reward, done = env.step(action)
        if env.score > best_score:
            best_score = env.score
            best_weights = net.weights.copy()
            best_bias = net.bias
    
    print(f"Meilleur score : {best_score}")
    print(f"Poids : {best_weights}")
    print(f"Biais : {best_bias}")
if __name__ == '__main__':
    tanh_perceptron(100)
