brew install pyenv
pyenv install 3.5.2
mkdir ~/dev/py3_keras; cd ~/dev/py3_keras
pyenv local 3.5.2
mkvirtualenv --python=`pyenv which python` ~/dev/py3_keras
source ~/dev/py3_keras/bin/activate
pip install -r requirements.txt
pip install --extra-index-url https://developer.download.nvidia.com/compute/redist/jp33 tensorflow-gpu
ln -s /usr/local/lib/python3.5/dist-packages/cv2.cpython-35m-aarch64-linux-gnu.so \\n     
~/dev/py3_keras/lib/python3.5/site-packages/cv2.cpython-35m-aarch64-linux-gnu.so
