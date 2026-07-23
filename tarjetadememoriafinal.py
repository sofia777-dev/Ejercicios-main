from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton,
    QPushButton, QLabel)
from random import randint, shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        # todas las líneas deben ser dadas durante la creación del objeto y serán registradas como propiedades
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        
questions_list = []
questions_list.append(Question('¿Qué color no aparece en la bandera de Estados Unidos?',
'Verde', 'Rojo', 'Blanco', 'Azul'))
questions_list.append(Question('Una residencia tradicional de los yakutos', 'Urasa', 
'Yurta', 'Iglú', 'Choza'))
questions_list.append(Question('¿Cuál es la capital de Francia?', 'París', 
'Londres', 'Berlín', 'Madrid'))
questions_list.append(Question('¿Cuál es la capital de España?', 'Madrid', 
'Barcelona', 'Sevilla', 'Valencia'))
questions_list.append(Question('¿Cuál es la capital de Alemania?', 'Berlín',
'Munich', 'Hamburgo', 'Frankfurt'))
questions_list.append(Question('¿Cuál es la capital de Italia?', 'Roma',
'Milán', 'Venecia', 'Florencia'))

app = QApplication([])
btn_OK = QPushButton('Responder') # botón de responder
lb_Question = QLabel('¡La pregunta más difícil del mundo!') # texto de pregunta

RadioGroupBox = QGroupBox("Opciones de respuesta") # grupo en pantalla para los botones de radio con respuestas

rbtn_1 = QRadioButton('Opción 1')
rbtn_2 = QRadioButton('Opción 2')
rbtn_3 = QRadioButton('Opción 3')
rbtn_4 = QRadioButton('Opción 4')

RadioGroup = QButtonGroup() # este agrupa los botones de radio para poder controlar su comportamiento
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

Layout_ans1 = QHBoxLayout()
Layout_ans2 = QVBoxLayout() # las verticales estarán dentro de la horizontal
Layout_ans3 = QVBoxLayout()
Layout_ans2.addWidget(rbtn_1) # dos respuestas en la primera columna
Layout_ans2.addWidget(rbtn_2) # dos respuestas en la primera columna
Layout_ans3.addWidget(rbtn_3) # dos respuestas en la segunda columna
Layout_ans3.addWidget(rbtn_4) # dos respuestas en la segunda columna
Layout_ans1.addLayout(Layout_ans2)
Layout_ans1.addLayout(Layout_ans3) # colocar las columnas en la misma línea
RadioGroupBox.setLayout(Layout_ans1) # colocar el diseño de las respuestas en el grupo
AnsGroupBox = QGroupBox("Resultado de prueba") # grupo en pantalla para el resultado de la prueba
lb_Result = QLabel('¿Es correcto o no?') # texto de resultado de la prueba
lb_Correct = QLabel('¡Aquí estará la respuesta!') # texto de la respuesta correcta
Layout_res = QVBoxLayout()
Layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
Layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(Layout_res) # colocar el diseño de las respuestas en el grupo
Layout_line1 = QHBoxLayout() # diseño de la primera línea
Layout_line2 = QHBoxLayout() # diseño de la segunda línea
Layout_line3 = QHBoxLayout() # diseño de la tercera línea

Layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
Layout_line2.addWidget(RadioGroupBox) # el grupo de respuestas con botones de radio
Layout_line2.addWidget(AnsGroupBox) 
AnsGroupBox.hide()
Layout_line3.addStretch(1)
Layout_line3.addWidget(btn_OK, stretch=2) # botón de respuesta
Layout_line3.addStretch(1)
Layout_card = QVBoxLayout() # diseño de la tarjeta
Layout_card.addLayout(Layout_line1, stretch=2)
Layout_card.addLayout(Layout_line2, stretch=8)
Layout_card.addStretch(1)
Layout_card.addLayout(Layout_line3, stretch=1)
Layout_card.addStretch(1)
Layout_card.setSpacing(5) # establecer el espacio entre los elementos del diseño

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Siguiente pregunta')


RadioGroup.setExclusive(False) # deseleccionar todos los botones de radio

def show_question(): 
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Responder')
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # volver a hacer que los botones de radio sean exclusivos
    
answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] # lista de botones de radio para las respuestas

def ask(q: Question):
    shuffle(answer) # mezclar las respuestas
    answer[0].setText(q.right_answer) # colocar la respuesta correcta en el primer botón de radi
    answer[1].setText(q.wrong1) # colocar la primera respuesta incorrecta en el segundo botón de radio
    answer[2].setText(q.wrong2) # colocar la segunda respuesta incorrecta en el tercer botón de radio
    answer[3].setText(q.wrong3) # colocar la tercera respuesta incorrecta en el cuarto botón de radio
    lb_Question.setText(q.question) # colocar la pregunta en el texto de la pregunta
    lb_Correct.setText(q.right_answer) # colocar la respuesta correcta en el texto de la respuesta correcta
    show_question() # mostrar la pregunta y ocultar el resultado de la prueba
    
def show_correct(res):
    lb_Result.setText(res) # colocar el resultado de la prueba en el texto del resultado de la prueba
    show_result() # mostrar el resultado de la prueba y ocultar la pregunta
    
def check_answer():
   if answer[0].isChecked():
        show_correct('¡Correcto!')
        window.score += 1
        print('Estadisticas/n-Preguntas totales:', window.total, '/n-Preguntas correctas:', window.score, '/n-Preguntas incorrectas:', window.total - window.score)
        print('Calificación:', window.score / window.total * 100, '%')
   else:
       if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('¡Incorrecto!')
            print('Calificación:', (window.score / window.total * 100, '%'))
            
def next_question():
    window.total += 1
    print('Estadisticas/n-Preguntas totales:', window.total, '/n-Preguntas correctas:', window.score, '/n-Preguntas incorrectas:', window.total - window.score)
    cur_question = randint(0, len(questions_list) - 1) # seleccionar una pregunta aleatoria de la lista de preguntas
    q = questions_list[cur_question] # obtener la pregunta seleccionada
    ask(q) # mostrar la pregunta y las respuestas en la pantalla

def click_OK():
    if btn_OK.text() == 'Responder':
        check_answer() # comprobar la respuesta
    else:
        next_question() # pasar a la siguiente pregunta
        
window = QWidget() # crear una ventana
window.setLayout(Layout_card) # colocar el diseño de la tarjeta en la ventana
window.setWindowTitle('Tarjeta de memoria') # establecer el título de la ventana

btn_OK.clicked.connect(click_OK) # conectar el botón de respuesta con la función click_OK

window.score = 0
window.total = 0
next_question() # mostrar la primera pregunta
window.resize(400, 300) # establecer el tamaño de la ventana
window.show() # mostrar la ventana
app.exec_() # ejecutar la aplicación

