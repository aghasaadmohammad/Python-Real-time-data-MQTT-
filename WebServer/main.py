#!/usr/bin/env python
from datetime import datetime
import sqlite3
import paho.mqtt.client as paho
broker="192.168.178.110"

#path="D:/old/FreeLancing/rail_project/sensorsData.db"
#conn=sqlite3.connect('../sensorsData.db')
#curs=conn.cursor()

def insert(temp, hum, lux,):
    sql_insert_query = "INSERT INTO DHT_data ('temp', 'hum') VALUES (%d,%d)"%(temp,hum)
    conn.execute(sql_insert_query)
    
    sql_insert_query2 = "INSERT INTO lux_data (lux) VALUES (%d)"%(lux)
    conn.execute(sql_insert_query2)
    #version = curs.fetchone()
    conn.commit()
    #print "Records created successfully";
    conn.close()
    
def insert2(lux):
    sql_insert_query = "INSERT INTO lux_data (lux) VALUES (%d)"%(lux)
    conn.execute(sql_insert_query)
    #version = curs.fetchone()
    conn.commit()
    #print "Records created successfully";
    conn.close()
    
def on_message(client, userdata, message):
    #time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))
    msg = str(message.payload.decode("utf-8"))
    hu = msg.split(':')
    #te = msg.split(':' ,2)
    #3lu = msg.split(':' ,3)
    print(hu[1])
    
    temperture = hu[2]
    humidity = hu[1]
    lux_val = hu[3]
    
    #print(te)
    #insert(int(temperture), int(humidity),80999)
    temp = int(temperture)
    hum = int(humidity)
    #lux = int(lux_val)
    
    path="D:/old/FreeLancing/rail_project/sensorsData.db"
    conn=sqlite3.connect('../sensorsData.db')
    curs=conn.cursor()

    
    sql_insert_query = "INSERT INTO DHT_data ('temp', 'hum') VALUES (%d,%d)"%(temp,hum)
    conn.execute(sql_insert_query)
    
    #sql_insert_query2 = "INSERT INTO lux_data (lux) VALUES (%d)"%(lux)
    #conn.execute(sql_insert_query2)
    #version = curs.fetchone()
    conn.commit()
    #print "Records created successfully";
    conn.close()
    

client= paho.Client("client-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
######Bind function to callback
client.on_message=on_message
#####
print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("outTopic")#subscribe
#time.sleep(2)
print("publishing ")
#client.disconnect() #disconnect
client.loop_start() 

