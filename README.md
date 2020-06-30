***
## faceMongo
***
Scrape facebook public pages and save int in a mongo database as a collection of documents.
Retrieved collections from mongo database.

***
### Installattion 
***

Run the following command from the terminal

```
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps faceMongo-toraaglobal
```
***
### Usage
***

To retrive  the facebook pad of `donaldtrump` and save it in `facebook` database in mongo db .
assuming you have a mongo db installed locally.

run the code below.

```
import FaceMongo
fm = FaceMongo('facebook','localhost',27017)
fm.fb_page_to_db('donaldtrump',nums= 200)

```

To retrive `donaldtrump` collection from the facebook database,

The code below will return the collection of documents in a list

```
docs = fm.docs_from_db('donaldtrump' )

```
***
### Licence
***
MIT License

