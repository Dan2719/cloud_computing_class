# Simple program
def my_function():
  print("Hello from a function")

my_function()

# A function
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Arguments and functions
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Another Argument and function example
def my_progrm(ofstudy):
    print(ofstudy + "  InDs")
my_progrm(" ICT Department")
my_progrm(" Doing Data Science")
my_progrm(" In Second Year")

# Working with libriaries!
import math
import numpy as np
import pandas as pd
import nltk
import matplotlib.pyplot as plt
import seaborn as sns;sns.set()
from IPython.display import display, HTML
from patsy import dmatrices
import warnings
warnings.filterwarnings ("ignore")
%pylab inline