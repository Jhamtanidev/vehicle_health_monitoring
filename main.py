import pyaudio
import numpy as np
import soundfile as sf
from tkinter import *

# define parameters for recording
sampling_rate = 44100
chunk_size = 1024


def rec(old):
    old.destroy()
    # create an instance of PyAudio
    p = pyaudio.PyAudio()

    # open an audio stream
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=sampling_rate,
                    input=True,
                    frames_per_buffer=chunk_size)

    # record some audio data
    print('Recording...')
    num_chunks = 100
    audio_data = []
    for i in range(num_chunks):
        data = stream.read(chunk_size)
        audio_data.append(np.frombuffer(data, dtype=np.int16))

    # convert the audio data to a numpy array
    audio_data = np.concatenate(audio_data)

    # calculate the average volume level
    avg_volume = np.abs(audio_data).mean()

    # define the value chart mapping sound levels to health conditions
    value_chart = {
        0: 'Healthy',
        1: 'Slight issue',
        2: 'Moderate issue',
        3: 'Serious issue',
        4: 'Critical issue'
    }

    # map the sound level to a health condition using the value chart
    if avg_volume < 500:
        health_condition = value_chart[0]
    elif avg_volume < 1000:
        health_condition = value_chart[1]
    elif avg_volume < 2000:
        health_condition = value_chart[2]
    elif avg_volume < 3000:
        health_condition = value_chart[3]
    else:
        health_condition = value_chart[4]

    # display the current health condition
    print('Current health condition: ', health_condition)

    # close the audio stream and terminate PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()

def prerec(old):
    old.destroy()
    audio_data, samplerate = sf.read('bad.wav') 

     # convert the audio data to a numpy array
    audio_data = np.concatenate(audio_data)

    # calculate the average volume level
    avg_volume = np.abs(audio_data).mean()

    # define the value chart mapping sound levels to health conditions
    value_chart = {
        0: 'Healthy',
        1: 'Slight issue',
        2: 'Moderate issue',
        3: 'Serious issue',
        4: 'Critical issue'
    }

    # map the sound level to a health condition using the value chart
    if avg_volume < 500:
        health_condition = value_chart[0]
    elif avg_volume < 1000:
        health_condition = value_chart[1]
    elif avg_volume < 2000:
        health_condition = value_chart[2]
    elif avg_volume < 3000:
        health_condition = value_chart[3]
    else:
        health_condition = value_chart[4]

    # display the current health condition
    print('Current health condition:', health_condition)

def show_custom_message_box():
    # Create a new window for the message box
    message_box = Tk()
    message_box.geometry("480x120+720+480")
    message_box.title("Type of input")

    # Add a label to display the message
    message_label = Label(message_box, text="Would you like to upload an audio file or record real time audio?")
    message_label.pack(padx=10, pady=10)

    # Add "Yes" and "No" buttons to the message box
    button_frame = Frame(message_box)
    yes_button = Button(button_frame, text="Upload audio file", command=lambda:prerec(message_box))
    yes_button.pack(side=LEFT, padx=10, pady=10)
    no_button = Button(button_frame, text="Record audio", command=lambda:rec(message_box))
    no_button.pack(side=LEFT, padx=10, pady=10)
    button_frame.pack()
    message_box.mainloop()

def main():
    show_custom_message_box()


if __name__ == "__main__":
    main()