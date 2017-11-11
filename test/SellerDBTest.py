##########################################################
##
## File: SellerDBTest.py
## Author: Priysha Pradhan
## Description: This file contains tests for SellerDB class
## These test cases check if the SellerDB class is interacting
## with the db correctly and returning data in correct format
##
##########################################################

# Module Import #
import unittest
from SellerDB import SellerDB
import json

##
## Class: SellerDBTest
## Description: This class is the unittest driver for SellerDB class
##
class SellerDBTest(unittest.TestCase):
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
        self.Seller = SellerDB()

    ##
    ## Name: testCreateSeller
    ## Description: This method tests createSeller()
    ## method for SellerDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testCreateSeller(self):

        seller_dict = {'seller_id': 'foo1', 'first_name': 'foo', 'last_name': 'bar',
                       'location': '', 'job_title': '', 'company': ''}

        #should pass
        self.assertEquals(True, self.Seller.createSeller(seller_dict))

        self.assertEquals(True, 'Priysha' in self.Seller.getAllSellers().first_name.values)


    ##
    ## Name: testGetSellerInfo
    ## Description: This method tests getSellerInfo()
    ## method for SellerDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetSellerInfo(self):

        seller_id = 'priysha'
        self.assertEquals('Pradhan', self.Seller.getSellerInfo(seller_id).last_name[0])

    ##
    ## Name: testGetNonExistingSellerInfo
    ## Description: This method tests getSellerInfo()
    ## method for SellerDB class when seller doesnt exist
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetNonExistingSellerInfo(self):

        seller_id = 'xyz'
        self.assertEquals(True, self.Seller.getSellerInfo(seller_id).empty)

    ##
    ## Name: testGetAllSellers
    ## Description: This method tests getAllSellers()
    ## method for SellerDB class
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

    ##
    ## Name: testRemoveSeller
    ## Description: This method tests removeSeller()
    ## method for SellerDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testRemoveSeller(self):
        seller_id = 'bwetherbyb'
        self.assertEquals(True, self.Seller.removeSeller(seller_id))
        self.assertEquals(True, self.Seller.getSellerInfo(seller_id).empty)

    ##
    ## Name: testjsonEncoderForOneSeller
    ## Description: This method tests jsonEncoder()
    ## method for SellerDB class to return correct json
    ## for one seller in the data
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testjsonEncoderForOneSeller(self):
        seller_data = self.Seller.getSellerInfo('dwiltonm')
        output_json = seller_data.to_json(orient='records')
        self.assertEquals(output_json, self.Seller.jsonEncoder(seller_data))

    ##
    ## Name: testjsonEncoderForAllSellers
    ## Description: This method tests jsonEncoder()
    ## method for SellerDB class to return correct json
    ## for all sellers in the data
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testjsonEncoderForAllSellers(self):
        seller_data = self.Seller.getAllSellers()
        output_json = seller_data.to_json(orient='records')
        self.assertEquals(output_json, self.Seller.jsonEncoder(seller_data))


    ##
    ## Name: testjsonDecoder
    ## Description: This method tests jsonDecoder()
    ## method for BuyerDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testjsonDecoder(self):
        test_data = self.Seller.getSellerInfo('slankester6').to_dict(orient='records')

        self.assertEquals(sorted(test_data[0]), sorted(self.Seller.jsonDecoder(test_data[0])))


