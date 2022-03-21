"""
MIT License

Copyright (c) 2022 lalithakalle

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import random
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap


def make_uppercase(word):
    return word.capitalize()

def add_number(word):
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    w1 = word[:len(word)//2]
    w2 = word[len(word)//2:]
    return w1 + random.choice(number) + w2

def generate_password(word1, word2, word3):
    special = ['!', '@', '#', '$', '%', '^', '&', '*']
    m_word1 = make_uppercase(word1)
    m_word1 = add_number(m_word1)

    m_word2 = make_uppercase(word2)
    m_word2 = add_number(m_word2)

    m_word3 = make_uppercase(word3)
    m_word3 = add_number(m_word3)

    final_password = m_word1 + random.choice(special) + m_word2 + random.choice(special) + m_word3 + random.choice(special)
    return final_password

def dumb_one(word1, word2, word3):
    return word1 + word2 + word3

def dumb_two(word1, word2, word3):
    special = ['!', '@', '#', '$', '%', '^', '&', '*']
    return word1 + random.choice(special) + word2 + random.choice(special) + word3 + random.choice(special)

def dumb_three(word1, word2, word3):
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    return word1 + random.choice(number) + word2 + random.choice(number) + word3 + random.choice(number)\

def dumb_four(word1, word2, word3):
    m_word1 = make_uppercase(word1)
    m_word2 = make_uppercase(word2)
    m_word3 = make_uppercase(word3)
    return m_word1 + m_word2 + m_word3

def dumb_five(word1):
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    return word1 + random.choice(number)

def dumb_six(word2):
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    return word2 + random.choice(number)

def dumb_seven(word3):
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    return word3 + random.choice(number)

def commonly_usedP(word1, word2, word3):
    return dumb_five(word1) + " or " + dumb_six(word2) + " or " + dumb_seven(word3)

def dumb_nine(word1, word2, word3):
    return '"' + word1 + "123" + '"' + " or " + '"' + word2 + "123" + '"' + " or " + '"' + word3 + "123" + '"'

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/", methods = ['POST'])
def show_password():
    passwords = []
    word1 = request.form['word1']
    word2 = request.form['word2']
    word3 = request.form['word3']

    strong_password = generate_password(word1, word2, word3)
    dumb_password1 = dumb_one(word1, word2, word3)
    dumb_password2 = dumb_two(word1, word2, word3)
    dumb_password3 = dumb_three(word1, word2, word3)
    dumb_password4 = dumb_four(word1, word2, word3)
    dumb_password5 = commonly_usedP(word1, word2, word3)
    dumb_password6 = dumb_nine(word1, word2, word3)

    passwords.append(strong_password)
    passwords.append(dumb_password1)
    passwords.append(dumb_password2)
    passwords.append(dumb_password3)
    passwords.append(dumb_password4)
    passwords.append(dumb_password5)
    passwords.append(dumb_password6)

    return render_template("index.html", passwords=passwords)


