from BidAPI import BidAPI
from BuyerAPI import BuyerAPI
from SellerAPI import SellerAPI
from ProjectAPI import ProjectAPI
from DataBaseDriver import DataBaseDriver
from constants import *
import pandas as pd

#TODO Automate this script to run before all unittests

Project = ProjectAPI()
Buyer = BuyerAPI()
Seller = SellerAPI()
Bid = BidAPI()
db = DataBaseDriver()

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