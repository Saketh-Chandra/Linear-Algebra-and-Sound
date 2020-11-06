# Author : B Saketh Chandra
# more info : https://github.com/Saketh-Chandra


import numpy as np
from scipy.io.wavfile import write, read
from scipy import signal as sg
from numpy import sin, cos, e
import matplotlib.pyplot as plt
from playsound import playsound
from subprocess import Popen
import os
# Author

def create_wave_sin(freq_Hz=10000.0, duration_S=5.0, volume=0.3):
    sps = 44100  # Samples per second(sps)
    each_sample_number = np.arange(duration_S * sps)
    waveform = np.sin(2 * np.pi * each_sample_number * freq_Hz / sps)
    waveform_quiet = waveform * volume
    waveform_integers = np.int16(waveform_quiet * 32767)  # integer because making its digital signal
    file_name = f'sine_wave(sin(x))-{freq_Hz}Hz.wav'
    write(file_name, sps, waveform_integers)  # Write the .wav file
    return file_name


def create_wave_cos(freq_Hz=10000.0, duration_S=5.0, volume=0.3):
    sps = 44100  # Samples per second(sps)
    π = np.pi
    each_sample_number = np.arange(duration_S * sps)
    θ = (2 * π * each_sample_number * freq_Hz / sps)
    # print(θ)
    waveform = np.cos(θ)
    waveform_quiet = waveform * volume
    # print(waveform_quiet)
    waveform_integers = np.int16(waveform_quiet * 32767)  # integer because making its digital signal
    file_name = f'cose_wave{freq_Hz}Hz.wav'
    write(file_name, sps, waveform_integers)  # Write the .wav file
    return file_name


def create_wave_squ(freq_Hz=10000.0, duration_S=5.0, volume=0.3):
    sps = 44100  # Samples per second(sps)
    π = np.pi
    each_sample_number = np.arange(duration_S * sps)
    θ = (2 * π * each_sample_number * freq_Hz / sps)
    # print(θ)
    waveform = 10000 * sg.square(θ)
    waveform_quiet = waveform * volume
    # print(waveform_quiet)
    waveform_integers = np.int16(waveform_quiet * 32767)  # integer because making its digital signal
    file_name = f'squ_wave{freq_Hz}Hz.wav'
    write(file_name, sps, waveform_integers)  # Write the .wav file
    return file_name


def f(x, equ):
    return eval(equ)


def create_wave_custom(freq_Hz=10000.0, duration_S=5.0, equ_custom='sin(x)', volume=0.3):
    sps = 44100  # Samples per second(sps)
    π = np.pi
    each_sample_number = np.arange(duration_S * sps)
    x = (2 * π * each_sample_number * freq_Hz / sps)
    # print(x)
    waveform = f(x=x, equ=equ_custom)
    waveform_quiet = waveform * volume
    # print(waveform_quiet)
    waveform_integers = np.int16(waveform_quiet * 32767)  # integer because making its digital signal
    file_name = f'custom_equ_wave({equ_custom})-{freq_Hz}Hz.wav'
    file_name = file_name.replace('*', 'X')
    file_name = file_name.replace('/', '-')
    write(file_name, sps, waveform_integers)  # Write the .wav file
    return file_name


list = [
    'create sin wave',
    'create cos wave',
    'create square wave',
    'create custom wave in terms of x'
]
for ch, i in enumerate(list):
    print(ch, i)

while (True):
    choice = int(input('select the choice! again! '))
    freq = int(input('enter the freq of the sound wave(Hz) '))
    vol = float(input("enter the volume from (0.0 to 1.0) "))
    duration=float(input("enter the duration of the sound wave in (seconds)"))
    if choice == (0):
        file_name = create_wave_sin(freq_Hz=freq, volume=vol)
        break
    elif choice == (1):
        file_name = create_wave_cos(freq_Hz=freq, volume=vol)
        break
    elif choice == (2):
        file_name = create_wave_squ(freq_Hz=freq, volume=vol)
        break
    elif choice == (3):
        equ = input('enter the custom eqution in terms of x')
        file_name = create_wave_custom(freq_Hz=freq, volume=vol, equ_custom=equ)
        break
    else:
        print('wrong in put, select 0 t0 3 ')
        continue

yn = input('do you want to see the graph? (y/n) ')
if yn in ('y', 'Y'):
    # read audio samples
    input_data = read(filename=file_name)
    audio = input_data[1]
    # print(audio[0:1024])
    # plot the first 1024 samples
    plt.plot(audio[0:1024])
    # label the axes
    plt.ylabel("Amplitude")
    plt.xlabel("samples")
    # set the title
    plt.title(file_name)
    # display the plot
    plt.show()
else:
    print('ok fine!')

yn = input('do you want to play the sound (y/n) ')
if yn in ('Y', 'y'):
    playsound(file_name)
else:
    print('ok fine!')

yn = input('do you want to see the files (y/n) ')
if yn in ('Y', 'y'):
    path = f'explorer /select,{os.path.dirname(os.path.abspath(__file__))}\{file_name}'
    print(path)
    Popen(path)

else:
    print('ok fine!')
