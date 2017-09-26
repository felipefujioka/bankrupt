# Bankrupt

## Install

This simulation runs on python 3.6.

## Running the test

If you have an installation of python 3.4 or higher, just run:

```
cd bankrupt
./bin/run.sh
```

The output will be in CSV (Comma separated values), featuring the following columns: max_rounds, player_style and rounds

That represent if a game has ended by timeout, the player style that won the match and the number of rounds that took to end the game, respectively.

## Browsing results

The results of the simulation can be examined on the results folder. Run:

````
cd bankrupt/results
python pip install -r requirements.txt
jupyter notebook
```

Or visit https://github.com/felipefujioka/bankrupt/blob/master/results/bankrupt_stats.ipynb to see my calculated results.
