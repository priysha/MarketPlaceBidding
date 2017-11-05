##########################################################
##
## File: SellerAPITest.py
## Author: Priysha Pradhan
## Description: This file contains tests for SellerAPI class
## These test cases check if the Seller class is interacting
## with the db correctly and returning data in correct format
##
##########################################################

import unittest
from SellerAPI import SellerAPI
import pandas as pd

##
## Class: SellerAPITest
## Description: This class is the unittest driver for SellerAPI class
##
class SellerAPITest(unittest.TestCase):
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
        self.Seller = SellerAPI()

        df = pd.read_csv("./test/sellers.csv")
        self.Seller.load(df)

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
        self.Seller.runTruncateTableQuery('seller')
        #delete all the data


    ##
    ## Name: testCreateSeller
    ## Description: This method tests createSeller()
    ## method for SellerAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testCreateSeller(self):

        seller_dict = {'seller_id': 'foo', 'first_name': 'foo', 'last_name': 'bar',
                       'location': '', 'job_title': '', 'company': ''}

        #should pass
        self.assertEquals(True, self.Seller.createSeller(seller_dict))

        self.assertEquals(True, 'Priysha' in self.Seller.getAllSellers().first_name.values)

    ##
    ## Name: testCreateSeller
    ## Description: This method tests getSellerInfo()
    ## method for SellerAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetSellerInfo(self):

        seller_id = 'priysha'
        self.assertEquals('Pradhan', self.Seller.getSellerInfo(seller_id).last_name[0])

    ##
    ## Name: testGetAllSellers
    ## Description: This method tests getAllSellers()
    ## method for SellerAPI class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetAllSellers(self):
        seller_id = 'priysha'
        result = self.Seller.getAllSellers()
        self.assertEquals(False, result.empty)
        self.assertEquals(True, seller_id in result.seller_id.values)