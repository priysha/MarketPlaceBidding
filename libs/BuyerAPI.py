##########################################################
##
## File: BuyerAPI.py
## Author: Priysha Pradhan
## Description: This is a database access class for buyer
## table. This class handles all the SQL queries executed
## for maintaining the buyer table
##
##########################################################

# Module Import #
import DataBaseDriver
from constants import *

##
## Class: BuyerAPI
## Description: This class is the database driver for Buyer
##
class BuyerAPI(DataBaseDriver.DataBaseDriver):
    BUYER_TABLENAME = BUYER_TABLE
    def __init__(self):
        DataBaseDriver.DataBaseDriver.__init__(self)

    ##
    ## Name: createBuyer
    ## Description: This function creates a new buyer
    ##
    ## Parameters: buyer dict with required values
    ##
    ## Returns: returns True if buyer is created
    ##
    def createBuyer(self, buyer):

        query = "INSERT INTO " + BuyerAPI.BUYER_TABLENAME + " (buyer_id, first_name, last_name, location, skills) VALUES (%s, %s, %s, %s, %s) "
        params = (buyer['buyer_id'], buyer['first_name'],buyer['last_name'] , buyer['location'], buyer['skills'])
        return self.runInsertQuery(query, params)

    ##
    ## Name: getBuyerInfo
    ## Description: This function returns buyer's
    ## info from the db
    ##
    ## Parameters: buyer_id
    ##
    ## Returns: Dataframe containing buyer's info
    ##
    def getBuyerInfo(self, buyer_id):

        query = "SELECT buyer_id, first_name, last_name, location, skills, creation_time FROM "\
                + BuyerAPI.BUYER_TABLENAME + " WHERE buyer_id = '" + buyer_id + "'"
        return self.runSelectDfQuery(query)

    ##
    ## Name: getAllBuyers
    ## Description: This function returns info
    ## of all the buyers in the system
    ##
    ## Parameters: None
    ##
    ## Returns: dataframe with all the buyers' info
    ##
    def getAllBuyers(self):
        query = "SELECT buyer_id, first_name, last_name, location, skills, creation_time FROM " \
                + BuyerAPI.BUYER_TABLENAME
        return self.runSelectDfQuery(query)

    ##
    ## Name: setBuyerFirstName
    ## Description: This function updates first name
    ## of the buyer in the db
    ##
    ## Parameters: buyer_id, first_name
    ##
    ## Returns: True if updated else false
    ##
    def setBuyerFirstName(self, buyer_id, first_name):

        query = "UPDATE " + BuyerAPI.BUYER_TABLENAME + "SET first_name = ' " + first_name + "' WHERE buyer_id = '" + buyer_id + "'"
        return self.runUpdateQuery(query)

    ##
    ## Name: setBuyerLastName
    ## Description: This function updates last_name
    ## of the buyer in the db
    ##
    ## Parameters: buyer_id, last_name
    ##
    ## Returns: True if updated else false
    ##
    def setBuyerLastName(self, buyer_id, last_name):

        query = "UPDATE " + BuyerAPI.BUYER_TABLENAME + "SET last_name = ' " + last_name + "' WHERE buyer_id = '" + buyer_id + "'"
        return self.runUpdateQuery(query)

    ##
    ## Name: setBuyerLocation
    ## Description: This function updates location
    ## of the buyer in the db
    ##
    ## Parameters: buyer_id, location
    ##
    ## Returns: True if updated else false
    ##
    def setBuyerLocation(self, buyer_id, location):

        query = "UPDATE " + BuyerAPI.BUYER_TABLENAME + "SET location = ' " + location + "' WHERE buyer_id = '" + buyer_id + "'"
        return self.runUpdateQuery(query)

    ##
    ## Name: setBuyerSkills
    ## Description: This function updates skills
    ## of the buyer in the db
    ##
    ## Parameters: buyer_id, skills
    ##
    ## Returns: True if updated else false
    ##
    def setBuyerSkills(self, buyer_id, skills):

        query = "UPDATE " + BuyerAPI.BUYER_TABLENAME + "SET skills = ' " + skills + "' WHERE buyer_id = '" + buyer_id + "'"
        return self.runUpdateQuery(query)

    ##
    ## Name: load
    ## Description: This function loads the buyer info
    ## directly from the dataframe given
    ##
    ## Parameters: dataframe df
    ##
    ## Returns: True if all rows inserted else false
    ##
    def load(self, df):
        check = True
        for index, row in df.iterrows():
            buyer_dict = {'buyer_id': row['buyer_id'],'first_name' : row['first_name'], 'last_name' : row['last_name'],
                    'location': row['location'], 'skills' : row['skills']}
            if not self.createBuyer(buyer_dict):
                check = False
        return check
