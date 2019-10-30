import numpy as np
import pandas as pd
from scipy.signal import stft
import os
# import matplotlib.pyplot as plt
# from numpy.fft import fft, fftshift


def get_next_file_name_2test(file=None):
    prefix = '~/Downloads/Bearing_dataset/IMS/2nd_test/2004.02.'
    if file == None:
        suffix = '12.10.32.39'
    else:
        prev_date = file[-11:]
        next_date = prev_date.split('.')
        if int(next_date[2]) >= 50:
            next_date[2] = '0' + str(int(next_date[2]) - 50)
            if int(next_date[1]) >= 23:
                next_date[1] = '0' + str(int(next_date[1]) - 23)
                next_date[0] = str(int(next_date[0]) + 1)
            else:
                if int(next_date[1]) < 9:
                    next_date[1] = '0' + str(int(next_date[1]) + 1)
                else:
                    next_date[1] = str(int(next_date[1]) + 1)
        else:
            next_date[2] = str(int(next_date[2]) + 10)
        suffix = ''
        for t in next_date:
            suffix = suffix + t + '.'
        suffix = suffix[:-1]
    return prefix + suffix


# f = open(os.path.expanduser(get_next_file_name_2test()), "r")
# i = 0
# for line in f:
#     row = line.split('\t')
#     row[3] = row[3].replace("\n","")
#     row = [float(i) for i in row]
#     if i == 0:
#         mat = np.asarray(row)
#         # print(mat)
#     else:
#         aux = np.asarray(row)
#         mat = np.concatenate((mat, aux))
#     i += 1
#     # if i >= 8:
#     #     break
# # print(mat.reshape((4,8), order='F'))
# mat = mat.reshape((4,20480), order='F')

#################
freq_samp = 20e3
width = 410 # 20ms
frame_shift = 205 # 10ms
# f, t, Zxx = stft(mat[0], fs=freq_samp, window='hamming', nperseg=width, noverlap=frame_shift)
#
# print(t.shape)
# print(f.shape)
# print(Zxx.shape)
# print(f[f <= 5000].shape) # 103 frequencies <= 5kHz
#
# # Signal with noise
# plt.figure()
# plt.pcolormesh(t, f, np.abs(Zxx), vmin=0)
# plt.title('STFT Magnitude')
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
#
# # 'Denoised' signal
# plt.figure()
# plt.pcolormesh(t, f[:103], np.abs(Zxx[:103]), vmin=0)
# plt.title('STFT Magnitude')
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.show()
#########################

path = get_next_file_name_2test()
for i in range(984):
    f = open(os.path.expanduser(path), "r")
    i = 0
    for line in f:
        row = line.split('\t')
        row[3] = row[3].replace("\n", "")
        row = [float(i) for i in row]
        if i == 0:
            mat = np.asarray(row)
            # print(mat)
        else:
            aux = np.asarray(row)
            mat = np.concatenate((mat, aux))
        i += 1
        # if i >= 8:
        #     break
    # print(mat.reshape((4,8), order='F'))
    mat = mat.reshape((4, 20480), order='F')
    path = get_next_file_name_2test(path)

    f, t, Zxx = stft(mat[0], fs=freq_samp, window='hamming', nperseg=width, noverlap=frame_shift)

    pd.DataFrame(Zxx).to_csv("foo.csv", header=None, index=None)
    # z = np.asarray(Zxx)
    # np.savetxt('foo.csv', z, delimiter=',')

# window = np.hamming(51)
#
# plt.plot(window)
# plt.title("Hamming window")
# plt.ylabel("Amplitude")
# plt.xlabel("Sample")
# plt.show()
#
# plt.figure()
# A = fft(window, 2048) / 25.5
# mag = np.abs(fftshift(A))
# freq = np.linspace(-0.5, 0.5, len(A))
# response = 20 * np.log10(mag)
# response = np.clip(response, -100, 100)
# plt.plot(freq, response)
# plt.title("Frequency response of Hamming window")
# plt.ylabel("Magnitude [dB]")
# plt.xlabel("Normalized frequency [cycles per sample]")
# plt.axis('tight')
# plt.show()
