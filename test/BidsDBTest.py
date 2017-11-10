##########################################################
##
## File: BidDBTest.py
## Author: Priysha Pradhan
## Description: This file contains tests for BidDB class
## These test cases check if the BidDB class is interacting
## with the db correctly and returning data in correct format
##
##########################################################

# Module Import #
import unittest
from BidDB import BidDB
import json
import pandas as pd

##
## Class: BidDBTest
## Description: This class is the unittest driver for BidDB class
##
class BidDBTest(unittest.TestCase):
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
        self.Bid = BidDB()

    ##
    ## Name: testGetAllBids
    ## Description: This method tests getAllBids()
    ## method for BidDB class
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
    ## method for BidDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testCreateBid(self):
        bid_dict_hourly = {'bid_id': '88','project_id' : '3' , 'buyer_id' : 'smarr9', 'bid_amount' : '20', 'bid_type' : 'hourly', 'bid_hours' : 1000}
        self.assertEquals(True, self.Bid.createBid(bid_dict_hourly))
        self.assertEquals(True, 'smarr9' in self.Bid.getAllBids().buyer_id.values)

        bid_dict_fixed = {'bid_id': '89','project_id': '10', 'buyer_id': 'rstonehamj', 'bid_amount': '2000', 'bid_type': 'fixed',
                           'bid_hours': 0}
        self.assertEquals(True, self.Bid.createBid(bid_dict_fixed))
        self.assertEquals(True, 'rstonehamj' in self.Bid.getAllBids().buyer_id.values)

    ##
    ## Name: testGetBidInfo
    ## Description: This method tests getBidInfo()
    ## method for BidDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetBidInfo(self):
        bid_id = int(self.Bid.getAllBids().bid_id[0])
        self.assertEquals(False, self.Bid.getBidInfo(bid_id).empty)


    ##
    ## Name: testGetBidAmount
    ## Description: This method tests getBidAmount()
    ## method for BidDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetBidAmount(self):
        bid_id = 10
        self.assertEquals(33273.6, self.Bid.getBidAmount(bid_id))


    ##
    ## Name: testGetBidsForBuyer
    ## Description: This method tests getBidsForBuyer()
    ## method for BidDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetBidsForBuyer(self):
        buyer_id = 'priysha'

        self.assertEquals(False, self.Bid.getBidsForBuyer(buyer_id).empty)
        self.assertEquals(True, '8' in self.Bid.getBidsForBuyer(buyer_id).project_id.values)

    ##
    ## Name: testRemoveBid
    ## Description: This method tests removeBid()
    ## method for BidDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testRemoveBid(self):
        bid_id = 3
        self.assertEquals(True, self.Bid.removeBid(bid_id))
        self.assertEquals(True, self.Bid.getBidInfo(bid_id).empty)

    ##
    ## Name: testjsonEncoderForOneBid
    ## Description: This method tests jsonEncoder()
    ## method for BidDB class to return correct json
    ## for one bid in the data
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testjsonEncoderForOneBid(self):
        bid_id = 12
        bid_data = self.Bid.getBidInfo(bid_id)
        output_json = bid_data.to_json(orient='records')
        self.assertEquals(output_json, self.Bid.jsonEncoder(bid_data))

    ##
    ## Name: testjsonEncoderForAllBids
    ## Description: This method tests jsonEncoder()
    ## method for BidDB class to return correct json
    ## for all bids in the data
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testjsonEncoderForAllBids(self):
        bid_data = self.Bid.getAllBids()
        output_json = bid_data.to_json(orient='records')
        self.assertEquals(output_json, self.Bid.jsonEncoder(bid_data))


    ##
    ## Name: testjsonDecoder
    ## Description: This method tests jsonDecoder()
    ## method for BidDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testjsonDecoder(self):
        test_data = self.Bid.jsonEncoder(self.Bid.getBidInfo(10))

        actual_result = self.Bid.jsonDecoder(test_data)
        expected_result = json.loads(test_data)[0]
        self.assertEquals(sorted(actual_result),sorted(expected_result))




