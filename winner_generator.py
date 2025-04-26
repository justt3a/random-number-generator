from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

from random import randint 

app = QApplication([])
window = QWidget()
window.setWindowTitle('Lottery')
window.move(100, 100)
window.resize(400, 200)

text = QLabel('The number of the winner:')
winner = QLabel('?')
button = QPushButton('Generate')

line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
window.setLayout(line)

#freaking button\

def show_win():
    number = randint(0, 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
    number = str(number)
    winner.setText(number)
    
button.clicked.connect(show_win)

window.show()
app.exec_() #leave the app opened
