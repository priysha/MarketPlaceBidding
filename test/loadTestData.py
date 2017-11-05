from BidAPI import BidAPI
from BuyerAPI import BuyerAPI
from SellerAPI import SellerAPI
from ProjectAPI import ProjectAPI
from DataBaseDriver import DataBaseDriver
import pandas as pd

#TODO Automate this script to run before all unittests

Project = ProjectAPI()
Buyer = BuyerAPI()
Seller = SellerAPI()
Bid = BidAPI()
db = DataBaseDriver()

db.runTruncateTableQuery('project')
db.runTruncateTableQuery('buyer')
db.runTruncateTableQuery('seller')
db.runTruncateTableQuery('bid')

df = pd.read_csv("./projects.csv")
Project.load(df)

df = pd.read_csv("./buyers.csv")
Buyer.load(df)

df = pd.read_csv("./sellers.csv")
Seller.load(df)

df = pd.read_csv("./bids.csv")
Bid.load(df)