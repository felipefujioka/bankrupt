# Bankrupt

## Install

This simulation runs on python 3.4+, and requires just the builtin libraries.

## Running the test

If you have an installation of python 3.4 or higher, just run (on UNIX like system):

```
cd bankrupt
./bin/run.sh
```

The output will tell the number of games that ends in a timeout, the mean duration of a game, the number of times each player style has won, the player style that more frequently wins.

## Browsing results

The results of the simulation can be examined on the results folder. Run:

```
cd bankrupt/results
python pip install -r requirements.txt
jupyter notebook
```

Or visit https://github.com/felipefujioka/bankrupt/blob/master/results/bankrupt_stats.ipynb to see my calculated results.

A file with the records of a entire game can be found at `results/game.txt`.
