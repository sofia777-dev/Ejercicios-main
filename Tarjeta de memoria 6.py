from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        # todas las líneas deben ser dadas durante la creación del objeto y serán registradas como propiedades
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('¿Qué color no aparece en la bandera de Estados Unidos?', 'Verde', 'Rojo', 'Blanco', 'Azul'))
questions_list.append(Question('Una residencia tradicional de los yakutos', 'Urasa', 'Yurta', 'Iglú', 'Choza'))
questions_list.append(Question('¿Cuál es la capital de Francia?', 'París', 'Londres', 'Berlín', 'Madrid'))   
questions_list.append(Question('¿Cuál es la capital de España?', 'Madrid', 'Barcelona', 'Sevilla', 'Valencia'))                     
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

Layout_ans2.addWidget(rbtn_2)
Layout_ans3.addWidget(rbtn_3) # dos respuestas en la segunda columna
Layout_ans3.addWidget(rbtn_4)

Layout_ans1.addLayout(Layout_ans2)
Layout_ans1.addLayout(Layout_ans3) # colocar las columnas en la misma línea

RadioGroupBox.setLayout(Layout_ans1) # colocar el diseño de las respuestas en el grupo de respuestas

AnsGroupBox = QGroupBox("Resultado de prueba") # grupo en pantalla para el resultado de la prueba
lb_Result = QLabel('¿Es correcto o no?') # texto de resultado de la prueba
lb_Correct = QLabel('¡Aquí estará la respuesta!') # texto de la respuesta correcta
Layout_res = QVBoxLayout()
Layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
Layout_res.addWidget(lb_Correct, alignment=(Qt.AlignLeft | Qt.AlignTop))
AnsGroupBox.setLayout(Layout_res)

layout_line1 = QHBoxLayout() # diseño de la primera línea
layout_line2 = QHBoxLayout() # diseño de la segunda línea
layout_line3 = QHBoxLayout() # diseño de la tercera línea
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide() # ocultar el grupo de resultados de la prueba al inicio

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # botón de responder
layout_line3.addStretch(1)

Layout_card = QVBoxLayout() # diseño de la tarjeta

Layout_card.addLayout(layout_line1, stretch=2)
Layout_card.addLayout(layout_line2, stretch=8)
Layout_card.addStretch(1)
Layout_card.addLayout(layout_line3, stretch=1)
Layout_card.addStretch(1)
Layout_card.setSpacing(5) # establecer el espacio entre los elementos del diseño

def show_result():
    RadioGroupBox.hide() # ocultar el grupo de respuestas
    AnsGroupBox.show() # mostrar el grupo de resultados de la prueba
    btn_OK.setText('Siguiente pregunta') # cambiar el texto del botón a "Siguiente pregunta"
    
def show_question():
    RadioGroupBox.show() # mostrar el grupo de respuestas
    AnsGroupBox.hide() # ocultar el grupo de resultados de la prueba
    btn_OK.setText('Responder') # cambiar el texto del botón a "Responder"
    RadioGroup.setExclusive(False) # permitir que se deseleccione un botón de radio
    rbtn_1.setChecked(False) # deseleccionar el primer botón de radio
    rbtn_2.setChecked(False) # deseleccionar el segundo botón de radio
    rbtn_3.setChecked(False) # deseleccionar el tercer botón de radio
    rbtn_4.setChecked(False) # deseleccionar el cuarto botón de radio
    RadioGroup.setExclusive(True) # volver a establecer la exclusividad del grupo de botones de radio

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] # lista para almacenar las respuestas
def ask(q: Question):
    shuffle(answers) # mezclar las respuestas
    answers[0].setText(q.right_answer) # asignar la respuesta correcta al primer botón de radio
    answers[1].setText(q.wrong1) # asignar la primera respuesta incorrecta al segundo botón de radio
    answers[2].setText(q.wrong2) # asignar la segunda respuesta incorrecta al tercer botón de radio
    answers[3].setText(q.wrong3) # asignar la tercera respuesta incorrecta al cuarto botón de radio
    lb_Question.setText(q.question) # establecer el texto de la pregunta
    lb_Correct.setText(q.right_answer) # establecer el texto de la respuesta correcta
    show_question() # mostrar la pregunta y ocultar el resultado de la prueba

def show_correct(res):
    lb_Result.setText(res)
    show_result() # mostrar el resultado de la prueba
    
def check_answer():
    if answers[0].isChecked():
        show_correct('¡Correcto!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('¡Incorrecto!')
def next_question():
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(questions_list):
       window.cur_question = 0
    q = questions_list[window.cur_question]
    ask(q)
    
def click_OK():
    if btn_OK.text() == 'Responder':
        check_answer()
    else:
        next_question()
        
      
window = QWidget() # crear la ventana principal
window.setLayout(Layout_card) # establecer el diseño de la tarjeta como el diseño principal de la ventana
window.setWindowTitle('Tarjeta de Memoria') # establecer el título de la ventana
window.cur_question = -1 # variable para almacenar el índice de la pregunta actual
btn_OK.clicked.connect(click_OK)
next_question() # conectar el botón de responder con la función click_OK
window.show() # mostrar la ventana principal
app.exec()