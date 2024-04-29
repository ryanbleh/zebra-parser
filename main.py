"""
        Parse JSON that contains Zebra MotionWorks data
        Format is as follows:
        [{
            key: '2020casj_qm1',
            times: [<elapsed time (float seconds)>, 0.0, 0.5, 1.0, 1.5, ...],
            alliances: {
                red: [
                    {
                        team_key: "frc254",
                        xs: [<float feet or null>, null, 1.2, 1.3, 1.4, ...],
                        ys: [<float feet or null>, null, 0.1, 0.1, 0.1, ...],
                    },
                    {
                        team_key: "frc971",
                        xs: [1.1, 1.2, 1.3, 1.4, ...],
                        ys: [0.1, 0.1, 0.1, 0.1, ...],
                    },
                    ...
                ],
                blue: [...],
            }
        }]
"""

import requests
from graphics import *
import pygame
import json
import math

class Button:
    #Purpose: Initilizes button, Function fully rewritten for this project
    #Args: PosX, PosY, width of butotn, height of button, name of button, text on button, if button is pressed by default (by default, is false)
    #Results: None  
    def __init__(self,posX, posY, width, height, button_name, button_text ):
        self.alignedX = posX
        self.alignedY = posY
        self.button_name = button_name
        self.width = width
        self.height = height
        self.text = button_text
        self.polygon = [(self.alignedX - width / 2, self.alignedY - height / 2),(self.alignedX + width - width / 2,self.alignedY - height / 2),(self.alignedX - width / 2+ width, self.alignedY + height / 2),(self.alignedX - width / 2, self.alignedY + height / 2)]
        self.size = 0 
        self.Selected = True
        while sizeString(self.text,self.size)[1] < self.height - 30 and sizeString(self.text,self.size)[0] < self.width - 30: 
            self.size += 1

    def draw(self, world):
        if self.button_name == "red1" or self.button_name == "red2" or self.button_name == "red3": 
            fillPolygon(self.polygon, (200,0,0))
            if not self.Selected:
                fillRectangle(self.polygon[0][0] , self.polygon[0][1],self.width,10, (255,0,0))
                fillRectangle(self.polygon[0][0], self.polygon[0][1],10,self.height, (255,0,0))
                fillRectangle(self.polygon[3][0], self.polygon[3][1] - 9,self.width,10, (255,0,0))
                fillRectangle(self.polygon[1][0] - 9, self.polygon[1][1],10,self.height, (255,0,0))
            else:
                fillRectangle(self.polygon[0][0] , self.polygon[0][1],self.width,10, (0,255,0))
                fillRectangle(self.polygon[0][0], self.polygon[0][1],10,self.height, (0,255,0))
                fillRectangle(self.polygon[3][0], self.polygon[3][1] - 9,self.width,10, (0,255,0))
                fillRectangle(self.polygon[1][0] - 9, self.polygon[1][1],10,self.height, (0,255,0))
            drawString(self.text,self.alignedX - sizeString(self.text,self.size)[0] / 2 , self.alignedY - sizeString(self.text,self.size)[1] / 2 + 5, self.size, (0,0,0))
        if self.button_name == "blue1" or self.button_name == "blue2" or self.button_name == "blue3": 
            fillPolygon(self.polygon, (0,0,200))
            if not self.Selected:
                fillRectangle(self.polygon[0][0] , self.polygon[0][1],self.width,10, (0,0,255))
                fillRectangle(self.polygon[0][0], self.polygon[0][1],10,self.height, (0,0,255))
                fillRectangle(self.polygon[3][0], self.polygon[3][1] - 9,self.width,10, (0,0,255))
                fillRectangle(self.polygon[1][0] - 9, self.polygon[1][1],10,self.height, (0,0,255))
            else:
                fillRectangle(self.polygon[0][0] , self.polygon[0][1],self.width,10, (0,255,0))
                fillRectangle(self.polygon[0][0], self.polygon[0][1],10,self.height, (0,255,0))
                fillRectangle(self.polygon[3][0], self.polygon[3][1] - 9,self.width,10, (0,255,0))
                fillRectangle(self.polygon[1][0] - 9, self.polygon[1][1],10,self.height, (0,255,0))
            drawString(self.text,self.alignedX - sizeString(self.text,self.size)[0] / 2 , self.alignedY - sizeString(self.text,self.size)[1] / 2 + 5, self.size, (0,0,0))
    #Purpose: Detects where clicks occur and if they are in the area of a button, reacts accordingly 
    #Args: world
    #Results: None 
    def onClick(self,world):
        if pointInPolygon(getMousePosition()[0],getMousePosition()[1],self.polygon) == True:
            if self.button_name == "red1":
                if world.red1 == False:
                    world.red1 = True
                    self.Selected = True  
                else:
                    self.Selected = False
                    world.red1 = False
            elif self.button_name == "red2":
                if world.red2 == False:
                    world.red2 = True  
                    self.Selected = True
                else:
                    self.Selected = False
                    world.red2 = False
            elif self.button_name == "red3":
                if world.red3 == False:
                    world.red3 = True  
                    self.Selected = True
                else:
                    world.red3 = False 
                    self.Selected = False
            elif self.button_name == "blue1":
                if world.blue1 == False:
                    world.blue1 = True  
                    self.Selected = True
                else:
                    world.blue1 = False
                    self.Selected = False
            elif self.button_name == "blue2":
                if world.blue2 == False:
                    world.blue2 = True  
                    self.Selected = True
                else:
                    self.Selected = False
                    world.blue2 = False
            elif self.button_name == "blue3":
                if world.blue3 == False:
                    world.blue3 = True  
                    self.Selected = True
                else:
                    world.blue3 = False 
                    self.Selected = False
                
