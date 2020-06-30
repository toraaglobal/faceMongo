# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 15:26:34 2020

@author: teeja
"""


from faceMongo import faceMongo
from tqdm import tqdm

if __name__=="__main__":
    fm = faceMongo.FaceMongo('facebook','localhost',27017)
    
    pages = ['donaldtrump','joebiden','senschumer'] # 
    for page in tqdm(pages):
        fm.fb_page_to_db(page)
    
    # load documents from DB
    docs = fm.docs_from_db('joebiden' )
    print(len(docs))
