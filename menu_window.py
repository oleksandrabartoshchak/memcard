from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit

menu_win = QWidget()
menu_win.setWindowTitle('Меню')
menu_win.resize(550, 450)

lb_question = QLabel('Введіть запитання:')
lb_right_ans = QLabel('Введіть правильну відповідь:')
lb_wrong_ans1 = QLabel('Введіть 1 неправильну відповідь:')
lb_wrong_ans2 = QLabel('Введіть 2 неправильну відповідь:')
lb_wrong_ans3 = QLabel('Введіть 3 неправильну відповідь:')

le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

lb_stat = QLabel('Статистика')

vl_label = QVBoxLayout()
vl_label.addWidget(lb_question)
vl_label.addWidget(lb_right_ans)
vl_label.addWidget(lb_wrong_ans1)
vl_label.addWidget(lb_wrong_ans2)
vl_label.addWidget(lb_wrong_ans3)

vl_lineEdits = QVBoxLayout()
vl_lineEdits.addWidget(le_question)
vl_lineEdits.addWidget(le_right_ans)
vl_lineEdits.addWidget(le_wrong_ans1)
vl_lineEdits.addWidget(le_wrong_ans2)
vl_lineEdits.addWidget(le_wrong_ans3)

hl_question = QHBoxLayout()
hl_question.addLayout(vl_label)
hl_question.addLayout(vl_lineEdits)

btn_back = QPushButton('Назад')
btn_add = QPushButton('Додати запитання')
btn_clear = QPushButton('Очистити')

hl_btns = QHBoxLayout()
hl_btns.addWidget(btn_add)
hl_btns.addWidget(btn_clear)

main_vl = QVBoxLayout()
main_vl.addLayout(hl_question)
main_vl.addLayout(hl_btns)
main_vl.addWidget(lb_stat)
main_vl.addWidget(btn_back)

menu_win.setLayout(main_vl)