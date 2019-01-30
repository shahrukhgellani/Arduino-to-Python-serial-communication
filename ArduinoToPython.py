import serial as s
import time
import numpy as n

arduinoData = s.Serial('/dev/ttyACM2',  baudrate=9600, timeout=1.0)
'''def receiveData():
    if(s.available()
    msg = arduino.readline()
    print ("Message from arduino: ")
    print (msg)
receiveData()'''

while True: # While loop that loops forever
    while (arduinoData.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    arduinoString = arduinoData.readline() #read the line of text from the serial port
    arduinoInt = (arduinoString[0:-2])
    #milimeters = miliseconds * 343000
    if(int(arduinoString[0:-2])> int(500)):
        print("microseconds 400 : " + arduinoInt)
        arduinoData.write('H'.encode())
    elif(int(arduinoString[0:-2]) < int(500)):
        arduinoData.write('L'.encode())
    #print("Higher and equal to 500 : " + str(arduinoString[0:-2]))
    
    
    
    
    #print(str(arduinoString))
    #dataArray = arduinoString.split(',')   #Split it into an array called dataArray
    #temp = float( dataArray[0])            #Convert first element to floating number and put in temp
    #P =    float( dataArray[1])            #Convert second element to floating number and put in P
    #tempF.append(temp)                     #Build our tempF array by appending temp readings
    #pressure.append(P)                     #Building our pressure array by appending P readings
    #drawnow(makeFig)                       #Call drawnow to update our live graph
    #plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
    #cnt=cnt+1
    #if(cnt>50):                            #If you have 50 or more points, delete the first one from the array
        #tempF.pop(0)                       #This allows us to just see the last 50 data points
        #pressure.pop(0)
	