makeGraphicsWindow(1080,700)

def startWorld(world):

    world.red1 = True
    world.red2 = True
    world.red3 = True

    world.blue1 = True
    world.blue2 = True
    world.blue3 = True


    team_key = 'frc1540'  # Example team key
    world.match_key = '2023orore_f1m3'
    api_key = 'kgzgO1XK3IJO3Ire0au6MOGiqvX7a6oGgJ4b7v3AbEdK1fUlKQOJZOueOKmpNgGs'

    headers = {
        'X-TBA-Auth-Key': api_key
    }

    url = f'https://www.thebluealliance.com/api/v3//match/{world.match_key}/zebra_motionworks'


    print("Loading Data")
    # Make API request
    
    #f = open("/Users/ryanturner/Desktop/Python Comp Sci/moredata.json")
    #world.data = json.load(f)
    
    response = requests.get(url, headers=headers)
    world.data = response.json()
    
    #print(world.data)
    #print(len(world.data["times"]))
    print("Data loaded --> Cleaning data")
    #cleans data to be full match time
    while len(world.data["times"]) > 1501:
        world.data["times"].pop(-1)
        world.data["alliances"]["blue"][0]["xs"].pop(-1)
        world.data["alliances"]["blue"][1]["xs"].pop(-1)
        world.data["alliances"]["blue"][2]["xs"].pop(-1)
        world.data["alliances"]["red"][0]["xs"].pop(-1)
        world.data["alliances"]["red"][1]["xs"].pop(-1)
        world.data["alliances"]["red"][2]["xs"].pop(-1)
        world.data["alliances"]["blue"][0]["ys"].pop(-1)
        world.data["alliances"]["blue"][1]["ys"].pop(-1)
        world.data["alliances"]["blue"][2]["ys"].pop(-1)
        world.data["alliances"]["red"][0]["ys"].pop(-1)
        world.data["alliances"]["red"][1]["ys"].pop(-1)
        world.data["alliances"]["red"][2]["ys"].pop(-1)

    print("Data Cleaned --> Loading Buttons")

    world.bg = loadImage("bg1.png")
    world.buttons = [
                Button(90 + 405,160 / 3 + 540,100, 80, "red1",world.data["alliances"]["red"][0]["team_key"]),
                Button(90 + 300 + (2 * (100 + 5)),160 / 3 + 540, 100, 80, "red2",world.data["alliances"]["red"][1]["team_key"]),
                Button(90 + 300 + (3 * (100 + 5)),160 / 3 + 540, 100, 80, "red3",world.data["alliances"]["red"][2]["team_key"]),
                Button(90 + 300 + (4 * (100 + 5)),160 / 3 + 540, 100, 80, "blue1",world.data["alliances"]["blue"][0]["team_key"]),
                Button(90 + 300 + (5 * (100 + 5)),160 / 3 + 540, 100, 80, "blue2",world.data["alliances"]["blue"][1]["team_key"]), 
                Button(90 + 300 + (6 * (100 + 5)),160 / 3 + 540, 100, 80, "blue3",world.data["alliances"]["blue"][2]["team_key"])]

    print("Buttons Loaded --> Grid Creation Started")
    world.gridSize = 20  
    world.depthArray = {}
    for counter in range(len(world.data["times"]) - 1):
        for x in range(int(getWindowWidth() / world.gridSize + 1)):
            for y in range(int(540 / world.gridSize + 1)):
                for alliance in ["red","blue"]:
                    for i in range(3):
                        if (x * world.gridSize < world.data["alliances"][alliance][i]["xs"][counter] * 20 and (x + 1) * world.gridSize > world.data["alliances"][alliance][i]["xs"][counter] * 20 and y * world.gridSize < world.data["alliances"][alliance][i]["ys"][counter] * 20 and (y + 1) * world.gridSize > world.data["alliances"][alliance][i]["ys"][counter] * 20):
                            if str(x*world.gridSize)+"_"+str(y*world.gridSize) not in world.depthArray.keys():
                                world.depthArray[str(x*world.gridSize)+"_"+str(y*world.gridSize)] = 1
                            else: 
                                world.depthArray[str(x*world.gridSize)+"_"+str(y*world.gridSize)] += 1

    world.sortedValues = sorted(world.depthArray.values())
    print("Grids!")
