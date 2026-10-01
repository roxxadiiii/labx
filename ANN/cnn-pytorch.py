steps = """
import necessary libraries
check for gpu drive
transfromations on training and test data we will define those
load the data
divide the data into batches
construct cnn architecture using a class
write a functions for training, evaluating
then call the model
"""

ascii= """
╔═╗╔╗╔╔╗╔            
║  ║║║║║║            
╚═╝╝╚╝╝╚╝            
╔═╗╦ ╦╔╦╗╔═╗╦═╗╔═╗╦ ╦
╠═╝╚╦╝ ║ ║ ║╠╦╝║  ╠═╣
╩   ╩  ╩ ╚═╝╩╚═╚═╝╩ ╩

"""


notes = """
everything is treated as tensor(multi dim. arrays)
pytorch is a framework/lib developed by meta
pytorch -> consist 2 libs named torch torchvision

torch -> tensor
    helps to achieve the best performance with cuda or in another word helps in hardware acceleration
    create
    mathematical op.
    gradients calc.
    classes
    consist a nn model
        which used only for neural networks things
    torch vision
        manipulation of datasets and more

data augmentation 
    flippig
    crop
    shearing

"""


# code begin here

#importing py torch

import torch , torchvision
import torch.nn as nn
import torch.transforms as transforms
from torch.utils.data import DataLoader


# checking devices
torch.device()
