#hangman design from Andy G's blog, found at https://gieseanw.wordpress.com/2010/03/29/ascii-hangman/
#no guesses wrong
initial_hangman = """
------
:    :
:
:
:
:
:
:
"""
one_wrong_hangman = """
------
:    :
:    @
:
:
:
:
:
"""
two_wrong_hangman = """
------
:    :
:    @
:    :
:    :
:
:
:
"""
three_wrong_hangman = """
------
:    :
:    @
:   /:
:    :
:
:
:
"""
four_wrong_hangman = """
------
:    :
:    @
:   /:\\
:    :
:
:
:
"""
five_wrong_hangman = """
------
:    :
:    @
:   /:\\
:    :
:   /
:
:
"""
#game over
six_wrong_hangman = """
------
:    :
:    @
:   /:\\
:    :
:   / \\
:
:
"""