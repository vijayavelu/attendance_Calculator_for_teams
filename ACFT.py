import tkinter as tk
import pandas as pd
from tkinter import StringVar, ttk, filedialog

window = tk.Tk()
window.title("Attendance Calculator for Teams") # to define the title

canvas1 = tk.Canvas(window, width = 400, height = 620)
canvas1.pack()

label10 = tk.Label(window, text = "Attendance Calculator")
label10.config(font=("Comic Sans MS", 32))
canvas1.create_window(200, 50, window = label10)

#Getting Start time input from user
label1 = tk.Label(window, text = "Enter Start Time: ")
canvas1.create_window(200, 85, window = label1)

clicked1 = StringVar(window)
drop1 = ttk.Combobox(window , width = 3, textvariable = clicked1)
drop1['values'] = tuple(range(0,13))
drop1.set('00')
canvas1.create_window(145, 110, window = drop1)

label4 = tk.Label(window, text = ":")
canvas1.create_window(170, 110, window = label4)

clicked2 = StringVar(window)
drop2 = ttk.Combobox(window , width = 3, textvariable = clicked2)
drop2['values'] = tuple(range(0,60))
drop2.set('00')
canvas1.create_window(195, 110, window = drop2)

label5 = tk.Label(window, text = ":")
canvas1.create_window(220, 110, window = label5)

clicked3 = StringVar(window)
drop3 = ttk.Combobox(window , width = 3, textvariable = clicked3)
drop3['values'] = tuple(range(0,60))
drop3.set('00')
canvas1.create_window(245, 110, window = drop3)

clicked4 = StringVar(window)
drop4 = ttk.Combobox(window , width = 4, textvariable = clicked4)
drop4['values'] = ('AM', 'PM')
drop4.set('AM')
canvas1.create_window(290, 110, window = drop4)

text_Starttime = u'\u24D8' + " Enter the start time of the class meeting in this format: HH:MM:SS.\nFor Example, 10:30:00 AM"
label7 = tk.Label(window, text = text_Starttime)
canvas1.create_window(200, 140, window = label7)

#Getting Stop time input from user
label2 = tk.Label(window, text = "Enter Stop Time: ")
canvas1.create_window(200, 185, window = label2)

clicked5 = StringVar(window)
drop5 = ttk.Combobox(window , width = 3, textvariable = clicked5)
drop5['values'] = tuple(range(0,13))
drop5.set('00')
canvas1.create_window(145, 210, window = drop5)

label5 = tk.Label(window, text = ":")
canvas1.create_window(170, 210, window = label5)

clicked6 = StringVar(window)
drop6 = ttk.Combobox(window , width = 3, textvariable = clicked6)
drop6['values'] = tuple(range(0,60))
drop6.set('00')
canvas1.create_window(195, 210, window = drop6)

label6 = tk.Label(window, text = ":")
canvas1.create_window(220, 210, window = label6)

clicked7 = StringVar(window)
drop7 = ttk.Combobox(window , width = 3, textvariable = clicked7)
drop7['values'] = tuple(range(0,60))
drop7.set('00')
canvas1.create_window(245, 210, window = drop7)

clicked8 = StringVar(window)
drop8 = ttk.Combobox(window , width = 4, textvariable = clicked8)
drop8['values'] = ('AM', 'PM')
drop8.set('AM')
canvas1.create_window(290, 210, window = drop8)

text_Stoptime =  u'\u24D8' + " Enter the stop time of the class meeting in this format: HH:MM:SS.\nFor Example, 12:30:00 PM"
label8 = tk.Label(window, text = text_Stoptime)
canvas1.create_window(200, 240, window = label8)

#Getting Threshold Percentage from the user
label3 = tk.Label(window, text = "Enter Threshold Percentage: ")
canvas1.create_window(200, 285, window = label3)
entry3 = tk.Entry(window, width = 5)
entry3.insert(50,'90')
canvas1.create_window(200, 310, window = entry3)

text_thres =  u'\u24D8' + " Enter the percentage of time that a student should have\nspent in the meeting to be given attendance(0 - 100).\nFor Example - 75.\nRecommended threshold - 90"
label9 = tk.Label(window, text = text_thres)
canvas1.create_window(200, 360, window = label9)

#Calculating time difference between joined and left time in seconds
def difftime(a,b):
    a = a.split(":")
    b = b.split(":")
    if b[-1][-2].upper() == "P":
        b[0] = str(int(b[0]) + 12)
    if a[-1][-2].upper() == "P":
        a[0] = str(int(a[0]) + 12)
    return (int(b[0]) - int(a[0]))*3600 + (int(b[1]) - int(a[1]))*60 + int(b[2][:2]) - int(a[2][:2])

#Minimum time calculation for setting start and end time for individual students
def minitime(a,b):
    a = a.split(":")
    b = b.split(":")
    if b[-1][-2].upper() == "P" and a[-1][-2].upper() == "A":
        return True
    elif (b[-1][-2].upper() == "P" and a[-1][-2].upper() == "P") or (b[-1][-2].upper() == "A" and a[-1][-2].upper() == "A"):
        if int(a[0]) < int(b[0]):
            return True
        elif int(a[0]) == int(b[0]):
            if int(a[1]) < int(b[1]):
                return True
            elif int(a[1]) == int(a[1]):
                if int(a[2][:2]) < int(b[2][:2]) or int(a[2][:2]) == int(b[2][:2]):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def browse_file1():
    global file1
    file1 = filedialog.askopenfilename()
    text_file1 = "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
    label16 = tk.Label(window, text = text_file1)
    label16.config(font=("Helvetica", 8))
    canvas1.create_window(200, 505, window = label16)
    text_file1 = "Attendance Calculation File Path: " + file1
    label16 = tk.Label(window, text = text_file1)
    label16.config(font=("Helvetica", 8))
    canvas1.create_window(200, 505, window = label16)
    print(file1)

