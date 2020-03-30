# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:42:50 2020

Copyright (c) 2020, Mohammad Hafiz bin Ismail.

@author: Mohammad Hafiz bin Ismail (mypapit@gmail.com)
@Purpose: Desktop GUI demonstration for tensorflow


Trained using Tensorflow 1.14 with MobileNet 192

##See function "addOpenFile()" and  "detectGate" for documentation


p/s: I wrote this under one hour during Movement Control Order in Alor Setar, Malaysia
At the time of this writing (30 March 2020), I haven't venture past my residential 
area since 19 March 2020.


"""

import tkinter as tk
from tkinter import filedialog, Text,messagebox
import os
from PIL import ImageTk,Image
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array



import numpy as np
import tensorflow as tf
import time




imgfile=""

root = tk.Tk()
root.title("Demo Tensorflow TKInter Classification by Mohammad Hafiz bin Ismail (mypapit@gmail.com)")
canvas = tk.Canvas(root, height=600,width=800)

bottomFrame = tk.Frame(root)
bottomFrame.pack(side=tk.BOTTOM)

canvas.pack()

    
def load_graph(model_file):
  graph = tf.Graph()
  graph_def = tf.GraphDef()

  with open(model_file, "rb") as f:
    graph_def.ParseFromString(f.read())
  with graph.as_default():
    tf.import_graph_def(graph_def)

  return graph

def addOpenFile():
    """
    ##Tested on Inception and MobileNet##    
    Please edit model_file to suit your model pb file and label_file to specify your label text file
    
    
    Please see function "detectGate" for further customization.


    """
    model_file = "mobile_graph.pb"
    label_file = "mobile_labels.txt"
    graph = load_graph(model_file)
    
    
    
    filename = filedialog.askopenfilename(initialdir="/",title="Select File",filetypes=[("JPEG Files",".jpeg .jpg")])
    print("Selected file: %s" % filename)
    image = ImageTk.PhotoImage(Image.open(filename))
    canvas.create_image(50,50,anchor=tk.NW,image=image)
   
    imgfile = filename
    
    #recognize(filename)
    
    #line ni paling penting untuk pass parameter model file dengan label file
    detectGate(graph,label_file,filename)
    
    
def read_tensor_from_image_file(file_name,
                                input_height=299,
                                input_width=299,
                                input_mean=0,
                                input_std=255):
  input_name = "file_reader"
  output_name = "normalized"
  file_reader = tf.read_file(file_name, input_name)
  if file_name.endswith(".png"):
    image_reader = tf.image.decode_png(
        file_reader, channels=3, name="png_reader")
  elif file_name.endswith(".gif"):
    image_reader = tf.squeeze(
        tf.image.decode_gif(file_reader, name="gif_reader"))
  elif file_name.endswith(".bmp"):
    image_reader = tf.image.decode_bmp(file_reader, name="bmp_reader")
  else:
    image_reader = tf.image.decode_jpeg(
        file_reader, channels=3, name="jpeg_reader")
  float_caster = tf.cast(image_reader, tf.float32)
  dims_expander = tf.expand_dims(float_caster, 0)
  resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
  normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
  sess = tf.Session()
  result = sess.run(normalized)

  return result


def load_labels(label_file):
  label = []
  proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
  for l in proto_as_ascii_lines:
    label.append(l.rstrip())
  return label


def detectGate(graph,label_file,file_name):
  """ 
  #Modify parameter ini untuk Inception
  input_height = 299
  input_width = 299
  

  #Modify parameter ini untuk MobileNet 224
  input_height = 299
  input_width = 299
  

  #Modify parameter ini untuk MobileNet compact 192
  input_height = 192
  input_width = 192


  """
  input_height = 192
  input_width = 192
  input_mean = 0
  input_std = 255
  input_layer = "Placeholder"
  output_layer = "final_result"
  
  
 

 

  
  t = read_tensor_from_image_file(
      file_name,
      input_height=input_height,
      input_width=input_width,
      input_mean=input_mean,
      input_std=input_std)
  
  input_name = "import/" + input_layer
  output_name = "import/" + output_layer
  input_operation = graph.get_operation_by_name(input_name)
  output_operation = graph.get_operation_by_name(output_name)

  with tf.Session(graph=graph) as sess:
    results = sess.run(output_operation.outputs[0], {
        input_operation.outputs[0]: t
    })
  results = np.squeeze(results)

  top_k = results.argsort()[-5:][::-1]
  labels = load_labels(label_file)
  #for i in top_k:
  #  print(labels[i], results[i])
  
  gresults = float("{:.4f}".format(results[top_k[0]]))
      
  labelandimage = "{0} \r\n {1} - {2}".format(file_name,labels[top_k[0]],gresults)
    
  label = tk.Label(canvas,text=labelandimage,bg="gray")
  label.pack()

  print (labels[top_k[0]], results[top_k[0]])
  

def classifyFunction():
    if (len(imgfile)<2):
        print ("%s file "%imgfile)
        messagebox.showinfo("Alert","Please select valid file")
        pass
    pass





if __name__ == "__main__":
  
  
  
  openFile = tk.Button(bottomFrame,text="Classify",padx=10,pady=5,bg="#999999",command=addOpenFile)
  openFile.pack()


  frame = tk.Frame(root,bg="white")
  root.mainloop()



