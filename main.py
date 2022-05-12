from numpy.distutils.system_info import p
from projetfonction import *

notes = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']
frequences = [264, 297, 330, 352, 396, 440, 495]
figures = ['c', 'n', 'b', 'r']
d0 = 0.125

choix = int(input(
    "1: Partition \n2: Nouvelle partition \n3: Transformation d'une partition \n4: Composition d’une nouvelle partition  \n5: Enrichir la base de donnée \nChoix: "))
if choix == 1:
    f = "partitions"
    print("Voici les partitions qu'on vous propose: ")
    cpt = 1
    file = open("partitions.txt", 'r')
    lignes = file.readlines()
    for i in lignes:
        if cpt % 2 != 0 and cpt < 25:
            print(i, end='')
        cpt = cpt + 1
    num = int(input("indique le numero de la partition que vous vouhaitez: "))
    ligne, freq_seq, duration_seq = read_sheet(read_line_file(f, num), calc_frequency(notes, frequences),
                                               calc_duration(figures, d0))
    play_sheet(freq_seq, duration_seq)
    print(freq_seq)
    print(duration_seq)
"""elif choix == 2:

elif choix == 3:
    choix = input("1: Transposition \n2: Inversion \nChoix: ")
    if choix == 1:

    else:

elif choix == 4:

elif choix == 5:

else:
    break"""
"""n = {'Do':1,'Ré':2,'Mi':3,'Fa':4,'Sol':5,'La':6,'Si':7}
f = {1: 264, 2: 297, 3: 330, 4: 352, 5: 396, 6: 440, 7: 495}
d = {'r': 1, 'b': 0.5, 'n': 0.25, 'c': 0.125}"""

from time import sleep
import numpy as np
import simpleaudio as sa

def calc_frequency(notes, frequence):
    dictionnairefreq = {}
    cpt = 0
    for i in notes:
        dictionnairefreq[i] = frequence[cpt]
        cpt += 1
    return dictionnairefreq


def calc_duration(figures, d0):
    dictionnairedura = {}
    for i in figures:
        dictionnairedura[i] = d0
        d0 = d0*2
    return dictionnairedura


def read_line_file(f, num):
    if f == "partitions":
        if num == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12:
            num = num *2
        cpt = 1
        file = open("partitions.txt", 'r')
        lignes = file.readlines()
        for i in lignes:
            if cpt == num:
                return i
            cpt += 1


def read_sheet(ligne, freq, dura):
    freq_seq = []
    duration_seq = []
    ligne = ligne.split(" ")
    for i in ligne:
        for cpt in freq:
            if 'Z' in i:
                freq_seq.append(-1)
                break
            if cpt in i:
                freq_seq.append(freq[cpt])
        for cpts in dura:
            if 'Z' in i:
                duration_seq.append(-dura[cpts])
                break
            if cpts in i:
                duration_seq.append(dura[cpts])
    ligne = ' '.join(ligne)
    return ligne, freq_seq, duration_seq


def play_sheet(freq, dura):
    for i in range(len(freq)):
        if freq[i] > 0 and dura[i] > 0:
            sound(freq[i],dura[i])
        else:
            sleep(-dura[i])


def sound(freq, duration):
    sample_rate = 44100
    t = np.linspace(0, duration, int(duration*sample_rate), False)
    tone = np.sin(freq*t*6*np.pi)
    tone *= 838607 / np.max(np.abs(tone))
    tone = tone.astype(np.int32)
    i = 0
    byte_array = []
    for b in tone.tobytes():
        if i % 4 != 3:
            byte_array . append(b)
        i += 1
    audio = bytearray(byte_array)
    play_obj = sa.play_buffer(audio, 1, 3, sample_rate)
    play_obj.wait_done()


