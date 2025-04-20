#
# ************************************ Notes on Audio Processing Basics 
#  ! Audio file Format
# mp3 --> Lossy compression Format
# flac --> Lossless compression Format permit to perfectly recontract the data
# wav --> Uncompressed Format CD audio Quality
 
# ! Audio Signal Parameters
#  - Number of channels 1 or 2 number of independent audio channels
#  - sample width number of bytes
#  - framerate/sample_rate
#  - number of frames
#  - value of frames

import wave

# ! Parameters Manipulation of Audio Signal

# Parameters of the audio signal
object = wave.open('harvard.wav', 'rb') # open the file in read mode
print("number of channels: ", object.getnchannels()) # number of channels
print("sample width: ", object.getsampwidth()) # sample width in bytes  
print("frame rate: ", object.getframerate()) # frame rate in Hz
print("number of frames: ", object.getnframes()) # number of frames
print("Parameters: ", object.getparams()) # all parameters


#  Audio Signal Properties
time_Audio= object.getnframes()/object.getframerate() # time of the audio in seconds
print("Time of the audio: ", time_Audio) # time of the audio in seconds 

# Frame Types 
frames= object.readframes(-1) # read all frames
print(type(frames),type (frames[0])) 
print(len(frames))


# Saving an Audio File 
New_Audio = wave.open('new_audio.wav', 'wb') # open the file in write mode 

New_Audio.setnchannels(2) # set number of channels
New_Audio.setsampwidth(2) # set sample width in bytes
New_Audio.setframerate(44100)# set frame rate in Hz

New_Audio.writeframes(frames) # write frames to the file

New_Audio.close() # close the file

# ! Audio Signal Visualization Plotting 

import matplotlib.pyplot as plt
import numpy as np

sample_frequency= object.getframerate()
number_samples= object.getnframes()

object.close()  

# Creating a Plot 

# Preparing the data for plotting
signal_array = np.frombuffer(frames, dtype=np.int16).reshape(-1, object.getnchannels())
left_channel = signal_array[:, 0]
times= np.linspace(0,time_Audio, num= number_samples) # linspace creates an array of evenly spaced values between 0 and time_Audio

# Configuring the plot
plt.figure(figsize=(20, 4))
plt.plot(times, left_channel)
plt.title('Audio Signal')
plt.xlabel('Time [s]')  
plt.ylabel('frames')
plt.xlim(0, time_Audio) # set the x-axis limits

plt.show()


# ! Microphone Recording 

import pyaudio
# we are using PyAudio to play and record Audio 

frames_per_buffer= 3200
format= pyaudio.paInt16 # 16 bit signed integer
channels=1
rate= 16000

p= pyaudio.PyAudio() # create an instance of PyAudio

stream= p.open(
    format=format, 
    channels=channels, 
    rate=rate, 
    input=True, 
    frames_per_buffer=frames_per_buffer) # open the stream for recording

print("🎙️Recording...")


seconds= 5 
frames= [] 

for i  in range(0,int(rate/frames_per_buffer*seconds)):
    data= stream.read(frames_per_buffer) # read the data from the stream
    frames.append(data) # append the data to the frames list



stream.stop_stream() 
stream.close() 
p.terminate()


Recorded_Audio= wave.open('recorded_audio.wav', 'wb') 
Recorded_Audio.setnchannels(channels) 
Recorded_Audio.setsampwidth(p.get_sample_size(format)) 
Recorded_Audio.setframerate(rate)
Recorded_Audio.writeframes(b''.join(frames)) 
Recorded_Audio.close()



























