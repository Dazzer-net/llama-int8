# LLaMA int8 + flask server

This is a fork of LLaMA int8 by tloen

Currently testing, do not trust code or docs.

## How to use

On server:

1. Make folder structure
2. Install bitsandbytes and other dependencies to run facebook LLaMA with int8
3. Download weights
4. Use this repo to start flask server

On client machine:

1. Test that server is running


#### Make folder structure

cd ~
mkdir llama llama/weights

#### To install bitsandbytes from source

```
sudo apt install -y build-essential
cd ~
git clone https://github.com/tloen/llama-int8
cd ~/bitsandbytes
make cuda11x CUDA_VERSION=116
python setup.py install
pip install torch fairscale fire sentencepiece tqdm
export LD_LIBRARY_PATH=/opt/conda/lib
cd ~
```

If your system has lib not lib64, use this repo instead of tloen's repo:
```
git clone https://github.com/Aashrith-V/bitsandbytes.git
```

#### To download weights

From seedbox:

(replace XXX.XXX.XXX.XXX with IP of seedbox)
(to use a bigger model replace 7B with 13B, 30B or 65B)

```
sftp -P 2222 user@XXX.XXX.XXX.XXX
yes
1c82a6bbbc
cd Downloads/LLaMA
lcd ~/llama/weights
get *.*
cd 7B
lmkdir 7B
lcd 7B
get *.*
exit
```

#### To run flask app with LLaMA int8

(This will expose model on all open ports to HTTP traffic, your IP can be DDoSed)

```
cd ~/llama/llama-int8
python3 flask-app-direct.py
```

#### On client machine: To test flask server

In python interpreter or new python file:

```
import requests
r1 = requests.post(url = "http://127.0.0.1:5000/flask-inference/", json = {"apikey":"22c1d19df3fafe2576f409c8", "prompt": "What is your name?"})
print(r1.json())
```

#### To run flask app without loading or running LLaMA

```
cd ~/llama/llama-int8
python3 flask-app-test.py
```

#### To test LLaMA interactively, without running flask app

```
cd ~/llama/llama-int8
python3 manual-int8.py
```
