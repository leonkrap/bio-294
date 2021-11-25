#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:59:46 2021

@author: leoniekrapf
"""



def get_all_genenames():
    import os

    genefiles=[]


    for files in os.walk("static/treefiles"):
        print(files)
        for file in files[2]:
        
            name=str(file)
            if name.endswith("png"):
                genefiles.append(name)
                
    genenames=[]
    for filename in genefiles:
        gene= filename.split(".")[1]
        genenames.append(gene)
        
        
    return genenames


print(get_all_genenames())



