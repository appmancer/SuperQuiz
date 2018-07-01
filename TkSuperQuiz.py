import tkinter as tk
import paho.mqtt.client as mqtt
import json

#Style constants
bgColor = "#F7FFF7"
titleTextColor = "#1a535c"

#text constants
cat         = "cat"
cockerel    = "cockerel"
cow         = "cow"
dog         = "dog"
elephant    = "elephant"
goose       = "goose"
horse       = "horse"
lion        = "lion"
monkey      = "monkey"
mouse       = "mouse"
pig         = "pig"
woodpecker  = "woodpecker"

animals = [cat, cockerel, cow, dog, elephant, goose, horse, lion, monkey, mouse, pig, woodpecker]
normalImages = [ cat        : tk.PhotoImage(file="Normal/cat.png"),
                 cockerel   : tk.PhotoImage(file="Normal/cockerel.png"),
                 cow        : tk.PhotoImage(file="Normal/cow.png"),
                 dog        : tk.PhotoImage(file="Normal/dog.png"),
                 elephant   : tk.PhotoImage(file="Normal/elephant.png"),
                 goose      : tk.PhotoImage(file="Normal/goose.png"),
                 horse      : tk.PhotoImage(file="Normal/horse.png"),
                 lion       : tk.PhotoImage(file="Normal/lion.png"),
                 monkey     : tk.PhotoImage(file="Normal/monkey.png"),
                 mouse      : tk.PhotoImage(file="Normal/mouse.png"),
                 pig        : tk.PhotoImage(file="Normal/pig.png"),
                 woodpecker : tk.PhotoImage(file="Normal/woodpecker.png")]

selectedImages = [ cat        : tk.PhotoImage(file="Selected/cat.png"),
                 cockerel   : tk.PhotoImage(file="Selected/cockerel.png"),
                 cow        : tk.PhotoImage(file="Selected/cow.png"),
                 dog        : tk.PhotoImage(file="Selected/dog.png"),
                 elephant   : tk.PhotoImage(file="Selected/elephant.png"),
                 goose      : tk.PhotoImage(file="Selected/goose.png"),
                 horse      : tk.PhotoImage(file="Selected/horse.png"),
                 lion       : tk.PhotoImage(file="Selected/lion.png"),
                 monkey     : tk.PhotoImage(file="Selected/monkey.png"),
                 mouse      : tk.PhotoImage(file="Selected/mouse.png"),
                 pig        : tk.PhotoImage(file="Selected/pig.png"),
                 woodpecker : tk.PhotoImage(file="Selected/woodpecker.png")]

class QuizPlayer(tk.Label):
    def __init__(self, parent, *args, **kwargs):
        tk.Label.__init__(self, parent, *args, **kwargs)
        self.score = 0
        self.team = ''
    
class ReadyPlayerList(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.title = tk.Label(self, anchor='n', text="Contestants", bg=bgColor, padx=20, pady=10, font=("Cabin", 30), fg=titleTextColor)
        self.title.pack(side="top", anchor="n", fill="x", expand=True)
        self.activePlayers = []

    def reset:
        self.activePlayers = []

    def addPlayer(self, playerName):
        if self.activePlayers.count(playerName) == 0:
            if animals.count(playerName) > 0:
                self.activePlayers.append(playerName)
                if playerName == cat:
                    addNewPlayer(cat, self.cat)
            
        
class BuzzedInPlayerList(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.title = tk.Label(self, anchor='n', text="SuperQuiz", bg=bgColor, padx=20, pady=10, font=("Cabin", 30), fg=titleTextColor)
        self.title.pack(side="top", anchor="n", fill="x", expand=True)
        
class SuperQuiz(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.contestants = ReadyPlayerList(self, bg=bgColor)
        self.contestants.pack(side="left", anchor="n", fill="x", expand=False)
        self.answers = BuzzedInPlayerList(self, bg=bgColor)
        self.answers.pack(side="left", anchor="n", fill="x", expand="true")


    def newPlayer(self, msg):
        #adding a new player to the list
        
    def buzz(self, msg):
        
    def on_message(self, client, userdata, msg):
        route = msg.topic.split("/")
        print(route)
        node_data = msg.payload.decode("utf-8")
        j = json.loads(node_data)

        #todo - make this even vaguely object oriented
        if route[1] == 'player_registrar':
            newPlayer(j['Player'])

        elif route[1] == 'buzz':
            buzz(j)

    #MQTT events
    def on_connect(self, client, userdata, flags,rc):
        print("Connected with result code " + str(rc))

        client.subscribe("SuperQuiz/#")        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x750")
    root.title = "SuperQuiz"
    mainWindow = SuperQuiz(root, bg=bgColor)
    mainWindow.pack_propagate(0)
    mainWindow.pack(side="top", fill="both", expand=True)

    client = mqtt.Client()
    client.on_connect = mainWindow.on_connect
    client.on_message = mainWindow.on_message
    client.connect("127.0.0.1", 1883, 60)
    client.loop_forever()

    root.mainloop()

