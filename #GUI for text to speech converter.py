#GUI for text to speech converter
import tkinter as tk
import  boto3 
import os
import sys
from tempfile import gettempdir
from contextlib import closing
#GUI for text to speech converter import boto3
#importing boto3 for polly
#creating window with name root
root=tk.Tk()
#setting size of the window
root.geometry("400x400")
#window title
root.title("text to speech-amazon polly")
#creating text enter place
textEX=tk.Text(root,height=10)
#inserting text into the area
textEX.pack()
#function for running the command read

def readtext():
    #opening man console programaticly  in aws
    
    aws_mag_con=boto3.session.Session(profile_name='user1')
    #amazon polly console
    
    client=aws_mag_con.client(service_name='polly',region_name='us-east-1')
    result=textEX.get("1.0","end")
    print(result)
    #we need voice id for which voice to use
    #output format is specifying in which format we need output
    response=client.synthesize_speech(VoiceId='Joanna',OutputFormat='mp3',Text=result,Engine='neural')
    print(response)
    #to extract audio stream
    if "AudioStream" in response:
        #opening the file extracting and closing it
        #extracting the audio stream from response
        with closing(response['AudioStream']) as stream:
            #the path of the directory where the speech is stored
            output=os.path.join(gettempdir(),"speech.mp3")
            #opening the speech file
            try:
                with open(output,"wb") as file:
                    #writing the output as binary stream 
                    file.write(stream.read())
            #if  not able to open
            except IOError as error: 
                print(error) 
                sys._exit(-1)   
    else:
        print("could not find the stream")
        sys.exit(-1)  
    #opening the media player
    if sys.platform=='win32':
        #to open the file from temporary directory
        os.startfile(output)     
#create a button
btn=tk.Button(root,height=1,width=10,text="Read",command=readtext)
btn.pack()
#to keep window open
root.mainloop()