# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 15:02:23 2020

@author: teeja
"""


import pymongo
import json
from bson.json_util import dumps
from pymongo.errors import BulkWriteError
from facebook_scraper import get_posts
import pandas as pd
from tqdm import tqdm
from facebook_scraper import get_posts


class FaceMongo:
    

    def __init__(self,dbname,host, port):
        self.host = host
        self.input_dbname = dbname
        self.port = port 
        self.client = pymongo.MongoClient(self.host, self.port)
        self.dbname = self.input_dbname.lower().replace('#', '').replace(' ','')
        
        
    def fb_page_to_db(self, page, nums):
        self.collection = page.lower().replace('#', '').replace(' ', '')
        self.db = self.client[self.dbname]
        self.collection = self.db[self.collection]
        
        data =  self._get_data_from_fb(page, nums)
        try:
            self.collection.insert_many(data)
            print("Saved", len(data), "documents to DB collection", self.db, self.collection)
        except BulkWriteError as e:
            print(e,details)
            
        
    def docs_from_db(self, collection):
        docs = self.collection.find()
        #  convert the cursor to a list
        docs_bson = list(docs)
        docs_json_str = [dumps(doc) for doc in docs_bson]
        docs_json = [json.loads(doc) for doc in docs_json_str]
        return docs_json
         
    
    def list_db(self):
        pass 
    
    def list_collections(self):
        
        pass 
    def  _get_data_from_fb(self, fb_page, nums):
        
        data = []
        for post in get_posts(fb_page, pages=nums):
            #post['_id'] = get_hash_id(str( post['post_id']) ) # used the hashed key of the post id as _id 
            data.append(post)
        return data 
    

    
