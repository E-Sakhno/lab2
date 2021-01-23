#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант с использованием %f,
# требуется приведение input к типу int
print("The task: 4*100-54")
user_answer = int(input("Input your answer: "))
rigth_answer = 4*100-54
print("The right answer is %.0f" % rigth_answer)
print("Your answer is %.0f" % user_answer)
if user_answer == rigth_answer:
    print("You're right!")

# Вариант с несколькими аргументами в функции
# Требуется приведение к типу int только при сравнении значений
print("The task: 4*100-54")
user_answer = input("Input your answer: ")
rigth_answer = 4*100-54
print("The right answer is", rigth_answer)
print("Your answer is", user_answer)
if int(user_answer) == rigth_answer:
    print("You're right!")
