import turtle
import pandas

# Función para mostrar texto en una coordenada específica
tortuga = turtle.Turtle()


def mostrar_texto(texto, x, y):
    tortuga.penup()
    tortuga.hideturtle()
    tortuga.goto(x, y)
    tortuga.write(texto, align="center", font=("Arial", 12, "normal"))


# Creando la pantalla del juego
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Inicializando la recogida de datos
states = pandas.read_csv("50_states.csv")

# Variables para usar
game_is_on = True
all_states = states["state"].tolist()
list_of_correct_answers = []
count = 0

# Iniciando el Funcionamiento del juego
while game_is_on:
    answer_state = screen.textinput(title=f"{count}/50 the States", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in list_of_correct_answers]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # Línea que revisa si una palabra está entre los datos
    esta_presente = states.isin([answer_state.title()]).any().any()
    if esta_presente:
        if answer_state.title() not in list_of_correct_answers:
            fila_buscada = states[states["state"] == answer_state.title()]
            coordenada_x = fila_buscada["x"].values[0]
            coordenada_y = fila_buscada["y"].values[0]
            print("Yeah :) ")
            count += 1
            mostrar_texto(answer_state.capitalize(), coordenada_x, coordenada_y)
            list_of_correct_answers.append(answer_state.title())
            if count == 50:
                game_is_on = False
                print("Yeah You Win")
    else:
        print("Oh no :/")

# states to learn.csv

turtle.exitonclick()
