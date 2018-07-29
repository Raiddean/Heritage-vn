label start:
    call prologue from _call_prologue
    call chapter1 from _call_chapter1
    return
label splashscreen:

    $ renpy.movie_cutscene('jahintro.mpeg')
    hide movie_cutscene
    return
