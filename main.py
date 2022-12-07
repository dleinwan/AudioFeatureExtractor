from utils import import_audio
from utils import extract_rms
import os
import matplotlib.pyplot as plt


def main():
    audio_file_path = os.path.abspath(os.getcwd()) + '/Levitating.wav'
    audio_file_path_alt = os.path.abspath(os.getcwd()) + '/beautiful-geometry.mp3'
    print(audio_file_path)

    data, sampling_rate = import_audio(audio_file_path)

    # print(f"Data: {data} ")
    print("sampling rate: " + str(sampling_rate))

    blockSize = 256
    hopSize = 128

    rms = extract_rms(data, blockSize, hopSize, sampling_rate)
    # print("rms: " + str(rms))



    plt.figure()
    plt.subplot(3, 1, 1)
    plt.plot(data)

    plt.subplot(3, 1, 2)
    plt.plot(rms)

    plt.subplot(3, 1, 3)
    plt.specgram(data)

    plt.show()





main()
