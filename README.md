# 🗺️ U.S. States Guessing Game

A fun, interactive Python game built with the **Turtle graphics** module and **Pandas**!  
Your goal: **Guess all 50 U.S. states** by typing their names on the map.  
Each correct guess is written on the map at its correct coordinates. 🇺🇸

---

## 🎮 How It Works

- You start with a blank map of the United States.  
- The program will ask you to **guess the name of a state**.  
- If your guess is correct, the name appears on the map at its proper location (based on x/y coordinates).  
- The game keeps track of how many states you’ve guessed correctly.  
- When you finish (or type "Exit"), a file will be created showing the **states you missed**.

---

## 🧩 Features

- 🗺️ Interactive map of the United States  
- 🧠 Educational — learn U.S. geography while playing  
- 🧮 Uses **Pandas** for CSV data handling (state names + coordinates)  
- 🐢 Uses **Turtle Graphics** for drawing text on the map  
- 📜 Saves unguessed states to a CSV file for review  

---

## 🧠 Game Logic

Each state’s position is read from the 50_states.csv file

```csv
state,x,y
Alabama,139,-77
Alaska,-204,-170
Arizona,-203,-40
...
Wyoming,-134,90
