import os
import matplotlib.pyplot as plt
import fileutils as fs
from threading import Event
import numpy as np
import sys
import wave
from scipy.fftpack import fft

def main(bit_depth='Int16'):
	files = os.listdir('processed')
	s = 'audio_'
	for file in files:
		base_name, ext = os.path.splitext(file)
		actual_file_path = os.path.join('processed', file)
		if ext == '.wav':
			f = wave.open(actual_file_path, 'rb')
			params = f.getparams()
			rate = params.framerate
			if params.nchannels == 1:
				raw = f.readframes(-1)
				data = np.fromstring(raw, bit_depth)
				x = np.linspace(0, rate, len(data))
				y = np.abs(fft(data))
				plt.title('FFT plot: %s' % actual_file_path)
				half = int(len(data)/2)
				plt.semilogx(x[:half], y[:half])
				image_path = 'processed/fig_fft_%s.png' % base_name[len(s):]
				plt.savefig(image_path)
				print('Saved:', image_path)
				plt.clf()

if __name__ == '__main__':
	if len(sys.argv[1:]):
		main(sys.argv[1])
	else:
		main()	