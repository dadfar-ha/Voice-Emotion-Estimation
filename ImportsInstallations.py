!pip install git+https://github.com/huggingface/datasets.git
!pip install git+https://github.com/huggingface/transformers.git
!pip install jiwer
!pip install torchaudio
!pip install librosa

%env LC_ALL=C.UTF-8
%env LANG=C.UTF-8
%env TRANSFORMERS_CACHE=/content/cache
%env HF_DATASETS_CACHE=/content/cache
%env CUDA_LAUNCH_BLOCKING=1



!mkdir -p /content/data
!gdown https://drive.google.com/uc?id=1_IAWexEWpH-ly_JaA5EGfZDp-_3flkN1
!unzip -q aesdd.zip -d /content/data/
!mv "/content/data/Acted Emotional Speech Dynamic Database/" /content/data/aesdd/



import numpy as np
import pandas as pd

from pathlib import Path
from tqdm import tqdm

import torchaudio
from sklearn.model_selection import train_test_split

import os
import sys