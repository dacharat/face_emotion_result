# ML² Face Emoji Recognition

This project is a project developed from [ML² Face Emoji Swap](https://gitlab.com/imla/demos/ml2_face_emotion_swap). The project use to prediction the face which detected working with [result-web](https://gitlab.com/imla/demos/ml2_face_emotion_result/tree/jack-2019/result-web) project.

## Note
There are 2 functions to running in different devices.

```
# this code was in `modified_ml2.py` line 283-286
# change `cam_dev` to 0 when you want to run with your PC camera
self.cam.open_cam_usb(0)
# this use for run camera on Jetson board
self.cam.open_cam_onboard()

```
- If ypu want to run on the PC, you must comment the line `self.cam.open_cam_onboard()`
- If you want to run on the Jetson board, you must comment the line `self.cam.open_cam_usb(0)`

## Python Environment For Jetson TX2
> this part was translate from [Python-Umgebung Jetson TX2](https://gitlab.com/imla/demos/ml2_face_emotion_swap#python-umgebung-jetson-tx2)

The version of Jetson TX2 Python supported by [NVIDIA] [install-tf-jetsontx2] is version 3.5.2. In addition, a pre-compiled Tensorflow version 1.09 is also available. Thus, this is the default configuration for the Python environment. This environment is subsequently created for the Jetson TX2.
 
* OpenCV On Jetson TX2  
Since the OpenCV library included in JetPack is only designed for the Python2 version, a newer version according to the [Instructions] [opencv3_on_tx2] will be installed in this step.
 
* Installation all required packages 
```
 sudo apt-get update && sudo apt-get install liblapack-dev \
libblas-dev \
libfreetype6-dev \ 
libhdf5 \
virtualenv \
python3-dev \
python3-pip \
```


* Create the Python environment  
```
# Create Python 3.5.2 environment under USER_HOME/dev/py3_keras
virtualenv --python=python3 ~/dev/py3_keras 
#
# Activate environment
source ~/dev/py3_keras/bin/activate
#
pip --version 
# pip 18.1 from /home/nvidia/dev/py3_keras/lib/python3.5/site-packages/pip (python 3.5)
#
python --version
# Python 3.5.2
#
# Installation of all required Python packages
pip install -r requirements.txt 
#
# Installation of Tensorflow for Jetson TX2 
pip install --extra-index-url https://developer.download.nvidia.com/compute/redist/jp33 tensorflow-gpu
#
# Add OpenCV to the environment
ln -s /usr/local/lib/python3.5/dist-packages/cv2.cpython-35m-aarch64-linux-gnu.so \
     ~/dev/py3_keras/lib/python3.5/site-packages/cv2.cpython-35m-aarch64-linux-gnu.so  
```


## Python environment for Windows

1. Installing [Python 3.5.2](https://www.python.org/) directly or using [Anaconda Distribution](https://www.anaconda.com/distribution/#download-section) to create a Python 3.5.2 environment.
2. Use ``pip`` to install the required packages:

````
pip install -r requirements.txt 
````

## Python environment for Mac

Installing by use shell script file:
`./setup_mac.sh`
 
## modified_ml2.py

The main script for the demonstrator represents the file `modified_ml2.py`. The script can be executed with the prepared Python environment in the following command: `python modified_ml2.py`.

* __Pretrained Network__  
The ``modified_ml2.py`` script needs an artificial neural network to run. In the ZIP archive [EmotionClassifier-EP35-ACC0.68.zip](https://bwsyncandshare.kit.edu/dl/fiLA4wRYWBKVzphjPKPoRVPq/EmotionClassifier.zip) there is a pre-trained model `EmotionClassifier.hdf5` and additional training information `model_history.png` and `model_summery.txt` ready. Finally, to be able to start the demonstrator, the model is placed in the `./data/` folder and the script is started as described.

Additional parameters and description are listed in the following help output.
```  
usage: modified_ml2.py [-h] [--cam-dev CAM_DEV] [-i IMAGE]
                              [-id IMAGE_DIRECTORY] [--api-url API_URL]

This script, mainly aimed as a demonstrator at exhibitions, is executed on the
Nvidia Jetson TX2 system. With this script a task in the field of machine
leaning is performed. Firstly, an object detector is used to detect faces in a
camera stream. Secondly, all detected faces are classified by an earlier
trained artificial neural network in few emotion classes like angry and
happy.In a last step, the face will now be replaced by a equivalent emoji,
e.g. if the face is classified as angry the angry emoji will replace the face.
The resulted image with all replaced faces is than displayed in a window

optional arguments:
  -h, --help            show this help message and exit
  --cam-dev CAM_DEV     The device number of the camera which should be used.
                        By the Default=1 an usb Webcam on Jetson TX2 will be
                        used.
  -i IMAGE, --image IMAGE
                        runs the detection and classification task on an
                        image, mainly as debugging purpose.
  -id IMAGE_DIRECTORY, --image-directory IMAGE_DIRECTORY
                        runs the detection and classification task on a whole
                        directory with multiple images in an endless loop.
  --api-url API_URL     The API use to POST and GET data from database. The
                         default is http://localhost:3000/ but if use with the
                         server that not in the localhost should set this to be
                         the IP addressof the machine which use to run the
                         server. Ex. --api-url http://158.16.77.12:3000/

```
 
After starting the application, a window with the corresponding output is opened. The top-left screen displays the image that the camera can capture. The top-right displays the image after processing through Deep Learning. The bottom displays the probability of each emotion.

The program can be controlled by the following keys:
* `ESC` Ends the program execution.
* `h` Help text on or hide.
* `f` offset application in fullscreen.
* `1-4` __experimental__ Selection of the haar-cascade file for facial recognition.

## References

[emotion-recognition-neural-networks][emotion-recognition-neural-networks]  
[fer2013][fer2013]  
[opencv3_on_tx2][opencv3_on_tx2]  
[tutorial_py_face_detection][tutorial_py_face_detection]  
[install-tf-jetsontx2][install-tf-jetsontx2]
[ML² Face Emoji Swap](https://gitlab.com/imla/demos/ml2_face_emotion_swap#python-umgebung-jetson-tx2)  
 
[ML2]: https://ml2.hs-offenburg.de/aktuelles/
[emotion-recognition-neural-networks]: https://github.com/isseu/emotion-recognition-neural-networks
[fer2013]: https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge
[opencv3_on_tx2]: https://jkjung-avt.github.io/opencv3-on-tx2/
[tutorial_py_face_detection]: https://docs.opencv.org/3.4.3/d7/d8b/tutorial_py_face_detection.html
[install-tf-jetsontx2]: https://docs.nvidia.com/deeplearning/dgx/install-tf-jetsontx2/index.html