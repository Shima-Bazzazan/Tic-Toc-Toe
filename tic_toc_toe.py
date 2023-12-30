import sys
from functools import partial
import random
from PySide6.QtWidgets import QApplication , QMessageBox
from PySide6.QtUiTools import QUiLoader

def check():
    global player
    checklist=["X","O"]
    
    global msg_box, win_game
    for j in range(len(checklist)):
        for i in range(3):
            if  buttons[i][0].text()==checklist[j]  and buttons[i][1].text()==checklist[j] and buttons[i][2].text()==checklist[j] or\
                buttons[0][i].text()==checklist[j]  and buttons[1][i].text()==checklist[j] and buttons[2][i].text()==checklist[j] or\
                buttons[0][0].text()==checklist[j]  and buttons[1][1].text()==checklist[j] and buttons[2][2].text()==checklist[j] or\
                buttons[0][2].text()==checklist[j]  and buttons[1][1].text()==checklist[j] and buttons[2][0].text()==checklist[j] :
                msg_box=QMessageBox(text=f"player{j+1} wins!")
                win_game=1
                msg_box.show()
                if j+1==1:
                    text=main_window.xscore.text()
                    text1=text.split(":")
                    main_window.xscore.setText(f"X score: {int(text1[1])+1}")
                    player=1
                    break
                elif j+1==2:
                    text=main_window.oscore.text()
                    text1=text.split(":")
                    main_window.oscore.setText(f"O score: {int(text1[1])+1}")
                    player=2
                    break
    if len(button_clicked)==9 and win_game!=1:
            msg_box=QMessageBox(text= "Ties!")
            text=main_window.oscore.text()
            text1=text.split(":")
            main_window.tie.setText(f"Ties: {int(text1[1])+1}")
            win_game=2
            msg_box.show()
    if player==2:
        cpu()

def play(row,col):
    global player, win_game
    global buttons
    if win_game==0:
        for i in button_clicked:
            if i==buttons[row][col]:
                break
        else:
            if player==1:
                buttons[row][col].setText("X")
                buttons[row][col].setStyleSheet("color : rgb(230, 230, 0);")
                main_window.turn.setText(f"Turn: O")
                player=2  
            elif player==2:
                buttons[row][col].setText("O")
                buttons[row][col].setStyleSheet("color : rgb(142, 89, 255);")
                main_window.turn.setText(f"Turn: X")
                player=1 
            button_clicked.append(buttons[row][col])

        check() 

def about():
    about_box = QMessageBox(text = "Game Rules : you are player 1 who play as 'X' , and your opponent plays as 'O' character .\nyou can choose between player modes  by clicking on 'New Game' button \nbelow the game :\n1. player vs cpu \n2. player-1 vs player-2 ")
    about_box.setWindowTitle("Tic Tac Toe")
    about_box.exec()

def cpu():
    global win_game, player
    if main_window.cpu.isChecked() and win_game==0:
        if len(button_clicked)==0:
            btn_cpu=buttons[random.randint(0,2)][random.randint(0,2)]
            btn_cpu.setText("O")
            btn_cpu.setStyleSheet("color : rgb(142, 89, 255);")
        else:
            while True:
                btn_cpu=buttons[random.randint(0,2)][random.randint(0,2)]
                for k in button_clicked:
                    if btn_cpu==k:
                        break
                else:
                    btn_cpu.setText("O")
                    btn_cpu.setStyleSheet("color : rgb(142, 89, 255);")
                    break
        main_window.turn.setText(f"Turn: X")
        player=1 
        button_clicked.append(btn_cpu)
        check()

def new_game():
    global win_game, player
    for i in range(3):
        for j in range(3):
            buttons[i][j].setText("")
            buttons[i][j].setStyleSheet("background-color: rgb(51, 214, 206); border-radius: 10px; border-style: outset; border-width:3px; border-color: rgb(255, 255, 255);")
    button_clicked.clear()
    win_game=0
    if player==1:
        main_window.turn.setText(f"Turn: X")
    elif player==2:
        main_window.turn.setText(f"Turn: O")
    if player==2 and main_window.cpu.isChecked():
        check()

loader = QUiLoader()
app = QApplication(sys.argv)
player = 1 
win_game=0

main_window = loader.load(".\\tic_toc_toe.ui")
main_window.show()
main_window.setWindowTitle("Tic Tac Toe")


button_clicked=[]
buttons = [[main_window.btn_1 , main_window.btn_2 , main_window.btn_3], 
           [main_window.btn_4 , main_window.btn_5 , main_window.btn_6],
           [main_window.btn_7 , main_window.btn_8 , main_window.btn_9]]

for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play , i , j))
   
main_window.about.clicked.connect(about)
main_window.newgame.clicked.connect(new_game)       
app.exec()