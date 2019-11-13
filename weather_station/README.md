## App which shows how to connect LED to Raspberry Pi and make it blink using Python.

### 1. What do we need for this app:
- Raspberry Pi 3 setup with monitor and USB Mouse & Keyboard
- Checkout this guide if you need help: 
    `https://nostarch.com/pythonplayground`
- Temperature sensor
- Humidity sensor
- Jumper wires for easy hookup

Also, we need to access raspberry-pi by wifi.

### 2. Instalation
```bash
sudo apt-get update

sudo apt-get install python-rpi.gpio python3-rpi.gpio python-setuptools python-dev 

sudo apt-get install python-bottle python3-bottle

wget http://www.flotcharts.org/downloads/flot-0.8.3.zip
unzip flot-0.8.3.zip
mv flot my_project_dir

git clone https://github.com/adafruit/Adafruit_Python_DHT.git

cd Adafruit_Python_DHT
sudo python setup.py install
```

### 3. Running
```python run_weatcher_station.py```
or as a root
```sudo python run_weatcher_station.py```

![start image](station.jpg)

### If we decide to stop we should write in terminal:
`$ sudo shutdown -h now`
