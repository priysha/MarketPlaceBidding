##########################################################
##
## File: BidAPITest.py
## Author: Priysha Pradhan
## Description: This file contains tests for BidAPI class
## These test cases check if the BidAPI class is interacting
## with the db correctly and returning data in correct format
##
##########################################################

# Module Import #
import unittest
from BidAPI import BidAPI
import pandas as pd

##
## Class: BidAPITest
## Description: This class is the unittest driver for BidAPI class
##
##TODO: Add more test cases
class BidAPITest(unittest.TestCase):
    ##
    ## Name: setUp
    ## Description: Fixture that runs prior to the execution of any test.
    ##
    ## Parameters:
    ## None
    ##
    ## Returns: None
    ##
    def setUp(self):
        self.Bid = BidAPI()

    ##
    ## Name: testGetAllBids
    ## Description: This method tests getAllBids()
    ## method for BidAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetAllBids(self):
        self.assertEquals(False, self.Bid.getAllBids().empty)
        self.assertEquals(True, 'priysha' in self.Bid.getAllBids().buyer_id.values)

    ##
    ## Name: testCreateBid
    ## Description: This method tests createBid()
    ## method for BidAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testCreateBid(self):
        bid_dict_hourly = {'project_id' : '3' , 'buyer_id' : 'smarr9', 'bid_amount' : '20', 'bid_type' : 'hourly', 'bid_hours' : 1000}
        self.assertEquals(True, self.Bid.createBid(bid_dict_hourly))
        self.assertEquals(True, 'smarr9' in self.Bid.getAllBids().buyer_id.values)

        bid_dict_fixed = {'project_id': '10', 'buyer_id': 'rstonehamj', 'bid_amount': '2000', 'bid_type': 'fixed',
                           'bid_hours': 0}
        self.assertEquals(True, self.Bid.createBid(bid_dict_fixed))
        self.assertEquals(True, 'rstonehamj' in self.Bid.getAllBids().buyer_id.values)

    ##
    ## Name: testGetBidInfo
    ## Description: This method tests getBidInfo()
    ## method for BidAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetBidInfo(self):
        bid_id = int(self.Bid.getAllBids().bid_id[0])
        self.assertEquals(False, self.Bid.getBidInfo(bid_id).empty)


    ##
    ## Name: testSetAmountForBid
    ## Description: This method tests setBidAmount()
    ## method for BidAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testSetAmountForBid(self):
        bid_id = int(self.Bid.getAllBids().bid_id[0])
        bid_amount = 500
        self.assertEquals(True, self.Bid.setBidAmount(bid_amount,bid_id))
        self.assertEquals(bid_amount,self.Bid.getBidInfo(bid_id).bid_amount[0])

    ##
    ## Name: testGetBidsForBuyer
    ## Description: This method tests getBidsForBuyer()
    ## method for BidAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetBidsForBuyer(self):
        buyer_id = 'priysha'
        self.assertEquals(False, self.Bid.getBidsForBuyer(buyer_id).empty)
        self.assertEquals(True, 8 in self.Bid.getBidsForBuyer(buyer_id).project_id.values)

    ##
    ## Name: testGetBidsForProject
    ## Description: This method tests getBidsForProject()
    ## method for BidAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetBidsForProject(self):
        project_id = 2
        self.assertEquals(False, self.Bid.getBidsForProject(project_id).empty)




