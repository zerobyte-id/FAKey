# FAKey
FAKey (Find Any Keys) tools for find credentials key.

![FAKey](https://raw.githubusercontent.com/zerobyte-id/FAKey/master/FAKey-SS.png)

## Installation 
```
git clone https://github.com/zerobyte-id/FAKey.git
cd FAKey
python3 -m pip install -r requirements.txt
```
## Using python (version 3)
```
python3 FAKey.py -t http://192.168.100.128
```
## Using docker
```
docker build -t FAKey .
docker run -it --rm FAKey -t http://192.168.100.128
```

### Custom
You can add something regex or path config : 
* Regexs: **data/keyregexs.json**
* Path config: **data/path_config.txt**

### Tested on :
[![](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)

### Thanks
* Regex: ([gitleaks](https://github.com/zricethezav/gitleaks/blob/master/config/gitleaks.toml))
* Path config: ([bruteforce-lists](https://github.com/random-robbie/bruteforce-lists))
