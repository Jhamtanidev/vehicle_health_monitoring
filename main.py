import pyaudio
import numpy as np
import soundfile as sf
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
import librosa
import matplotlib.pyplot as plt

# define parameters for recording
sampling_rate = 44100
chunk_size = 1024

def comp(old):
    file_types = (("WAV files", "*.wav"), ("All files","*.*"))
    messagebox.showinfo("Open file","Please select the first audio file.")
    file_path1 = filedialog.askopenfilename(filetypes=file_types)
    messagebox.showinfo("Open file","Please select the second audio file.")
    file_path2 = filedialog.askopenfilename(filetypes=file_types)
    old.destroy()

    y, sr = librosa.load(file_path1)
    z, sr = librosa.load(file_path2)

    # Create a time axis in seconds
    ty = librosa.times_like(y, sr=sr)
    tz = librosa.times_like(z, sr=sr)
    zre = np.interp(ty, tz, z)

    # Plot the waveform
    plt.figure(figsize=(12, 4))
    plt.plot(ty, y, alpha=0.8, color="red", label=file_path1.split("/")[-1])
    plt.plot(ty, zre, alpha=0.8, color="blue", label=file_path2.split("/")[-1])
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Waveform')
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()

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
    print("Average volume: ", avg_volume)

    # define the value chart mapping sound levels to health conditions
    value_chart = {
         0: 'Healthy,Nothing needs to be done right away. However, regular inspections should continue to guarantee that any potential problems are found quickly.',
        1: 'Slight issue,Before the issue gets worse, remedial action should be taken. This could entail doing maintenance, changing operating parameters, or replacing or repairing components.',
        2: 'Moderate issue,Potentially urgent action is required. It can be necessary to shut down the equipment or component for maintenance, and it might also need to be replaced.',
        3: 'Serious issue, immediate action is necessary to prevent catastrophic failure. The machine or component may need to be shut down immediately, and emergency repairs or replacement may be required.',
        4: 'Critical issue,immediate action is necessary to prevent catastrophic failure. The machine or component may need to be shut down immediately, and emergency repairs or replacement may be required.'

    }

    # map the sound level to a health condition using the value chart
    if avg_volume < 80:
        health_condition = value_chart[0]
    elif avg_volume < 100:
        health_condition = value_chart[1]
    elif avg_volume < 120:
        health_condition = value_chart[2]
    elif avg_volume < 150:
        health_condition = value_chart[3]
    else:
        health_condition = value_chart[4]

    # display the current health condition
    messagebox.showinfo("Vehicle Health Status","Current health condition: {}".format(health_condition))
    # close the audio stream and terminate PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()
    y, sr = librosa.load(audio_data)

    # Create a time axis in seconds
    t = librosa.times_like(y, sr=sr)

    # Plot the waveform
    plt.figure(figsize=(12, 4))
    plt.plot(t, audio_data, alpha=0.8)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Waveform')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def prerec(old):
    file_types = (("WAV files", "*.wav"), ("All files","*.*"))
    file_path = filedialog.askopenfilename(filetypes=file_types)
    old.destroy()
    audio_data, samplerate = sf.read(file_path) 

     # convert the audio data to a numpy array
    audio_data = np.concatenate(audio_data)

    # calculate the average volume level
    avg_volume = np.abs(audio_data).mean()
    print(avg_volume)

    # define the value chart mapping sound levels to health conditions
    value_chart = {
         0: 'Healthy,Nothing needs to be done right away. However, regular inspections should continue to guarantee that any potential problems are found quickly.',
        1: 'Slight issue,Before the issue gets worse, remedial action should be taken. This could entail doing maintenance, changing operating parameters, or replacing or repairing components.',
        2: 'Moderate issue,Potentially urgent action is required. It can be necessary to shut down the equipment or component for maintenance, and it might also need to be replaced.',
        3: 'Serious issue, immediate action is necessary to prevent catastrophic failure. The machine or component may need to be shut down immediately, and emergency repairs or replacement may be required.',
        4: 'Critical issue,immediate action is necessary to prevent catastrophic failure. The machine or component may need to be shut down immediately, and emergency repairs or replacement may be required.'

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
    messagebox.showinfo("Vehicle Health Status","Current health condition: {}".format(health_condition))
    y, sr = librosa.load(file_path)

    # Create a time axis in seconds
    t = librosa.times_like(y, sr=sr)

    # Plot the waveform
    plt.figure(figsize=(12, 4))
    plt.plot(t, y, alpha=0.8, label=file_path.split("/")[-1])
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Waveform')
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()

def main():
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
    no_button = Button(button_frame, text="Compare audio files", command=lambda:comp(message_box))
    no_button.pack(side=LEFT, padx=10, pady=10)
    button_frame.pack()
    message_box.mainloop()


if __name__ == "__main__":
    main()