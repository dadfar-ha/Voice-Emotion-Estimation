# Voice-Emotion-Estimation
A mew Method for estimating the emotion of speech (Persian_Dataset). 



### Requires - Section
Before Testing, please install these libraries from huggingface:


```bash
!pip install torchaudio
!pip install librosa
!pip install git+https://github.com/huggingface/datasets.git
!pip install git+https://github.com/huggingface/transformers.git
```
```bash
!git clone https://github.com/m3hrdadfi/soxan.git
!git clone https://github.com/dadfar-ha/Voice-Emotion-Estimation.git
```
### Dataset - Section
you can download the SheMo dataset by following link (female utterances):
```bash
wget -O female.zip "https://www.dropbox.com/s/4t6mep8mo4yf81f/female.zip?dl=0"
```

you can download the SheMo dataset by following link (male utterances):
```bash
wget -O male.zip "https://www.dropbox.com/s/xfi3hi927yxixa9/male.zip?dl=0"
```

you can download the SheMo dataset by following link (labels):
```bash
wget https://github.com/pariajm/sharif-emotional-speech-dataset/raw/master/shemo.json
```

### Test - Section
for testing, please run ''' test.py '''


## Models

| Name                                                                                                                      | Model                                                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [Pre-Trained Model for persian dataset besed on HUBERT]          | [Model](https://huggingface.co/m3hrdadfi/wav2vec2-xlsr-persian-speech-emotion-recognition)         |   |
