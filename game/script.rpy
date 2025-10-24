init:
    image bg bus_stop = "bus_stop.jpg"
    image bg bus = "bus.jpg"
    image bg bus_inside = "bus_inside.jpg"
    image bg road_to_home = "road_to_home.jpg"
    image bg missing_p_news = "missing_people_news.jpg"
    image cat = "cute_cat.png"
    $ cat = Character("Kitty", color="#382a19")
    # Размером они обычно <~четверть-треть ширины игрового
    # окна>х<полная высота игрового окна>


# Игра начинается здесь:
label start:
    scene bg bus_stop
    show cat at center with moveinleft
    cat "meow"
    cat "meow meow"
    hide cat
    scene bg bus
    "..."
    show cat at center with moveinleft
    cat "meow"
    cat "meow meow"
    hide cat
    menu:
        "MEOW?"
        "meow...":
            scene bg road_to_home
            show cat at center with moveinleft
            cat "meow."
            cat "meow meow..."
            hide cat
            scene bg missing_p_news
            "CAT" "Meow Meow Meow"
            show cat at center with moveinleft
            cat "meow"
            "END."
            return
        "meow meow":
            scene bg bus_inside
            show cat at center with moveinleft
            cat "meow..."
            hide cat



return


#1920x1080