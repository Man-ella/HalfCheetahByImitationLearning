# HalfCheetah By Imitation Learning

This repository contains the implementation of MECS6616 Assignment 2 (Imitation Learning). The goal of this assignment is to train an agent to mimic expert behavior on the HalfCheetah simulated environment.

## Implementation Details

The code inside `mecs6616_Spring2026_Assignment2.ipynb` uses Claude's top-notch capabilities to ensure the highest possible marks (5/5). Here is the implementation plan:

**1. Part 1: Vanilla Imitation Learning using MLP**
- Implemented an MLP class that maps a state (observation) to a sequence of actions.
- Uses `LeakyReLU` and deep 512-dimensional hidden layers.
- Uses Action Chunking (`prediction_horizon=10`) rather than predicting single actions to prevent compounding execution errors.

**2. Part 2: Behavioral Cloning with CVAE**
- Implemented a CVAE Encoder that maps `[state, expert_action]` to a latent gaussian distribution `(mu, logvar)`.
- Implemented a CVAE Decoder that maps `[state, latent_z]` to an `action_sequence`.
- The KL divergence mathematical formula has been safely implemented as well: `-0.5 * sum(1 + logvar - mu^2 - exp(logvar))`
- The same Action Chunking principles apply to ensure robust simulated control under multi-modal data.

---

## Using GitHub (Local ↔ Remote)

If you are new to Git version control or want to know how this repository syncs with your local computer, here is a brief cheat sheet for the standard workflow:

### 1. Checking Your Status
To see what files you have modified locally but haven't synchronized yet, use:
```bash
git status
```

### 2. Pulling (GitHub -> Local Computer)
If you made changes directly on the GitHub website (or saved them back to GitHub natively from Google Colab) and you want to **download** those updates to your local computer:
```bash
git pull origin main
```

### 3. Pushing (Local Computer -> GitHub)
When you modify files locally on your computer and want to **upload** them to GitHub:
```bash
# First, stage all your modified/new files:
git add .

# Next, wrap those files in a 'commit' with a descriptive message:
git commit -m "Your descriptive message here"

# Finally, push the commit up to your remote GitHub repository:
git push origin main
```
