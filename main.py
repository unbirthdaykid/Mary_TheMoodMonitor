import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

primary = pd.read_csv("Stress.csv")
df_main = primary[["subreddit", "text"]].copy()

new_column = []

for i in range(len(primary)):
    extracted_strings = primary["text"].tolist()[i].lower().strip().split()
    extracted_strings_cleaned = ""
    for word in extracted_strings:
        word_cleaned = word.replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace("(", "").replace(")","").replace(
            "<", "").replace(">", "").replace("*", "").replace("_", "").replace("[", "").replace("]", "")
        if word_cleaned != "":
            extracted_strings_cleaned = word_cleaned + " " + extracted_strings_cleaned

    new_column.append(extracted_strings_cleaned)

# corpus = []

# for i in range(len(new_column)):
# for j in range(len(new_column[i])):
# if new_column[i][j] not in corpus:
# corpus.append(new_column[i][j])


df_main["parsed_words"] = new_column
df_main.drop(["text"], axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(df_main["parsed_words"], df_main["subreddit"], test_size=0.25)

v = CountVectorizer()

X_train_count = v.fit_transform(X_train)

model = MultinomialNB()
model.fit(X_train_count, Y_train)

X_test_count = v.transform(X_test)


# print(model.score(X_test_count, Y_test))


def user_input(sentence):
    new_x = [sentence]
    new_x_vectorized = v.transform(new_x)
    predict = model.predict(new_x_vectorized)
    return predict


import tkinter as tk
from tkinter import *


# hover effects
def on_enter(e):
    e.widget['background'] = '#D3D3D3'


def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'


# click command
def button_click():
    print(input_text.get())
    print(type(input_text.get()))
    input = input_text.get()
    # response = user_input(input)
    # print(response)
    # result_label.config(text=str(response[0]))
    response = str(user_input(input)[0])
    if response == 'anxiety':
        result_label.config(text='I can see you are feeling anxious. It might help to take deep breaths to calm your nerves.')
    elif response == 'ptsd':
        result_label.config(text='It sounds like you are experiencing PTSD. If you are comfortable, talk to an expert.')
    elif response == 'domesticviolence' or 'survivorsofabuse':
        result_label.config(text="It sounds like you are a victim of abuse. Please know that you do not have to face this alone.")
    elif response == 'stress':
        result_label.config(text='I can sense that you are feeling stressed. It might help to talk to someone or to try relaxation techniques.')
    elif response == 'relationships':
        result_label.config(text='I am here to support you through your relationship problems. Sometimes seeking guidance from a counselor can be helpful.')
    elif response == 'homeless' or response == 'almosthomeless':
        result_label.config(text="I'm really sorry to hear about your situation. Please know that there are organizations and shelters that can provide help.")
    elif response == 'assistance':
        result_label.config(text='I am here and willing to assist you.')
    elif response == 'food_pantry':
        result_label.config(text='Finding the nearest food banks and support programs will be helpful for you.')



# main window
win = tk.Tk()
win.geometry("1200x800")
win.title("Mary the Mood Monitor")

# background
bg = PhotoImage(file="background.png")
label1 = Label(win, image=bg)
label1.place(x=0, y=0)

# title
app_header = tk.Label(win, text="Mary the Mood Monitor👩‍⚕️", font=('Bernard MT COndensed', 50), fg='black', bg='#fad5c2')
app_header.pack(pady=70)

# label to display the result
result_label = tk.Label(win, text='Hello, how are you feeling?', bg='#fad5c2', font=('Arial', 26), fg="black")
result_label.pack(pady=80)

# app_header=tkinter.Label(win, text="input your text here", font=('Arial', 12), fg='black')
# app_header.pack(pady = 10)

# instructions
# instruction = tk.Label(win, text = 'What is on your mind?', font=('Arial', 16), bg='#fad5c2')
# instruction.pack(pady=5)

# text box
input_text = tk.Entry(win, bg="white", fg="black", font=('arial', 24), width=50)
input_text.pack(pady=20)

# button
button = tk.Button(win, text='Analyze', bd=0, bg='white', activebackground='grey', font=('arial', 16), width=15,
                   height=2, command=button_click)
button.pack(pady=80)

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)


def backend_process(number):
    pass


win.mainloop()
