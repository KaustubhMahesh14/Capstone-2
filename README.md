<<<<<<< HEAD
# Emotion_detection_with_CNN

![emotion_detection](https://github.com/datamagic2020/Emotion_detection_with_CNN/blob/main/emoition_detection.png)

### Packages need to be installed
- pip install numpy
- pip install opencv-python
- pip install keras
- pip3 install --upgrade tensorflow
- pip install pillow

### download FER2013 dataset
- from below link and put in data folder under your project directory
- https://www.kaggle.com/msambare/fer2013

### Train Emotion detector
- with all face expression images in the FER2013 Dataset
- command --> python TranEmotionDetector.py

It will take several hours depends on your processor. (On i7 processor with 16 GB RAM it took me around 4 hours)
after Training , you will find the trained model structure and weights are stored in your project directory.
emotion_model.json
emotion_model.h5

copy these two files create model folder in your project directory and paste it.

### run your emotion detection test file
python TestEmotionDetector.py
=======
# EmoViz(Facial Emotion Detector)
# 🙂😀😮😤😒😔😨

https://user-images.githubusercontent.com/96725900/164004710-2fbaaa02-fe4f-4645-b08d-d1426139ced5.mp4

![7Emotions](https://user-images.githubusercontent.com/96725900/163942354-e7befdcc-1772-4877-b271-bab3d5c9eabf.png)

Jump over to the Installation section using the table of contents if you don't want to know much about the project. 

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Description">Description</a></li>
    <li>
      <a href="#About the Models">About the Models</a>
      <ul>
        <li><a href="#Face Detector">Face Detector</a></li>
      </ul>
      <ul>
        <li><a href="#Facial Emotion Classifier">Facial Emotion Classifier</a></li>
      </ul>
      <ul>
        <li><a href="#How it works">How it works</a></li>
      </ul>
    </li>
    <li>
      <a href="#Installation">Installation</a>
      <ul>
        <li><a href="#Requirements">Requirements</a></li>
        <li><a href="#Setup">Setup</a></li>
      </ul>
    </li>
    <li><a href="#Inference">Inference</a></li>
    <li><a href="#License">License</a></li>
    <li><a href="#Credits">Credits</a></li>
  </ol>
</details>

# 📝Description

Facial Emotion Detection is one of the useful and toughest Machine Learning tasks because of the intra-class variation in expressions among the people. The best usecase of FED is in human-machine interaction. EmoViz is a facial emotion detection system built using TensorFlow, which takes image input and display one of the seven emotions(Neutral, Happy, Surprise, Angry, Disgust, Sad, Fear).

<p align="right">(<a href="#top">back to top</a>)</p>

# 🤖About the Models

The system employs two models: one for face detection and another for facial emotion classification.

## Face Detector

* Face detection model is built using TensorFlow 2.0 object detection API, where I used SSD MOBILENET V2 as the pretrained model.
* To built a face detection model first get the data(There will be many resources out there or else take some random pictures from internet and the number is dependent, in my case it's 50 for training and 10 for validation) to train the model.
* And then follow [this](https://tensorflow-object-detection-api-tutorial.readthedocs.io/) documentation to train a face detector on the gathered data. If u want a video tutorial check [this](https://youtu.be/XoMiveY_1Z4).
* I'd used colab to train the model.

## Facial Emotion Classifier

* Facial Emotion Classification model is built using TensorFlow 2.0, where I trained a deep convolutional neural network on RAF-DB. It's a generalised modelwith a training accuracy of 90% and test accuracy of 83%.
*  I'll create a separate repo on how to create a model like this, so if you're here then check my repos.
*  RAF-DB is a private database and to download it you need to send an email as shown on their [website](http://www.whdeng.cn/raf/model1.html#:~:text=Real%2Dworld%20Affective%20Faces%20Database%20(RAF%2DDB)%20is,labeled%20by%20about%2040%20annotators.).
*  First I'd started training the model on my local machine(GPU - GTX 1660ti), but when I started incresing the complexity of the model it took a lot of time to train and also started crying like a baby. 
*  I can't experiment fastly, So I shifted to kaggle to train the model. I've choosen kaggle over colab because of it's more gpu time and resources and it made experimentation faster.

## How it works

The input image is first given to the face detector to detect the face and then this is given to the facial emotion classifier to classify the emotion.

<p align="right">(<a href="#top">back to top</a>)</p>

# 🖥Installation

## 🛠Requirements

* Python 3.7+ 
* Other requirement are mentioned in requirements.txt and can be installed as shown below.

## ⚙️Setup
1. First create a virtual environment using venv. You can use powershell, go to the path you want and type the below commands. 
```
python -m venv EViz
```
2. Activate it.
```
EViz\Scripts\activate
```
Then you can use pip list to see what are all the packages installed and there will be pip and settup tools(in my case).

3. Upgrade pip to the latest version.
```
python -m pip install --upgrade pip
```
Clone the EmoViz repo and change the directory to EmoViz and run the below command.

4. Install the required packages.
```
python -m pip install -r requirements.txt
```
That's it you're set to go.

<p align="right">(<a href="#top">back to top</a>)</p>

# 🎯Inference
```
python app.py
```
<p align="right">(<a href="#top">back to top</a>)</p>

# ⚖License
Distributed under the MIT License. See LICENSE.txt for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

# Credits
* http://www.whdeng.cn/raf/li_RAFDB_2017_CVPR.pdf

<p align="right">(<a href="#top">back to top</a>)</p>
>>>>>>> 0722c816 (second commit)
