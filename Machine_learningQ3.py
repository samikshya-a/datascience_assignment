#!/usr/bin/env python
# coding: utf-8

# In[15]:


import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
import torchvision.transforms as transforms
from albumentations import Compose, Normalize
from albumentations.pytorch import ToTensor


# In[13]:


pip install albumentations


# In[4]:


#1
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
import torchvision.transforms as transforms
from albumentations import Compose, Normalize
from torchvision.transforms.functional import to_tensor



# In[5]:


#2
class VegetableClassifier(nn.Module):
    def __init__(self, num_classes):
        super(VegetableClassifier, self).__init__()
        # Define your model architecture here
        
    def forward(self, x):
        # Define the forward pass of your model
        return x


# In[8]:


#3
from albumentations import Compose, Normalize
from albumentations.pytorch.transforms import ToTensorV2

# ...

transform_train = Compose([
    # Add your desired image transformations here
    Normalize(),  # Normalize the image pixel values
    ToTensorV2()  # Convert the image to tensor
])

transform_valid = Compose([
    Normalize(),
    ToTensorV2()
])


# In[ ]:




