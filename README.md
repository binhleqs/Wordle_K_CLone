# Wordle Game

This is a python implementation of wordle, which uses the same set of available words as the hit game, Wordle.

## Play the game manually

```bash
python3 src/wordle_main.py --strategy=human
```

## Play the game using an AI

```bash
python3 src/wordle_main.py --strategy=(random|similar_words)
```

## Implement an algorithm to solve it

So you want to write an algorithm that can solve Wordle in as few turns as possible?

1. Create a new class that inherits from `BaseStrategy`.
2. Change the implementation of the `get_guess()` function, as well as the `make_guess()` function.
3. Update `wordle_main` to import the new `Strategy` class that you created.
4. Run it: `python3 src/wordle_main.py --stragey={your class}`

I have taken the liberty of implementing & wiring together `SimilarWordsStrategy` to show how you can wire your own algorithm in.
