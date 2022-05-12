# Rock, Paper, Scissors

## Goal(s)
I would simply like to observe the various outcomes of a single-shot game of RPS. I would like later iterations of the model to simulate a series of games where players used pre-selected non-changing strategies. Later still, I'd like to simulate adaptive strategies in an agent-based form of the model.

## Background
**Rock, Paper, Scissors** is a two-player game where players act by selecting one of three choices (rock, paper, or scissors) and comparing their own selection to that of the other player. Selections "beat" another selection using a predetermined ruleset:
- Rocks beat scissors
- Scissors beat papers
- Papers beat rocks

**Note:** When two selectsion are the same, a draw has occurred

## Assumption(s)
Initially, there are no assumptions as the model is a single-shot system with effectively random selections being made by players. In the future, I will have assumptions about the likely outcome of two strategies being played against each other.

## Random Variables
The first iteration of my model will randomly select **rock**, **paper**, or **scissors** for both players. In the future, randomized behavior will be introduced as more complex selection strategies are developed but I can't say exactly how at this point.

## Experiment(s)
This model, to begin, will only really be useful in expressing the payoff matrix.

## Initial Conditions
No initial conditions.

## Model Elements
Initially, our winner will be undetermined. After both players make selections those selections will be compared and our winner will be updated.