def updateWorld(world):
    onMousePress(mouseListener)


def drawWorld(world):
    drawImage(world.bg, getWindowWidth() / 2,540 / 2,scale=.475)
    for xy in world.depthArray.keys():
        x,y = xy.split("_")
        #print(world.depthArray[xy])
        #print(world.depthArray[xy], world.sortedValues[-1], 0,(3, 182, 252), (3, 182, 252))
        fillRectangle(x,y,world.gridSize,world.gridSize,gradient(world.depthArray[xy], world.sortedValues[-1], world.sortedValues[0],(3, 182, 252), (171, 255, 239)))
        #print(x + " "+ y)
    for counter in range(len(world.data["times"]) - 1):
        #Red
        if world.red1:
            drawLine(world.data["alliances"]["red"][0]["xs"][counter] * 20,world.data["alliances"]["red"][0]["ys"][counter] * 20, world.data["alliances"]["red"][0]["xs"][counter + 1] * 20,world.data["alliances"]["red"][0]["ys"][counter + 1] * 20, color= (255,0,0), thickness=3)
        if world.red2:
            drawLine(world.data["alliances"]["red"][1]["xs"][counter] * 20,world.data["alliances"]["red"][1]["ys"][counter] * 20, world.data["alliances"]["red"][1]["xs"][counter + 1] * 20,world.data["alliances"]["red"][1]["ys"][counter + 1] * 20, color= (200,0,70), thickness=3)
        if world.red3:    
            drawLine(world.data["alliances"]["red"][2]["xs"][counter] * 20,world.data["alliances"]["red"][2]["ys"][counter] * 20, world.data["alliances"]["red"][2]["xs"][counter + 1] * 20,world.data["alliances"]["red"][2]["ys"][counter + 1] * 20, color= (150,0,0), thickness=3)

        #blue
        if world.blue1:
            drawLine(world.data["alliances"]["blue"][0]["xs"][counter] * 20,world.data["alliances"]["blue"][0]["ys"][counter] * 20, world.data["alliances"]["blue"][0]["xs"][counter + 1] * 20,world.data["alliances"]["blue"][0]["ys"][counter + 1] * 20, color= (0,0,255), thickness=3)
        if world.blue2:
            drawLine(world.data["alliances"]["blue"][1]["xs"][counter] * 20,world.data["alliances"]["blue"][1]["ys"][counter] * 20, world.data["alliances"]["blue"][1]["xs"][counter + 1] * 20,world.data["alliances"]["blue"][1]["ys"][counter + 1] * 20, color= (70,0,200), thickness=3)
        if world.blue3:
            drawLine(world.data["alliances"]["blue"][2]["xs"][counter] * 20,world.data["alliances"]["blue"][2]["ys"][counter] * 20, world.data["alliances"]["blue"][2]["xs"][counter + 1] * 20,world.data["alliances"]["blue"][2]["ys"][counter + 1] * 20, color= (0,0,150), thickness=3)

    if world.red1:
        fillCircle(world.data["alliances"]["red"][0]["xs"][0] * 20,world.data["alliances"]["red"][0]["ys"][0] * 20, 5, (0,255,0))
        fillCircle(world.data["alliances"]["red"][0]["xs"][-1] * 20,world.data["alliances"]["red"][0]["ys"][-1] * 20, 5, (0,0,0))
    if world.red2:
        fillCircle(world.data["alliances"]["red"][1]["xs"][0] * 20,world.data["alliances"]["red"][1]["ys"][0] * 20, 5, (0,255,0))
        fillCircle(world.data["alliances"]["red"][1]["xs"][-1] * 20,world.data["alliances"]["red"][1]["ys"][-1] * 20, 5, (0,0,0))
    if world.red3:
        fillCircle(world.data["alliances"]["red"][2]["xs"][0] * 20,world.data["alliances"]["red"][2]["ys"][0] * 20, 5, (0,255,0))
        fillCircle(world.data["alliances"]["red"][2]["xs"][-1] * 20,world.data["alliances"]["red"][2]["ys"][-1] * 20, 5, (0,0,0))
    if world.blue1:
        fillCircle(world.data["alliances"]["blue"][0]["xs"][0] * 20,world.data["alliances"]["blue"][0]["ys"][0] * 20, 5, (0,255,0))
        fillCircle(world.data["alliances"]["blue"][0]["xs"][-1] * 20,world.data["alliances"]["blue"][0]["ys"][-1] * 20, 5, (0,0,0))
    if world.blue2:
        fillCircle(world.data["alliances"]["blue"][1]["xs"][0] * 20,world.data["alliances"]["blue"][1]["ys"][0] * 20, 5, (0,255,0))
        fillCircle(world.data["alliances"]["blue"][1]["xs"][-1] * 20,world.data["alliances"]["blue"][1]["ys"][-1] * 20, 5, (0,0,0))
    if world.blue3:
        fillCircle(world.data["alliances"]["blue"][2]["xs"][0] * 20,world.data["alliances"]["blue"][2]["ys"][0] * 20, 5, (0,255,0))
        fillCircle(world.data["alliances"]["blue"][2]["xs"][-1] * 20,world.data["alliances"]["blue"][2]["ys"][-1] * 20, 5, (0,0,0))
    #for counter in range(len(world.data["times"]) - 1):
    #    drawCircle(world.data["alliances"]["red"][0]["xs"][counter] * 20,world.data["alliances"]["red"][0]["ys"][counter] * 20, 5, (255,255,255))

    fillRectangle(0,540,getWindowWidth(), getWindowHeight() - 540, (120,120,120)) 
    drawString(f"Match Code: {world.match_key}", 10, 550, font="PressStart2P-Regular", size=10)
    time = world.data["times"][len(world.data["times"]) - 1]
    drawString(f"Length of Data: {time}s/150.0s", 10, 565, font="PressStart2P-Regular", size=10)
    for button in world.buttons:
        button.draw(world)

