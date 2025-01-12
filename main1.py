''' Вікно для картки питання '''
from PyQt5.QtWidgets import QApplication
from random import shuffle, choice
from time import sleep
app = QApplication([])

from main_window import *
from menu_window import *


class Question():
    def __init__ (self, question1, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question1
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.correct = 0
        self.attempts = 0

    def got_right(self):
        self.correct += 1
        self.attempts += 1

    def got_wrong(self):
        self.attempts += 1


q1 = Question("Як звали Шевченка?", "Тарас", "Іван", "Григорій", "Олександр")
q2 = Question("Як звали Франка?", "Іван", "Тарас", "Олександр", "Григорій")
q3 = Question("Як звали Хмельницького?", "Богдан", "Стеапан", "Андрій", "Денис")
q4 = Question("Як звали Тютюнника?", "Григорій", "Михайло", "Федір", "Олесь")

radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
questions = [q1, q2, q3, q4]

def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_Question.setText(cur_q.question)
    lb_Correct.setText(cur_q.answer)
    shuffle(radio_buttons)

    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)

new_question()

def show_result():
   ''' показати панель відповідей '''
   RadioGroupBox.hide()
   AnsGroupBox.show()
   btn_OK.setText('Наступне питання')

def show_question():
   ''' показати панель питань '''
   RadioGroupBox.show()
   AnsGroupBox.hide()
   btn_OK.setText('Відповісти')
   # скинути вибрану радіо-кнопку
   RadioGroup.setExclusive(False) # зняли обмеження, щоб можна було скинути вибір радіокнопки
   rbtn_1.setChecked(False)
   rbtn_2.setChecked(False)
   rbtn_3.setChecked(False)
   rbtn_4.setChecked(False)
   RadioGroup.setExclusive(True) # повернули обмеження, тепер лише одна радіокнопка може бути вибрана

def show_data():
   ''' показує потрібну інформацію на екрані '''
   # об'єднаємо у функцію схожі дії
   lb_Question.setText(cur_q.question)
   lb_Correct.setText(cur_q.answer)
   answer.setText(cur_q.answer)
   wrong_answer1.setText(cur_q.wrong_answer1)
   wrong_answer2.setText(cur_q.wrong_answer2)
   wrong_answer3.setText(cur_q.wrong_answer3)

def check_result():
    for answer in radio_buttons:  # перевіряємо кожен варіант
        if answer.isChecked():  # якщо вибраний радіобаттон
            if answer.text() == lb_Correct.text():  # якщо текст відповідає правильній відповіді
                cur_q.got_right()
                lb_Result.setText('Правильно')  # виводимо правильний результат
            else:
                cur_q.got_wrong()
                lb_Result.setText('Неправильно')  # виводимо неправильний результат
            break
    show_result()  # викликаємо функцію для відображення результату


def click_OK():
    if btn_OK.text() == 'Відповісти':  # якщо кнопка для відповіді
        check_result()
    elif btn_OK.text() == 'Наступне питання':  # якщо кнопка для нового питання
        new_question()
        show_question()  # відновлюємо початковий вигляд вікна

def rest():
    win_card.hide()
    wait_time = box_Minutes.value() * 60
    sleep(wait_time)
    win_card.show()

btn_Sleep.clicked.connect(rest)

def menu_show():
    menu_win.show()
    win_card.hide()

btn_Menu.clicked.connect(menu_show)

def main_show():
    menu_win.hide()
    win_card.show()

btn_back.clicked.connect(main_show)

show_data()
show_question()
btn_OK.clicked.connect(click_OK)

app.exec_()