# MathEvalLib


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.txt)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Description
This library allows for the solving of math equations inputted as strings. I made this because the eval function was too dangerous to use and had features I didn't need.\
This is a library I am writing to make a calculator app from scratch (Not completed yet) and I didn't want to use already existing libraries.
## How to use
It is quite simple. Using the evaluation function with the equation written in string form.
``` python
from MathEvalLib_NDev08 import MathEvalLib
matheval = MathEvalLib()

print(matheval.evaluate("2+3-4"))
```

That's all. At the moment it currently supports addition, subtraction, multiplication, and division, along with exponents, parentheses and Negatives.

## Features 

It currently supports:

* Addition and Subtraction
* Multiplication and Division
* Exponents
* Parentheses
* Negative Numbers

## Planned Features
* Implement decimal handling
* Make the tokenizer more robust to handle edge cases
* Implement Sqrt 
* functions like sine, cosine, and tangent.

## How To Install
This is written in pure python so all you should need is python.
1. clone the repo or download and extract the zip
2. run python.exe -m pip install .

And bang, you're good to go and use this in whatever project you like.
## How to contribute

Issues and bug reports are always welcome! If you have anything you would like to add you are welcome to create an issue or make a pull request.

## Final Thoughts
This is a project I started simply because I wanted to know if I could. And I did it. I hope you enjoy using my tool as much as I enjoyed making it. This was not the first project made for this purpose nor is it the best by any means. But it works, and in the end thats all that matters.
