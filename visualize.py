import pyaudio
import numpy as np

import soundfile as sf


# define parameters for recording
sampling_rate = 44100
chunk_size = 1024

choice = int(input("Enter 1 for uploading an audio file and 2 for real time audio recording:"))
if choice==2:
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
    num_chunks = 10
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
    print('Current health condition:', health_condition)

    # close the audio stream and terminate PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()

else:
    audio_data, samplerate = sf.read(r'bad.wav') 

     # convert the audio data to a numpy array
    audio_data = np.concatenate(audio_data)

    # calculate the average volume level
    avg_volume = np.abs(audio_data).mean()

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
    print('Current health condition:', health_condition)