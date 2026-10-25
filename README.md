# Flappy Bird & neuroévolution

Jeu Flappy Bird en Pygame et agents qui apprennent à y jouer : bot naïf, perceptron et neuroévolution NEAT (points de sauvegarde, courbe de fitness, visualisation du réseau).

**Jouer en ligne : https://mvtteo.github.io/Flappy_bird/** (version web compilée avec pygbag ; espace ou clic pour sauter)

## Lancer en local

```bash
pip install -r game/requirements.txt
python game/main.py            # jouer

pip install -r Ai/requirements.txt
python Ai/train.py             # entraîner NEAT
python Ai/play_ai.py           # regarder le meilleur génome jouer
```

La version web (branche `gh-pages`) reprend `game/` avec une boucle `asyncio` exigée par pygbag et le clic / toucher pour démarrer et rejouer.
