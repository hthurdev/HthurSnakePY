import tkinter as tk
import random as rand
import time
import keyboard as kb
import FileReading as fr
##Variables and Declarations##
root = tk.Tk()
goalsnakelength = 1
root.title("Snake")
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
do_once = True
loss = False
file1 = fr.newfile("savefile.txt")

class snakehead:
    def __init__(self,x:int,y:int,direction:str):
        self.x=x
        self.y=y
        self.direction = direction

#class score:
#    def __init__(initials:str,)
        
#10x10 map of the game. 0 if empty, 1 if snake, 2 if food.
maparray = [[0,0,0,0,0,0,0,0,0,0,0]
           ,[0,0,0,0,0,0,0,0,0,0,0]
           ,[0,0,0,0,0,0,0,0,0,0,0]
           ,[0,0,0,0,0,0,0,0,0,0,0]
           ,[0,0,0,0,0,0,0,0,0,0,0]
           ,[0,0,0,0,0,0,0,0,0,0,0]
           ,[0,0,0,0,0,0,0,0,0,0,0]
           ,[0,0,0,0,0,0,0,0,0,0,0]
           ,[0,0,0,0,0,0,0,0,0,0,0]
           ,[0,0,0,0,0,0,0,0,0,0,0]
           ,[0,0,0,0,0,0,0,0,0,0,0]]

def drawmap(loss:bool):
    global do_once
    global goalsnakelength
    global file1
    if loss:
        if do_once:
            canvas.create_rectangle(0, 0, 500, 500, fill="gray",outline="white")
            text = tk.Message(root,justify="center",width=200,bd="4",text=f"You Lose! Highscore: {file1.read()}, Your Score:{goalsnakelength}")
            text.pack()
            do_once = False
            textbox = tk.Text(root)
            textbox.pack()
            button = tk.Button(root, text="Click to save score", command=lambda: file1.write(f"{goalsnakelength}","w") if (goalsnakelength>int(file1.readline(3))) else print("not high score"))
            button.pack()
    else:
        canvas.delete("reset")
        root.update()
        for i in range(10):
            for j in range(10):
                if maparray[j][i] == 1:
                    canvas.create_rectangle(i*50, j*50, i*50+50, j*50+50, fill="green",outline="green",tags="reset")
                elif maparray[j][i] == 2:
                    canvas.create_rectangle(i*50, j*50, i*50+50, j*50+50, fill="red",outline="red",tags="reset")
    root.update_idletasks()
    root.update()
    
def getdirection():
    key1 = kb.read_key(suppress=True)
    if key1 in ["up","down","left","right"]:
        return key1
    getdirection()

def opposites(string:str):
        match string:
            case "up": 
                return "down"
            case "left":
                return "right"
            case "right":
                return "left"
            case "down":
                return "up"
            