def mouseListener(world, x, y, button): 
    for buttons in world.buttons: 
        buttons.onClick(world)

def gradient(value , maxValue , minValue , maxColor , minColor ):
    #Math made by Nico
    r = minColor[0] * ((value - minValue) / (maxValue - minValue + 0.001)) + maxColor[0] * (((maxValue - minValue) - (value - minValue)) / (maxValue - minValue + 0.001))
    g = minColor[1] * ((value - minValue) / (maxValue - minValue + 0.001)) + maxColor[1] * (((maxValue - minValue) - (value - minValue)) / (maxValue - minValue + 0.001))
    b = minColor[2] * ((value - minValue) / (maxValue - minValue + 0.001)) + maxColor[2] * (((maxValue - minValue) - (value - minValue)) / (maxValue - minValue + 0.001))
    for color in [r,g,b]:
        if color > 255:
            color = 255
        elif color < 0:
            color = 0
    return (r, g, b) 
def getInterpolatedVal(vals, time):
    timeFloor = math.floor(time);
    timeCeil = math.ceil(time);
    a = vals[timeFloor];
    b = vals[timeCeil];
    if a is None or b is None:
        return None
    
    slope = b - a;
    delta = (time - timeFloor) * slope;
    return a + delta;


runGraphics(startWorld,updateWorld,drawWorld)
#if data "none", team not in match
#if data null, no tracking data for time 
