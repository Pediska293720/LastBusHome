init:
    image bg bus_stop = "bus_stop.jpg"
    image bg bus = "bus.jpg"
    image bg bus_inside = "bus_inside.jpg"
    image bg road_to_home = "road_to_home.jpg"
    image bg missing_p_news = "missing_people_news.jpg"
    image bg final_1 = "best_choice.jpg"
    image aya = "cute_cat.png"
    $ aya = Character("Aya (yes)")
    # Размером они обычно <~четверть-треть ширины игрового
    # окна>х<полная высота игрового окна>
    $ id_memory = [0, 1]
    $ flag_memory = ""

# Игра начинается здесь:
label start:
    scene bg bus_stop
    "Солнце давно зашло за горизонт, на улице  - кромешная темень. Лишь редкие фонари мигают вдоль дороги. "
    "Ни души. Не слышно даже шума машин вдалеке. Ощущение, будто город провалился в очень глубокий сон. "
    "С трудом переставляя ноги, к автобусной остановке подходит девушка."
    show aya at left with moveinleft
    aya "Наконец-то дошла..."
    aya "Эти курсы слишком выматывают, хочу поскорее добраться до дома..."
    hide aya with moveoutleft
    "Она тяжело опускается на холодную скамейку, рюкзак падает на пустое место рядом."
    "Ветер пробирает до мурашек, замершие руки не спасают даже глубокие карманы куртки."
    show aya at left with moveinleft
    aya "Вот бы автобус побыстрее приехал..."
    hide aya with moveoutleft
    "Девушка вздрагивает от очередного порыва ветра."
    "Автобуса нет уже довольно долго, и тревога в душе Аи все нарастает."
    "Но уже через мгновение, будто услышав ее желание, он медленно выплывает из-за поворота, подъезжает почти бесшумно."
    scene bg bus with fade
    "Однако спасительный транспорт выглядит совсем не безопасно, скорее наоборот - только пугает своим внешним видом."
    "Старая выцветшая краска с пятнами ржавчины, потрескавшиеся зеркала и фары, будто поглощающие остатки уличного света."
    "В окнах не видно пассажиров. Не видно и водителя. Казалось, автобус приехал сюда сам по себе."
    "С тихим скрежетом он останавливается."
    "Потянувшись к рюкзаку, Ая замирает в нерешительности."
    "Стоит ли садиться в этот автобус? Она слишком устала чтобы тратить еще больше сил на путь пешком, но и транспорт не вызывает особого доверия."
    "Мутные стекла, пустота в салоне, таинственность появления... Сомнение камнем оседает в груди. Сесть? Или уйти?"
    "Резко скрипнув, перед ней распахиваются двери. Из темного салона на веет запахом пыли и чего-то сладковатого, почти неуловимого. Внутри — никого."
    menu:
        "Cесть в автобус":
            jump go_bus

        "Пойти домой пешком":
            jump go_home

label go_home:
    "Нет. Все таки страх сильнее."
    "Сесть в этот автобус - сыграть в русскую рулетку. Кто знает что может произойти."
    show aya at left with moveinleft
    aya "Ну нет, лучше пройдусь еще немного."
    hide aya with moveoutleft
    "Накинув рюкзак на плечо, Ая направилась в темноту улицы."
    scene bg road_to_home with fade
    ""
    scene bg missing_p_news with fade
    ""
    scene bg final_1 with fade
    ""
    return

label go_bus:
    "Усталость оказалась сильнее. Гораздо сильнее."
    "Страх отступил."
    "Накинув рюкзак, Ая направилась к дверям автобуса. Будь что будет. Она слишком устала чтобы думать о чем-то еще."
    scene bg bus_inside with fade

    jump choice_memory

label choice_memory:

    menu:
        "Счастливое воспоминание" if 0 in id_memory:
            $ id_memory.remove(0)
            if flag_memory == "":
                $ flag_memory = "happy"
            jump happy_memory

        "Грустное воспоминание" if 1 in id_memory:
            $ id_memory.remove(1)
            if flag_memory == "":
                $ flag_memory = "sad"
            jump sad_memory
    jump after_memory


label happy_memory:
    "happy"
    jump choice_memory

label sad_memory:
    "sad"
    jump choice_memory

label after_memory:
    "text"
    menu:
        "Платить?"

        "Отдать счастливое воспоминание":
            "оу ноу ты отдаешь свое счатье"
            jump go_home_without_happy

        "Отдать грустное воспоминание":
            "оу ноу ты отдаешь свое несчастье"
            jump conductor_say

        "(Агрессивный ответ)":
            jump stay_bus

label go_home_without_happy:
    "final (очень sad)"
    return

label conductor_say:
    "bla bla bla"
    menu:
        "Что это за место":
            jump go_home_without_all

        "(Дождаться своей остановки)":
            jump go_home_without_sad

label go_home_without_all:
    "злой кондуктор ругается"
    "final (очень не очень)"
    return

label go_home_without_sad:
    "final (чуть чуть sad)"
    return


label stay_bus:
    "text..."
    if flag_memory == "happy":
        "Так дорожишь своим счастьем?"
        "text"
    elif flag_memory == "sad":
        "Цепляешься за свою боль?"
        "text"
    jump timer_choice


default downer = 0
screen QTEdown(rangeD, missed_event):
    on "show" action SetVariable("downer", rangeD)
    frame:
        xalign 0.5
        yalign 0.0
        hbox:
            timer 0.1 action If(0 < downer, true = SetVariable("downer", downer - 0.1), false = [Hide("timerDown"), Jump(missed_event)]) repeat True

            bar:
                value AnimatedValue(value=downer, range=rangeD, delay= 0.5)
                xalign 0.0
                yalign 0.0
                xmaximum 200

label timer_choice:
    show screen QTEdown(3, "pay_with_everything")
    menu:
        "Заплатить":
            hide screen QTEdown
            "Ну, плати всем тада"
            jump pay_with_everything

        "Настаивать на ответе":
            hide screen QTEdown
            "Ладно вот тебе ответ"
            jump get_answer

        "Попытаться сбежать":
            hide screen QTEdown
            "А фигушки сиди тут вечно"
            jump try_to_escape

label pay_with_everything:
    "Тебе пришлось отдать все свои воспоминания. Грустно конечно"
    "final (очень очень sad)"
    return

label get_answer:
    "Ну ты типо получил все ответы. Ура"
    "final (как будто даже не sad)"
    return

label try_to_escape:
    "Плохое решение"
    "final (тоже sad)"
    return 


#1920x1080