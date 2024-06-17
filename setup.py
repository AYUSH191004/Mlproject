from setuptools  import setup
from setuptools import find_packages
 
from typing import list 
HYPEN_E_DOT='-e.'

def getreqiurement(file_path=str):
    reqiurements=[]
    with open (file_path) as f:
      reqiurements=f.readlines()   
      reqiurements=[req.replace('/n',"") for req in reqiurements]  
      
      if (HYPEN_E_DOT in reqiurements):
         reqiurements.remove(HYPEN_E_DOT)

      return reqiurements
    
setup(name ='src',version= 0.0.1,author='AYUSH',install_packages= getreqiurement('requirement.txt')author_email='ayushrajputparihar@gmail.com',
packages= find_packages();)