##########################################################
##
## File: SellerDashboardAPI.py
## Author: Priysha Pradhan
## Description: This class works for Seller's
## dashboard, all the requirements for seller can be retrived
## using these methods.
##
##########################################################

# Module Import #
from ProjectAPI import ProjectAPI
from BidAPI import BidAPI
from SellerAPI import SellerAPI
from constants import *
import logging.config
logging.config.fileConfig(LOGGING_CONF)

##
## Class: SellerDashboardAPI
## Description: This class is the driver for Seller dashboard
##
class SellerDashboardAPI:
    def __init__(self, sellerId):
        self.logger = logging.getLogger('Market_Place')
        self.logger.info("IN - SellerDashboardAPI constructor")
        self.Project = ProjectAPI()
        self.Bid = BidAPI()
        self.Seller = SellerAPI()
        self.sellerId = sellerId

    ##
    ## Name: getSellerInfo
    ## Description: This function is called to retrieve a seller's
    ## info from the db
    ##
    ## Parameters: None
    ##
    ## Returns: returns dataframe with seller's info
    ##
    def getSellerInfo(self):
        self.logger.info("IN - SellerDashboardAPI getSellerInfo method")
        buyer_info = self.Seller.getSellerInfo(self.sellerId)
        return buyer_info

    ##
    ## Name: getAllProjectsUnderSeller
    ## Description: This function is called to retrieve all
    ## the projects under the seller
    ##
    ## Parameters: None
    ##
    ## Returns: returns dataframe with seller's projects
    ##
    def getAllProjectsUnderSeller(self):
        self.logger.info("IN - SellerDashboardAPI getAllProjectsUnderSeller method")
        seller_projects = self.Project.getAllProjectsForSellers(self.sellerId)
        return seller_projects

    ##
    ## Name: addANewProject
    ## Description: This function is called to let
    ## seller add a new project with details
    ##
    ## Parameters: project_name, location, bid_end_time, description
    ##
    ## Returns: returns True if project created
    ##
    def addANewProject(self, project_name, location, bid_end_time, description):
        self.logger.info("IN - SellerDashboardAPI addANewProject method")
        project = {'project_name' : project_name, 'location' : location,
                   'seller_id' : self.sellerId, 'bid_end_time' : bid_end_time, 'description' : description}

        return self.Project.createProject(project)






