##########################################################
##
## File: BiddingProcessAPITest.py
## Author: Priysha Pradhan
## Description: This file contains tests for BiddingProcessAPI
##  class. These test cases check if the Buyer class is
## interacting with the db correctly and returning data
## in correct format.
##
##########################################################

import unittest
from BiddingProcessAPI import BiddingProcessAPI
from BuyerAPI import BuyerAPI
from SellerAPI import SellerAPI
from
import pandas as pd

##
## Class: BuyerTest
## Description: This class is the unittest driver for BiddingProcessAPI class
##
class BiddingProcessAPITest(unittest.TestCase):
    ##
    ## Name: setUp
    ## Description: Fixture that runs prior to the execution of any test.
    ## In the setUp, we are adding some fake testing data in the db
    ##
    ## Parameters:
    ## None
    ##
    ## Returns: None
    ##
    def setUp(self):
        self.BidProcess = BiddingProcessAPI()

        df = pd.read_csv("./test/buyers.csv")
        self.Pro.load(df)

    ##
    ## Name: tearDown
    ## Description: Fixture that runs after the execution of all tests.
    ## This will remove the db entries made in the setUp
    ##
    ## Parameters:
    ## None
    ##
    ## Returns: None
    ##
    def tearDown(self):
        self.Buyer.runTruncateTableQuery('buyer')
        #delete all the data