if __name__ == "__main__":
    ## initialize the snake and food position 
    snake = [[rand.randint(0,9),rand.randint(0,9)]]
    foodposition = snakehead(rand.randint(0,9),rand.randint(0,9),"None")
    
    ## 
    maparray[9-snake[0][1]][snake[0][0]] = 1
    maparray[9-foodposition.y][foodposition.x] = 2
    drawmap(loss)

    direction = getdirection()

    lastpressed = []
    lastpressed+=direction

    def senddirection(dir):
        global lastpressed
        if lastpressed[-1] != opposites(dir):
            lastpressed.append(dir)
        return lastpressed
    
    kb.add_hotkey("up", senddirection, args=["up"])
    kb.add_hotkey("down",senddirection, args=["down"])
    kb.add_hotkey("left", senddirection, args=["left"])
    kb.add_hotkey("right", senddirection, args=["right"])

    while True:
        while loss==False:
            time.sleep(0.2)
            direction = lastpressed[-1]
            match direction:
                case "up":
                    if snake[-1][1] == 9 or maparray[9-snake[-1][1]-1][snake[-1][0]] == 1:
                        loss = True
                    elif maparray[9-snake[-1][1]-1][snake[-1][0]] == 2:
                        goalsnakelength+=1                                              #
                        openlocations=[[]]                                              #
                        for x in range(10):                                             # apple replacement and growth
                            for y in range(10):                                         #
                                 if maparray[x][y]==0:                                  # 
                                     openlocations.append([x,y])                        #
                        openlocations.pop(0)                                            #
                        newcoords = rand.choice(openlocations)                          #
                        foodposition.x,foodposition.y = newcoords[0], newcoords[1]      #

                        if len(snake)<goalsnakelength:
                            snake.append([snake[-1][0],snake[-1][1]+1]) 
                        else:
                            snake.append([snake[-1][0],snake[-1][1]+1])
                            snake.pop(0)
                    else:
                        if len(snake)<goalsnakelength:
                            snake.append([snake[-1][0],snake[-1][1]+1]) 
                        else:
                            snake.append([snake[-1][0],snake[-1][1]+1])
                            snake.pop(0)
                case "down":
                    if snake[-1][1] == 0 or maparray[9-snake[-1][1]+1][snake[-1][0]] == 1:
                        loss = True

                    elif maparray[9-snake[-1][1]+1][snake[-1][0]] == 2:
                        goalsnakelength+=1                                              #
                        openlocations=[[]]                                              #
                        for x in range(10):                                             # apple replacement and growth
                            for y in range(10):                                         #
                                 if maparray[x][y]==0:                                  # 
                                     openlocations.append([x,y])                        #
                        openlocations.pop(0)                                            #
                        newcoords = rand.choice(openlocations)                          #
                        foodposition.x,foodposition.y = newcoords[0], newcoords[1]      #

                        if len(snake)<goalsnakelength:
                            snake.append([snake[-1][0],snake[-1][1]-1]) 
                        else:
                            snake.append([snake[-1][0],snake[-1][1]-1])
                            snake.pop(0)
                    else:

                        if len(snake)<goalsnakelength:
                            snake.append([snake[-1][0],snake[-1][1]-1])
                        else:
                            snake.append([snake[-1][0],snake[-1][1]-1])
                            snake.pop(0)
                case "left":
                    if snake[-1][0] == 0 or maparray[9-snake[-1][1]][snake[-1][0]-1] == 1:
                        loss = True
                    elif maparray[9-snake[-1][1]][snake[-1][0]-1] == 2:
                        goalsnakelength+=1                                              #
                        openlocations=[[]]                                              #
                        for x in range(10):                                             # apple replacement and growth
                            for y in range(10):                                         #
                                 if maparray[x][y]==0:                                  # 
                                     openlocations.append([x,y])                        #
                        openlocations.pop(0)                                            #
                        newcoords = rand.choice(openlocations)                          #
                        foodposition.x,foodposition.y = newcoords[0], newcoords[1]

                        if len(snake)<goalsnakelength:
                            snake.append([snake[-1][0]-1,snake[-1][1]])
                        else:
                            snake.append([snake[-1][0]-1,snake[-1][1]])
                            snake.pop(0)
                    else:
                        print(snake[-1][0])
                        if len(snake)<goalsnakelength:
                            snake.append([snake[-1][0]-1,snake[-1][1]])
                        else:
                            snake.append([snake[-1][0]-1,snake[-1][1]])
                            snake.pop(0)
                case "right":
                    if snake[-1][0] == 9 or maparray[9-snake[-1][1]][snake[-1][0]+1] == 1:
                        loss = True
                    elif maparray[9-snake[-1][1]][snake[-1][0]+1] == 2:
                        goalsnakelength+=1                                              #
                        openlocations=[[]]                                              #
                        for x in range(10):                                             # apple replacement and growth
                            for y in range(10):                                         #
                                 if maparray[x][y]==0:                                  # 
                                     openlocations.append([x,y])                        #
                        openlocations.pop(0)                                            #
                        newcoords = rand.choice(openlocations)                          #
                        foodposition.x,foodposition.y = newcoords[0], newcoords[1]

                        if len(snake)<goalsnakelength:
                            snake.append([snake[-1][0]+1,snake[-1][1]])
                        else:
                            snake.append([snake[-1][0]+1,snake[-1][1]])
                            snake.pop(0)
                    else:
                        print(snake[-1][0])
                        if len(snake)<goalsnakelength:
                            snake.append([snake[-1][0]+1,snake[-1][1]])
                        else:
                            snake.append([snake[-1][0]+1,snake[-1][1]])
                            snake.pop(0)

            for x in range(10):          #           
                for y in range(10):      # resets the maparray
                    maparray[x][y] = 0   #       
            for subarray in snake:                              #
                maparray[9-subarray[1]][subarray[0]] = 1        # Paints the array with snake and food values
                maparray[9-foodposition.y][foodposition.x] = 2  #
            drawmap(loss)
        drawmap(loss)