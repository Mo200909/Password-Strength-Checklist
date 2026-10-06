# Password Strength Checklist

**TL;DR:** Type a password, get a pass/fail checklist of five basic rules. No score and no overall verdict. Standard library only.

## Run it (3 steps, ~1 min)

1. Open a terminal in this folder.
2. Run `python password_strength_checker.py`
3. Enter a username (unused) and a password when prompted.

Example output:

```
mo, your password is 9 characters long.
Password is too short.
Password has uppercase letters.
Password has lowercase letters.
Password has a number.
Password needs a symbol.
```

## The 5 checks

1. At least 12 characters
2. Contains an uppercase letter
3. Contains a lowercase letter
4. Contains a digit
5. Contains a symbol (any character in Python's `string.punctuation`)

Each check prints one line. Nothing combines them into a score.

## Limits (read before trusting it)

1. **The password is visible while you type** and is not hidden. Run it only on throwaway test passwords, never a real one.
2. No score or verdict, so you must read the five lines yourself.
3. The username prompt is unused beyond echoing it back.
4. Rules only: no common-password list, no breached-password check, no entropy estimate. A password like `Password1!` passes the 4 character-type checks, and it's still weak.
5. Testing was light: one password run on an earlier 4-check version, with the rest traced by hand. There's no test suite.

Learning project. Not a security control.

## Build note

This is a rewrite of an earlier AI-generated version, which it replaces. Code in this version written by me. AI (Claude) provided the project plan and debugging feedback, including catching that `isupper()` and `islower()` only match all-uppercase or all-lowercase strings.
