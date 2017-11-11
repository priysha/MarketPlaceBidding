##########################################################
##
## File: marketPlaceAppTest.py
## Author: Priysha Pradhan
## Description: This file tests the put and delete for the
## marketPlaceApp rest api
##
##########################################################

# Module Import #
import unittest
from BidDB import BidDB
from ProjectDB import ProjectDB
from BuyerDB import BuyerDB
from SellerDB import SellerDB
import json
import requests
from requests.auth import HTTPBasicAuth
from constants import *

BuyerDB = BuyerDB()
SellerDB = SellerDB()
BidDB = BidDB()
ProjectDB = ProjectDB()
api_headers = {'Content-Type': 'application/json'}
auth = HTTPBasicAuth(USERNAME, PASSWORD)
##
## Class: marketPlaceAppTest
## Description: This class is the unittest driver for marketPlaceApp
##
class marketPlaceAppTest(unittest.TestCase):

    ##
    ## Name: testProjectPut
    ## Description: This method tests PUT for
    ## Project
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testProjectPut(self):

        project_url = "http://localhost:5000/projects"
        project_data = {'data': {"project_id": "45", "project_name": "ABCD", "location": "New York",
                                 "bid_end_time":"2017-11-19","seller_id":"foo","buyer_id":None, "description":"ABC","creation_time":""}}
        requests.put(project_url, headers=api_headers, data=json.dumps(project_data), auth=auth)
        self.assertEquals("ABCD",ProjectDB.getProjectInfo(45).project_name[0])

    ##
    ## Name: testProjectDelete
    ## Description: This method tests DELETE for
    ## Project
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testProjectDelete(self):
        delete_project_id = '35'
        project_url = "http://localhost:5000/projects/" + delete_project_id

        requests.delete(project_url, headers=api_headers, auth=auth)
        self.assertEquals(True,ProjectDB.getProjectInfo(delete_project_id).empty)

    ##
    ## Name: testSellerPut
    ## Description: This method tests PUT for
    ## Seller
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testSellerPut(self):
        seller_url = "http://localhost:5000/sellers"
        seller_data = {'data': {"seller_id": "test_seller", "first_name": "Test", "last_name": "Seller",
                                "location": "foo", "job_title": "", "company": "",
                                "creation_time": ""}}
        requests.put(seller_url, headers=api_headers, data=json.dumps(seller_data), auth=auth)
        self.assertEquals("Test", SellerDB.getSellerInfo('test_seller').first_name[0])

    ##
    ## Name: testSellerDelete
    ## Description: This method tests DELETE for
    ## Seller
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testSellerDelete(self):
        delete_seller_id = 'foobar'
        seller_url = "http://localhost:5000/sellers/" + delete_seller_id

        requests.delete(seller_url, headers=api_headers, auth=auth)
        self.assertEquals(True,SellerDB.getSellerInfo(delete_seller_id).empty)

    ##
    ## Name: testProjectPut
    ## Description: This method tests PUT for
    ## Buyer
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testBuyerPut(self):
        buyer_url = "http://localhost:5000/buyers"
        buyer_data = {'data':{"buyer_id":"test_buyer","first_name":"Test","last_name":"Buyer",
                      "location":"NC","skills":"","creation_time":""}}

        requests.put(buyer_url, headers=api_headers, data=json.dumps(buyer_data), auth=auth)
        self.assertEquals("Test", BuyerDB.getBuyerInfo('test_buyer').first_name[0])

    ##
    ## Name: testBuyerDelete
    ## Description: This method tests DELETE for
    ## Buyer
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testBuyerDelete(self):
        delete_buyer_id = 'foobar'
        buyer_url = "http://localhost:5000/buyers/" + delete_buyer_id

        requests.delete(buyer_url, headers=api_headers, auth=auth)
        self.assertEquals(True,BuyerDB.getBuyerInfo(delete_buyer_id).empty)

    ##
    ## Name: testBidPut
    ## Description: This method tests PUT for
    ## Bid
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testBidPut(self):
        bid_url = "http://localhost:5000/bids"
        bid_data = {'data': {"bid_id": "100", "project_id": "10", "buyer_id": "foo", "bid_amount": 2400.33,
                             "bid_type": "hourly", "bid_hours": 80, "creation_time": ""
                             }}

        requests.put(bid_url, headers=api_headers, data=json.dumps(bid_data), auth=auth)
        self.assertEquals("foo", BidDB.getBidInfo(100).buyer_id[0])

    ##
    ## Name: testBidDelete
    ## Description: This method tests DELETE for
    ## Bid
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testBidDelete(self):
        delete_bid_id = '88'
        bid_url = "http://localhost:5000/bids/" + delete_bid_id

        requests.delete(bid_url, headers=api_headers, auth=auth)
        self.assertEquals(True,BidDB.getBidInfo(delete_bid_id).empty)



