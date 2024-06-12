#!/usr/bin/env python3

import time
import random
import tkinter as tk
from tkinter import ttk

def calculate_horrorscope():
	month_str = month_combobox.get()
	if not month_str:
		print("Debug: No month entered") 
		error_label.config(text="Please select a month.")
		return
	else:
		error_label.config(text="") 
		if month_str == "January":
			monthsnum = 1
		elif month_str == "February":
			monthsnum = 2
		elif month_str == "March":
			monthsnum = 3
		elif month_str == "April":
			monthsnum = 4
		elif month_str == "May":
			monthsnum = 5
		elif month_str == "June":
			monthsnum = 6
		elif month_str == "July":
			monthsnum = 7
		elif month_str == "August":
			monthsnum = 8
		elif month_str == "September":
			monthsnum = 9
		elif month_str == "October":
			monthsnum = 10
		elif month_str == "November":
			monthsnum = 11
		elif month_str == "December":
			monthsnum = 12

	daystr = (day_combobox.get())
	if not daystr:
		print("Debug: No day entered") 
		error_label.config(text="Please enter a valid number for the date.")
		return

	else:
		day = int(daystr) 
		error_label.config(text="") 
	
	yearstr = (year_combobox.get())
	if not yearstr:
		print("Debug: No year entered") 
		error_label.config(text="Please enter a valid number for the year.")
		return
	else:
		year = int(yearstr) 
		error_label.config(text="") 
	
	month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	num = sum(month_days[:monthsnum-1]) + day
	
	if num >= 20 and num <= 49:
		sign = "Aquarius"
	elif num >= 50 and num <= 79:
		sign = "Pisces"
	elif num >= 80 and num <= 109:
		psign = "Aries"
	elif num >= 100 and num <= 140:
		sign = "Taurus"
	elif num >= 141 and num <= 171:
		sign = "Gemini"
	elif num >= 172 and num <= 203:
		sign = "Cancer"
	elif num >= 204 and num <= 234:
		sign = "Leo"
	elif num >= 235 and num <= 265:
		sign = "Virgo"
	elif num >= 266 and num <= 295:
		sign = "Libra"
	elif num >= 296 and num <= 325:
		sign = "Scorpio"
	elif num >= 326 and num <= 355:
		sign = "Sagittarius"
	elif (num >= 356 and num <= 365) or (num >= 1 and num <= 19):
		sign = "Capricorn"
		
	horrorscope = random.choice(horror)
	if num >= 1 and num <= 365:
		month_combobox.pack_forget()
		day_combobox.pack_forget()
		year_combobox.pack_forget()
		month_label.pack_forget()
		day_label.pack_forget()
		year_label.pack_forget()
		calculate_button.pack_forget()
		
		sign_label.config(text=f"You are a {sign}.")
		horror_label.config(text=f"Your horrorscope is: {horrorscope}")
		print("Debug: Script completed successfully.")
		
	else:
		error_label.config(text="That is not a real date. Please correct your birthday.")
		print("Debug: Not a valid date.")

horror = [
	"You will die a horrible death by way of your family.",
	"You will win a million dollars in the lottery, and then get robbed.",
	"One of your loved ones will get kidnapped, and you will have to pay for their freedom.",
	"You will be run over by a train when crossing the tracks.",
	"You will be delayed by a canceled light rail train on your way to your dream job interview.",
	"Your significant other will cheat on you and will leave you homeless.",
	"You will run into your kindergarten teacher and have an awkward conversation with them.",
	"You will be in a car crash on the highway, and your car will be totaled.",
	"You will win the lottery when it is at a all-time high.",
	"While playing chess, your chair will break and you will fall and break both your legs",
	"Your parents will get a divorce.",
	"Your sibling will annoy you every waking moment of your day.",
	"Your parents are having another child, and they will be the most annoying younger sibling ever.",
	"You will run into your high school bully from 10 years ago, and he will beat you up like he used to.",
	"You will finally gain enough courage to ask the love of your life out, only for them to say no."
]

root = tk.Tk()
root.title("Horrorscope")
root.geometry("700x200")

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

days = list(range(1, 32))
years = list(range(0, 2025))
years.reverse()

error_label = tk.Label(root, text="", fg="red")  
error_label.pack()

month_label = tk.Label(root, text="Month:")
month_label.pack()
month_combobox = ttk.Combobox(root, values=months, state="readonly")
month_combobox.pack()
day_label = tk.Label(root, text="Day:")
day_label.pack()
day_combobox = ttk.Combobox(root, values=days)
day_combobox.pack()

year_label = tk.Label(root, text="Year:")
year_label.pack()
year_combobox = ttk.Combobox(root, values=years)
year_combobox.pack()

calculate_button = tk.Button(root, text="Find Your Horrorscope!", command=calculate_horrorscope)
calculate_button.pack()

sign_label = tk.Label(root, text="")
sign_label.pack()

horror_label = tk.Label(root, text="")
horror_label.pack()

root.mainloop()