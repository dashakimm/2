#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from random import shuffle,randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox,QButtonGroup, QBoxLayout

class Question():
    def __init__(self, question, right_answer,wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
 
question_list = []
question_list.append(Question('Сколько материков на земле?', '6', '8', '5' ,'7'))
question_list.append(Question('Сколько океанов на земле?', '4', '3', '5', '6'))
question_list.append(Question('Какой материк самый большой?', 'Евразия', 'Африка', 'Антарктида', 'Северная америка'))
question_list.append(Question('Сколько недель в году?','52' ,'56' ,'78' ,'97'  ))
app = QApplication([])
main_win = QWidget()
main_win.cur_index = -1
main_win.setWindowTitle('Memory Card')
main_win.resize(300,200)
button = QPushButton('Ответить')
text = QLabel('Какой национальности не существует?')

line = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line3.addWidget(button, alignment = Qt.AlignCenter )

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
line2.addWidget(RadioGroupBox,alignment = Qt.AlignCenter)
layout1 = QVBoxLayout()
layout1.addLayout(line)
layout1.addLayout(line2)
layout1.addLayout(line3)
main_win.setLayout(layout1)

AnsGroupBox = QGroupBox('Результат теста')
vert = QVBoxLayout()
res = QLabel('Правильно/Неправильно')
res2 = QLabel('Правильный ответ')
vert.addWidget(res)
vert.addWidget(res2)
AnsGroupBox.setLayout(vert)
AnsGroupBox.hide()
line2.addWidget(AnsGroupBox, alignment = Qt.AlignCenter)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')
radio_buttns = QButtonGroup()
radio_buttns.addButton(rbtn_1)
radio_buttns.addButton(rbtn_2)
radio_buttns.addButton(rbtn_3)
radio_buttns.addButton(rbtn_4)

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    radio_buttns.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    radio_buttns.setExclusive(True)
    button.setText('Ответить')
       
def next_question():
    cur_question = randint(0,len(question_list)-1)
    ask(question_list[main_win.cur_index])
    show_question()
buttons = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q: Question):
    shuffle(buttons)
    buttons[0].setText(q.right_answer)
    text.setText(q.question)
    buttons[1].setText(q.wrong1)
    buttons[2].setText(q.wrong2)
    buttons[3].setText(q.wrong3)
    res2.setText(q.right_answer)

# def show_correct(res):

def chek_answer():
    if buttons[0].isChecked():
        show_correct('Правильно')
    else:
        show_correct('Неверно')

def show_correct(result):
    res.setText(result)
    show_result()

def click_ok():
    if button.text() == 'Ответить':
        chek_answer()
    else:
        next_question()

next_question()
button.clicked.connect(click_ok)
main_win.show()
app.exec_()

