# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("")
define d = Character("???")
define config.name = ("This job is worse than hell.")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg gray gradient

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    n "You feel…"

    n "fuzzy…"

    n "everything is-"

    n "black."

    scene bg black
    with fade 

    d "{i}My head…{/i}"

    d "{i}it {b}hurts.{/b}{/i}"

    d "{i}Why…{/i}"

    d "{i}what… what's happening…?{/i}"

    n "You give in, and you..."

    n "fall into slumber. "

    scene bg white
    with fade

    d "Agh... what the-"

    d "AHHH MY EYES!"

    d "{i}Gughh...{/i}"

    scene bg sometime later
    with fade
    pause

    scene bg white
    with fade

    d "{i}Why is it so... so bright?!{/i}"

    d "Ugh... I think I'm gonna go blind."

    d "Where even is this...?"

    d "No place in hell is this... {i}bright.{/i}"

    # This ends the game.

    return
