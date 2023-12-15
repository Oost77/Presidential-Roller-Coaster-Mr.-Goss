# Roller Coaster Project Austin Faulkenburg 11-30-23
import turtle, random, Presidents, time

def draw_er(y_list, screen_width):
  i = 0
  x_spacing = (screen_width // (len(y_list))) # Gap Between Presidents
  turt.pendown()
  turt.pencolor('red')
  current_x = -screen_width // 2 - 10 
  for y in y_list: # Adding Presidents
    i += 1
    current_x += x_spacing
    turt.pencolor('red')
    if y-40 < screen_height//2:
      turt.goto(current_x, y-40)
    else: turt.goto(current_x, screen_height//2 - 5) # Off the charts!
    time.sleep(.01)
    turt.pencolor('black')
    turt.write(president_list[i][0])
  # Adding Words
  turt.penup()
  turt.goto(-900, 300)
  turt.write('Presidents rated by weight. \nWe considered rating each president by historical \nforeign/domestic policy. However we decided \nthat weight would be a superior due to \nthe powers of the excutive branch.', font=('areial', 25, 'normal'))

# Creating Window
screen = turtle.Screen()
screen.title('Presidents')
screen_width = 1800
screen_height = 900
screen.screensize(screen_width, screen_height, "white") # 1800x900 for PC, 1200x750 for laptop 

# Creating Turtle 
turt = turtle.Turtle()
turt.penup()
turt.setx(-(screen_width // 2))
turt.sety(-750//2-20)
turt.speed(8)

# Picking Presidents
president_scores = []

president_list = Presidents.presidents[0]
print(len(Presidents.presidents[0]), len(president_list))
list_name = president_list[0]
amp_factor = president_list[1]
for president in president_list: # getting minimum and maximum ranges 
  if type(president) != tuple:
    president_list.remove(president)
   
scoreing_list = []
for president in president_list: # Scores each president
  if type(president) == tuple:
    pres_score = president[1]
    scoreing_list.append(pres_score * amp_factor - (screen_height // 2))

average_score =  sum(scoreing_list) // len(scoreing_list)
new_scoring_list = []

for score in scoreing_list: # Accounts for origin point
  if score < average_score + 10:
    new_score = -abs(score - average_score)
    new_scoring_list.append(new_score)
  else:
    new_scoring_list.append(score-average_score)

draw_er(new_scoring_list, screen_width) # Draws screen

screen.mainloop()
