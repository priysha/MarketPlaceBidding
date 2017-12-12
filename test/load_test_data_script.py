#########################################################
##
## AUTHOR:  Priysha Pradhan
## PURPOSE: Script to load data from csv files
## to db for testing
##
##########################################################

from BidDB import BidDB
from BuyerDB import BuyerDB
from SellerDB import SellerDB
from ProjectDB import ProjectDB
from DataBaseDriver import DataBaseDriver
from constants import *
import pandas as pd

Project = ProjectDB()
Buyer = BuyerDB()
Seller = SellerDB()
Bid = BidDB()
db = DataBaseDriver()

def load_all():
    db.runTruncateTableQuery(PROJECT_TABLE)
    db.runTruncateTableQuery(BUYER_TABLE)
    db.runTruncateTableQuery(SELLER_TABLE)
    db.runTruncateTableQuery(BID_TABLE)

    df = pd.read_csv(PROJECT_DATA)
    Project.load(df)

    df = pd.read_csv(BUYER_DATA)
    Buyer.load(df)

    df = pd.read_csv(SELLER_DATA)
    Seller.load(df)

    df = pd.read_csv(BID_DATA)
    Bid.load(df)

if __name__=="__main__":
    load_all()