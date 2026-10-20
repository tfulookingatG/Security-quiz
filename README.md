# Security Quiz

A command-line quiz that measures how well you protect yourself online. You get a score out of 100, a rating, and personal tips on how to improve. You can also test the strength of your password.

## Features

- 7 security questions, weighted by importance
- Score out of 100 with a rating from "Very weak" to "Excellent"
- Tips for every question you answered "No" to, most important first
- Optional password strength tester (scored out of 10)
- Your password is typed hidden and is never stored or sent anywhere

## Requirements

- [Python 3.6 or newer](https://www.python.org/downloads/)

No extra packages needed.

## How to run

1. Download `Vragen.py` (or click **Code → Download ZIP** and unzip it)
2. Open a terminal in the folder with the file
3. Run:

```
python Vragen.py
```

On some systems you need `py Vragen.py` (Windows) or `python3 Vragen.py` (Mac/Linux).

## How the score works

Every question has a weight. Answer "Yes" and you earn those points. The weights add up to 100.

| Score | Rating |
|---|---|
| 90-100 | Excellent |
| 80-89 | Strong |
| 60-79 | Decent |
| 40-59 | Weak |
| 20-39 | Poor |
| 0-19 | Very weak |

## Password tester

The optional password test gives a score out of 10: up to 6 points for length and 1 point each for an uppercase letter, a lowercase letter, a number and a special character.

Note: it only checks length and character types, not whether a password is commonly used. A password like `Password123!` can still score high, so don't treat this as a guarantee.

## Roadmap

- [ ] Check passwords against a list of common passwords
- [ ] Move the questions to a separate file
- [ ] Graphical interface

## License

MIT
