##########################################################
##
## File: SellerTest.py
## Author: Priysha Pradhan
## Description: This file contains tests for Seller class
## These test cases check if the Seller class is interacting
## with the db correctly and returning data in correct format
##
##########################################################

import unittest
from Seller import Seller
import pandas as pd

##
## Class: SellerTest
## Description: This class is the unittest driver for Seller class
##
class SellerTest(unittest.TestCase):
    ##
    ## Name: setUp
    ## Description: Fixture that runs prior to the execution of any test. We are
    ## setting the database properties to point to the dev database.
    ##
    ## Parameters:
    ## None
    ##
    ## Returns: None
    ##
    def setUp(self):
        self.Seller = Seller()

        df = pd.read_csv("./test/sellers.csv")
        self.Seller.load(df)

    ##
    ## Name: tearDown
    ## Description: Fixture that runs after the execution of all tests. We are
    ## setting the database properties to point to the prod database.
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
    ## method for Seller class
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
        #should fail on trying to create duplicate seller
        self.assertEquals(False, self.Seller.createSeller(seller_dict))

        self.assertEquals(True, 'Priysha' in self.Seller.getAllSellers().first_name.values)

    ##
    ## Name: testCreateSeller
    ## Description: This method tests getSellerInfo()
    ## method for Seller class
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
    ## method for Seller class
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