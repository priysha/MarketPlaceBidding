##############################################################
##
## File: BuyerDBTest.py
## Author: Priysha Pradhan
## Description: This file contains tests for BuyerDB class
## These test cases check if the BuyerDB class is interacting
## with the db correctly and returning data in correct format
##
###############################################################

# Module Import #
import unittest
from BuyerDB import BuyerDB
import json

##
## Class: BuyerDBTest
## Description: This class is the unittest driver for BuyerDB class
##
class BuyerDBTest(unittest.TestCase):
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
        self.Buyer = BuyerDB()


    ##
    ## Name: testCreateBuyer
    ## Description: This method tests createBuyer()
    ## method for BuyerDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetAllBuyers(self):

        self.assertEquals(False, self.Buyer.getAllBuyers().empty)

    ##
    ## Name: testCreateBuyer
    ## Description: This method tests createBuyer()
    ## method for BuyerDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testCreateBuyer(self):

        buyer_dict = {'buyer_id': 'foo', 'first_name': 'foo', 'last_name': 'bar',
                       'location': '', 'skills': ''}

        #should pass
        self.assertEquals(True, self.Buyer.createBuyer(buyer_dict))

        self.assertEquals(True, 'Priysha' in self.Buyer.getAllBuyers().first_name.values)


    ##
    ## Name: testGetBuyerInfo
    ## Description: This method tests getBuyerInfo()
    ## method for BuyerDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetBuyerInfo(self):

        buyer_id = 'priysha'
        self.assertEquals('Pradhan', self.Buyer.getBuyerInfo(buyer_id).last_name[0])

    ##
    ## Name: testGetNonExistingBuyerInfo
    ## Description: This method tests getBuyerInfo()
    ## method for BuyerDB class for non-existing buyer
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testGetNonExistingBuyerInfo(self):
        buyer_id = 'xyz'
        self.assertEquals(True, self.Buyer.getBuyerInfo(buyer_id).empty)

    ##
    ## Name: testRemoveBuyer
    ## Description: This method tests removeBuyer()
    ## method for BuyerDB class
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testRemoveBuyer(self):
        buyer_id = 'cshilstonek'
        self.assertEquals(True, self.Buyer.removeBuyer(buyer_id))
        self.assertEquals(True, self.Buyer.getBuyerInfo(buyer_id).empty)

    ##
    ## Name: testjsonEncoderForOneBuyer
    ## Description: This method tests jsonEncoder()
    ## method for ProjectDB class to return correct json
    ## for one project in the data
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testjsonEncoderForOneBuyer(self):
        buyer_data = self.Buyer.getBuyerInfo('cstiegarf')
        output_json = buyer_data.to_json(orient='records')
        self.assertEquals(output_json, self.Buyer.jsonEncoder(buyer_data))

    ##
    ## Name: testjsonEncoderForAllBuyers
    ## Description: This method tests jsonEncoder()
    ## method for BuyerDB class to return correct json
    ## for all buyers in the data
    ##
    ## Parameters: None
    ##
    ## Returns: None
    ##
    def testjsonEncoderForAllBuyers(self):
        buyer_data = self.Buyer.getAllBuyers()
        output_json = buyer_data.to_json(orient='records')
        self.assertEquals(output_json, self.Buyer.jsonEncoder(buyer_data))


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
        test_data = self.Buyer.getBuyerInfo('odargann').to_dict(orient='records')

        self.assertEquals(sorted(test_data[0]),sorted(self.Buyer.jsonDecoder(test_data[0])))

