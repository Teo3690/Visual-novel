# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("")
define d = Character("???")
define e = Character("")
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


    n "{cps=10}You feel…"

    n "{cps=10}fuzzy…{/cps}"

    n "{cps=10}everything is-{/cps}"

    n "{cps=15}black.{/cps}"

    scene bg black
    with fade 
    pause 1.5

    d "{cps=15}{i}My head…{/i}{/cps}"

    d "{cps=15}{i}it{/cps} {w=0.5}{b}{i}hurts.{/b}{/i}"

    d "{cps=15}{i}Why… {w=0.5}what- what's happening…?{/i}"

    n "{cps=15}You give in, and you... {w=0.5}fall into slumber."

    pause 1.5
    scene bg white
    with fade
    pause 1.5

    n "You slowly open your eyes."

    n "The surface you're laying on feels cold, {w=0.5}making you shiver."

    d "Agh... what the-"

    d "AHHH MY EYES!"

    d "{i}Urggh...{/i}"

    scene bg sometime later
    with fade
    pause 1.5

    scene bg white
    with fade
    pause 1.5

    d "{i}Why is it so... {w=0.5}so bright?!{/i}"

    d "Ugh... I think I'm gonna go blind."

    d "Where even is this...?"

    d "No place in hell is this... {w=0.5}{i}bright.{/i}"

    d "It's so {i}cold{/i} too."

    #Show scene of inside the restaurant

    d "Wait, {w=0.5}this looks... {w=1}familiar..."

    #Realisation sound effect & worried sprite

    d "No... {w=0.5}don't tell me..."

    #Show the same scene inside the restaurant but sprite is gone

    d "{b}I'M BACK IN THE BUILDING AGAIN!"

    # This ends the game.

    return
