import sys
from pprint import pprint
s, n = map(int, sys.stdin.readline().split())
# 가로 s+2, 세로 2s+3
# s = 2 인 경우 가로 4, 세로 7

width = s + 2
height = 2 * s + 3
#   그냥 공백
b0 = " " * width + " "
# --
b1 = " " + "-" * s + " " + " "
# |
h1 = "|" + " "*(width-1) + " "
# |  |
h2 = "|" + " "*s + "|" + " "
#    |
h3 = " "*(width-1) + "|" + " "


def zero(idx):
    global lcd
    tmp = []
    tmp.append(b1)
    for i in range(s):
        tmp.append(h2)
    tmp.append(b0)
    for i in range(s):
        tmp.append(h2)
    tmp.append(b1)
    lcd.append(tmp)


def one(idx):
    global lcd
    tmp = []
    tmp.append(b0)
    for i in range(s):
        tmp.append(h3)
    tmp.append(b0)
    for i in range(s):
        tmp.append(h3)
    tmp.append(b0)
    lcd.append(tmp)


def two(idx):
    global lcd
    tmp = []
    tmp.append(b1)
    for i in range(s):
        tmp.append(h3)
    tmp.append(b1)
    for i in range(s):
        tmp.append(h1)
    tmp.append(b1)
    lcd.append(tmp)


def three(idx):
    global lcd
    tmp = []
    tmp.append(b1)
    for i in range(s):
        tmp.append(h3)
    tmp.append(b1)
    for i in range(s):
        tmp.append(h3)
    tmp.append(b1)
    lcd.append(tmp)


def four(idx):
    global lcd
    tmp = []
    tmp.append(b0)
    for i in range(s):
        tmp.append(h2)
    tmp.append(b1)
    for i in range(s):
        tmp.append(h3)
    tmp.append(b0)
    lcd.append(tmp)


def five(idx):
    global lcd
    tmp = []
    tmp.append(b1)
    for i in range(s):
        tmp.append(h1)
    tmp.append(b1)
    for i in range(s):
        tmp.append(h3)
    tmp.append(b1)
    lcd.append(tmp)


def six(idx):
    global lcd
    tmp = []
    tmp.append(b1)
    for i in range(s):
        tmp.append(h1)
    tmp.append(b1)
    for i in range(s):
        tmp.append(h2)
    tmp.append(b1)
    lcd.append(tmp)


def seven(idx):
    global lcd
    tmp = []
    tmp.append(b1)
    for i in range(s):
        tmp.append(h3)
    tmp.append(b0)
    for i in range(s):
        tmp.append(h3)
    tmp.append(b0)
    lcd.append(tmp)


def eight(idx):
    global lcd
    tmp = []
    tmp.append(b1)
    for i in range(s):
        tmp.append(h2)
    tmp.append(b1)
    for i in range(s):
        tmp.append(h2)
    tmp.append(b1)
    lcd.append(tmp)

def nine(idx):
    global lcd
    tmp = []
    tmp.append(b1)
    for i in range(s):
        tmp.append(h2)
    tmp.append(b1)
    for i in range(s):
        tmp.append(h3)
    tmp.append(b1)
    lcd.append(tmp)


str_n = str(n)
lcd = []
for i in range(len(str_n)):
    if str_n[i] == "0":
        zero(i)
    elif str_n[i] == "1":
        one(i)
    elif str_n[i] == "2":
        two(i)
    elif str_n[i] == "3":
        three(i)
    elif str_n[i] == "4":
        four(i)
    elif str_n[i] == "5":
        five(i)
    elif str_n[i] == "6":
        six(i)
    elif str_n[i] == "7":
        seven(i)
    elif str_n[i] == "8":
        eight(i)
    elif str_n[i] == "9":
        nine(i)


for i in range(height):
    for k in range(len(str_n)):
        print(lcd[k][i], end='')
    print()
# pprint(lcd)