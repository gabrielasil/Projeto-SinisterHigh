# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lyla")

define n = Character("????", who_color="#eee")



define humanas = False
define exatas = False
define biologicas = False



# The game starts here.

label start:

    stop music

    "Um mundo onde monstros vivem..."

    "...e convivem entre humanos!"

    "A protagonista desta história se chama {color=#9933ff}Lyla{/color}"

    "Uma estudante da escola híbrida de humanóides Monsters and Humans High School."

    "E hoje é seu primeiro dia de aula em sua nova escola..."

    l "Onde eu deixei meu tênis?"

    l "Será que eu tô arrumada demais pra uma volta ás aulas?"

    show bg bedroom
    with dissolve

    l "Ah, tanto faz, não vou perder muito tempo com isso, se não eu vou me atrasar..."


    menu:

        "A primeira aula é de uma disciplina de humanas."

        "Eu gosto mais de disciplinas da área de..."

        "Humanas, então tô bem ansiosa pra essa aula!":
            $ humanas = True
        
        "Biológicas, então eu tô ok com essa aula...":
            $ biologicas = True

        "Exatas, então essa aula vai ser uma tortura pra mim...":
            $ exatas = True

    hide bg bedroom
    with dissolve

    "Confesso que sinto um pouco de frio na barriga ao pensar em tudo que pode acontecer esse ano..."

    show bg escola corredor
    play music "musica escola.mp3"

    "Enquanto ando pelos corredores, procurando a minha sala, ouço uma voz familiar me chamando ao fundo."

    show nauk happy

    n "LYLA!?"

    "A voz familiar realmente era familiar..."

    n "MEU DEUS, A QUANTAS DÉCADAS A GENTE NÃO SE VÊ?"

    l "CARAMBA, OI {color=#ff9494}NAUK{/color}, A QUANTO TEMPO MESMO!"
    $ n = Character("Nauk", who_color="#ff9494")

    "Nauk é um velho amigo meu do ensino fundamental."

    n "Meu deus, você tá MUITO diferente de quando a gente se viu a última vez."

    l "Olha, você também mudou bastante, já que se não me falha a memória, eu costumava ser bem mais alta que você"

    n "Ah, que que eu posso dizer né... Mas vem cá, em qual sala você ficou esse ano?"

    l "1C, porquê?"

    with hpunch 

    n "CARAMBA! EU TAMBÉM!"

    "É curioso como ele praticamente só ficou maior desde a última vez que nos falamos, sua personalidade não mudou nada..." 

    "Provavelmente ainda tem os mesmos gostos estranhos de quando tentava dolorosamente me ensinar Xadrez Monstro..."

    "Ou quando tentou me fazer gostar de futebol brasileiro."

    "Mas aparentemente eu fui a única do nosso grupinho que não fez novas amizades."

    return
