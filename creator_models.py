"""
ner模型

@coder payphone
@date 2020-05-15
"""

import tensorflow as tf

from tensorflow.keras import Model
from tensorflow.keras.layers import Bidirectional, LSTM, Dropout, Dense

class BModel(Model):
	"""bi_lstm 

	"""

	def __init__(self):
		super(CBCModel).__init__()
		self.lstm = Bidirectional(LSTM(300),
							  backward_layer=LSTM(300, go_backwards=True),
                         	  merge_mode='concat')
		self.dropout = Dropout(0.5)
		self.dense = Dense(18, activation='softmax')

	def call(self, x):
		x = self.lstm(x)
		x = self.dropout(x)
		return x = self.dense(x)


