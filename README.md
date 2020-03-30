# tkkuih
A Demo App for combining TKInter with Tensorflow - an app for recognizing Malay Traditional Kuih.
In this demo, you can select a photo containing traditional Malay kuih (or cakes? desserts? not sure of direct translation), and the model will attempt to identify it.


# Who is this app for
This is a demo app to show students that it is possible and _extremely easy_ to create a GUI Desktop demonstration of Tensorflow-based application using TKinter. 


# Requirements
- Tensorflow 1.13+ or 1.14
- Python (obviously)
- TKinter
- Keras
- pillow / PIL
- numpy

or in Anaconda, you can run :
`pip install tensorflow==1.14 tk keras pillow numpy scikit-learn`

## TKinter Video Tutorial
You can watch TKinter video tutorial here [Youtube Link - TKinter video tutorial](https://youtu.be/PeMikTXzs1s)


# Configurable options
Since I wrote this in  a very short time (1 hour) on day-12 of isolation during COVID-19 outbreak (Movement Control Order), I didn't include much configurable options other than what provided from the default Tensorflow example distribution.

You can customized your model name and model label under `addOpenFile()` and `detectGate()`

# Model Support
The demo support any (*.pb) model trained by Tensorflow 1.10 - 1.15, with `Inception` and `MobileNet`. Please see the `Configuration options` on how to change input size parameter to suit your model.

# Youtube Video
[![Watch the video](https://img.youtube.com/vi/PeMikTXzs1s/maxresdefault.jpg)](https://youtu.be/PeMikTXzs1s)




