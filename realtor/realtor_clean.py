import pandas as pd 
import numpy as np 
import pymongo
from realtortransformer import realtor_df

def main():
    '''
    Iterates through dataframe webpage object and runs transformer to clean data from html objects
    '''

    #creates connection to mongodb
    client = pymongo.MongoClient()
    db = client.realtor
    collection = db.main_pages

    #updates clean values to new table in database
    clean_collection = db.realtor_data

    def transform_data(row):
        data = row.to_dict()
        clean_collection.insert_one(data)   

    df = realtor_df(collection)

    #drops duplicate listings based on mls id
    clean_df = df.drop_duplicates('listingId')
    clean_df.apply(transform_data, axis=1)

if __name__ == '__main__':
    main()