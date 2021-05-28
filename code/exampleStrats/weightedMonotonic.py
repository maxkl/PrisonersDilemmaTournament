# Copyright (c) 2021 maxkl
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# This strategy works by weighing and accumulating the opponents' most recent moves

# Weights for opponents' past moves, starting with the most recent one. These were determined in part by intuition and
# in part by experimentation. The '1' makes this behave similarly to titForTat. More or fewer and lower or higher
# weights make this strategy worse against a collection of 55 strategies by l4vr0v and valadaptive. I've also tried
# patterns like decreasing weights, incorporating the full history and others but none was as good as this one:
weights = [1, -0.8, 0.8, -0.8, 0.8, -0.8, 0.8, -0.8, 0.8]

def strategy(history, memory):
    round_index = history.shape[1]
    opponent_history = history[1]
    
    acc = 0
    for (i, w) in enumerate(weights):
        if i < round_index:
            # Weigh opponents' i-to-last move (-1 if they defected, +1 if they cooperated)
            acc += w * (opponent_history[-i - 1] * 2 - 1)
    
    # Cooperate if weighted sum is at least 0. It's important to cooperate in the first round (acc=0) as to not anger
    # the Grim Trigger
    return 1 if acc >= 0 else 0, None

