import sys
import os
import statistics

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'game'))

from game_engine import FlappyBirdEnv

def naive_action(state):
    bird_above_gap_top = state[3]
    bird_velocity = state[1]

    if bird_above_gap_top < 0 or bird_velocity < 0.6:
        return 0
    return 1

def run(n_games=50):
    env = FlappyBirdEnv()
    scores = []

    for i in range(n_games):
        state = env.reset()
        done = False
        while not done:
            action = naive_action(state)
            state, reward, done = env.step(action)
        scores.append(env.score)
        print(f"Partie {i + 1} : score = {env.score}")

    print(f"Max : {max(scores)}, Min : {min(scores)}, Ecart-type : {statistics.stdev(scores):.2f}")

if __name__ == '__main__':
    run()