def browse_file2():
    global file2
    file2 = filedialog.askopenfilename()
    text_file2 = "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
    label17 = tk.Label(window, text = text_file2)
    label17.config(font=("Helvetica", 8))
    canvas1.create_window(200, 525, window = label17)
    text_file2 = "Date File Path: " + file2
    label17 = tk.Label(window, text = text_file2)
    label17.config(font=("Helvetica", 8))
    canvas1.create_window(200, 525, window = label17)
    print(file2)

def compute():
    df1 = pd.read_excel(file1)
    path = file1
    df2 = pd.read_csv(file2)
    date = file2.split('/')[-1].split('.')[0]
    print(df1)
    print(df2)

    h = clicked1.get()
    m = clicked2.get()
    s = clicked3.get()
    t = clicked4.get()
    if len(h) == 1:
        h = "0" + str(h)
    if len(m) == 1:
        m = "0" + str(m)
    if len(s) == 1:
        s = "0" + str(s)
    start_time = h + ":" + m + ":" + s + " " + t
    print(start_time)

    h = clicked5.get()
    m = clicked6.get()
    s = clicked7.get()
    t = clicked8.get()
    if len(h) == 1:
        h = "0" + str(h)
    if len(m) == 1:
        m = "0" + str(m)
    if len(s) == 1:
        s = "0" + str(s)
    end_time = h + ":" + m + ":" + s + " " + t
    print(end_time)

    thers = entry3.get()
    print(thers)
    print(date)

    stud_attend = {}.fromkeys(df2["Full Name"])
    for i in stud_attend:
        i.strip(" ").upper

    #Timestamp extraction for individual students
    l = []
    for i in stud_attend:
        for j in range(0,len(df2["Full Name"])):
            if i == df2["Full Name"][j]:
                l.append(df2["Timestamp"][j].split(",")[1].lstrip(" "))
        stud_attend[i] = l
        l = []

    #Calculate difference between every joining and left time and calculate whether the person is present for given threshold
    #True if he is present and False, if he is absent
    tot_time = difftime(start_time, end_time)

    #If the person not attended meeting itself means set False for that person
    for i in stud_attend:
        sumtime = 0
        x = stud_attend[i]
        if not (minitime(x[0],start_time)):
            x[0] = start_time
        if (len(x) % 2) == 0 and minitime(end_time,x[-1]):
            x[-1] = end_time
        if (len(x) % 2) != 0:
            x.append(end_time)
        for j in range(0, len(x), 2):
            sum_time = difftime(x[j], x[j+1])
        if sum_time >= eval(thers)*tot_time / 100:
            stud_attend[i] = True
        else:
            stud_attend[i] = False


    #Empty column creation for the person to append the attendance list created
    for i in df1["FULL NAME"]:
        if i.upper().strip(" ") not in stud_attend:
            stud_attend[i.upper().strip(" ")] = False

    #Empty column creation for the person to append the attendance list created
    df1[date] = list(range(0, len(df1["FULL NAME"])))

    #For each person put the value True or False according to rules defined above
    d = list(df1["FULL NAME"])

    for i in d:
      df1[date][d.index(i)] = stud_attend[i.upper().strip(" ")]
      print(stud_attend[i.upper().strip("s ")])

    #Get the xlsx file and save it for future use
    df1.to_excel(path, index = False)

    print(df1)
    print(df2)
    print(start_time)
    print(end_time)
    print(thers)

    print('\nDone and Dusted')

button1 = tk.Button(text = 'Upload Attendance calculation file', command = browse_file1, bg = 'brown',fg = 'white', activebackground='green')
canvas1.create_window(150, 410, window = button1)

button2 = tk.Button(text = 'Upload Date file', command = browse_file2, bg = 'brown',fg = 'white', activebackground='green')
canvas1.create_window(300, 410, window = button2)

text_button1 =  u'\u24D8' + " Click the *Upload Attendance calculation file* button to upload the excel file\ncontaining the names of all the students of that paper or subject"
label11 = tk.Label(window, text = text_button1)
canvas1.create_window(200, 440, window = label11)

text_button2 =  u'\u24D8' + " Click the *Upload Date file* button to upload the csv file\nof a particular day's class meeting attendance"
label14 = tk.Label(window, text = text_button2)
canvas1.create_window(200, 475, window = label14)

button3 = tk.Button(text = 'Submit', command = compute, bg = 'brown',fg = 'white', activebackground='green')
canvas1.create_window(200, 550, window = button3)

text_button3 =  u'\u24D8' + " Click the above button to calculate Attendance"
label15 = tk.Label(window, text = text_button3)
canvas1.create_window(200, 570, window = label15)

text_copyright1 =  "App created by Vijayavelu SS and Rajeshwaran R for calculating attendance in a Microsoft Teams meeting"
label12 = tk.Label(window, text = text_copyright1)
label12.config(font=("Comic Sans MS", 8))
canvas1.create_window(200, 600, window = label12)

text_copyright2 =  u'\u00a9' + "Copyright 2020-2021 Vijayavelu SS and Rajeshwaran R"
label13 = tk.Label(window, text = text_copyright2)
label13.config(font=("Comic Sans MS", 12))
canvas1.create_window(200, 625, window = label13)

window.geometry("650x650")
window.mainloop()
