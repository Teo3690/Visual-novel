# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Typography replacer
define typography = (what)
    : replacements = [
        ('. ','. {w=.2}'),
        ('? ','? {w=.25}'),
        ('! ','! {w=.25}'),
        (', ',', {w=.15}'),
    ]

    for item in replacements:
        what = what.replace(item[0],item[1])

        return what
    
    define config.say_menu_text_filter = typography


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


    n "{cps=10}You feel…{/cps}"

    n "{cps=10}fuzzy…{/cps}"

    n "{cps=10}everything is-{/cps}"

    n "{cps=10}black.{/cps}"

    scene bg black
    with fade 
    pause 1.5

    d "{cps=15}{i}My head…{/i}{/cps}"

    d "{cps=15}{i}it {w}{b}hurts.{/b}{/i}"

    d "{cps=15}{i}Why…{/i}"

    d "{cps=15ß}{i}what… what's happening…?{/i}"

    n "{cps=15ß}You give in, and you..."

    n "{cps=15}fall into slumber. "

    scene bg white
    with fade

    n "You slowly open your eyes."

    n "The surface you're laying on feels cold, {w}making you shiver."

    d "Agh... what the-"

    d "AHHH MY EYES!"

    d "{i}Gughh...{/i}"

    scene bg sometime later
    with fade
    pause 0.5

    scene bg white
    with fade

    d "{i}Why is it so... {w}so bright?!{/i}"

    d "Ugh... I think I'm gonna go blind."

    d "Where even is this...?"

    d "No place in hell is this... {w}{i}bright.{/i}"

    # This ends the game.

    return
