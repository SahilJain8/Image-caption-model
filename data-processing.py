import numpy as np
from tqdm.notebook import tqdm
from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input
from tensorflow.keras.utils import load_img,img_to_array
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
