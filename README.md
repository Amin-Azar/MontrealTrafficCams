## Montréal Traffic Cameras - CloudVision Project

Hourly images of traffic cameras in Montréal. The images are being analyzed for their context, objects in it and the text messages. The extracted data can be used to get stats of vehicles commuted via captured routes throughout the day.
The next step is to capture the raw and extracted data and have an anomaly detection mechanism applied on them to detect accidents, fires, festivals and events.

```
# Update and upgrade Ubuntu packages
sudo apt update
sudo apt upgrade

# Get python 3.7+
sudo apt install python3-pip

pip3 install -r requirement.txt

mkdir models;
cd models; wget https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5

python3 detection.py
```
