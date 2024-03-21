# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:16:00 2024

@author: fatih
"""

import os
klasor = '20088929\Valid'#Dosya yolunu yazıyoruz
dosyalar = os.listdir(klasor)

for  dosya in dosyalar:
    os.rename(os.path.join(klasor, dosya), os.path.join(klasor, ''.join(["20088929_", dosya])))#Dosya yolu ve değiştirmek istediğimiz adı yazıyoruz