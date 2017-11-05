##########################################################
##
## File: ProjectAPI.py
## Author: Priysha Pradhan
## Description: This is a database access class for project
## table and its dependent project_detail table. This class
## handles all the SQL queries executed for maintaining both
## the tables
##
##########################################################

# Module Import #
import DataBaseDriver
from constants import *
import logging.config
logging.config.fileConfig(LOGGING_CONF)

##
## Class: ProjectAPI
## Description: This class is the database driver for Project
##
class ProjectAPI(DataBaseDriver.DataBaseDriver):
    PROJECT_TABLENAME = PROJECT_TABLE
    def __init__(self):
        self.logger = logging.getLogger('Market_Place')
        self.logger.info("IN - ProjectAPI constructor")
        DataBaseDriver.DataBaseDriver.__init__(self)

    ##
    ## Name: createProject
    ## Description: This function creates a new project
    ##
    ## Parameters: buyer dict with required values
    ##
    ## Returns: returns True if project is created
    ##
    def createProject(self, project):
        self.logger.info("IN - ProjectAPI createProject method")
        query = "INSERT INTO " + ProjectAPI.PROJECT_TABLENAME + \
                " (project_name, location, bid_end_time, seller_id, description) " \
                "VALUES (%s, %s, %s, %s, %s) "
        params = (project['project_name'], project['location'], project['bid_end_time'],
                  project['seller_id'], project['description'])
        self.logger.debug("Query: " + query)
        self.logger.debug("Params: %s, %s, %s, %s, %s",
                          project['project_name'], project['location'], project['bid_end_time'],
                          project['seller_id'], project['description'])
        return self.runInsertQuery(query, params)

    ##
    ## Name: getProjectId
    ## Description: This function returns project ID
    ## for a given project
    ##
    ## Parameters: project_name, seller_id
    ##
    ## Returns: returns project id
    ##
    def getProjectId(self, project_name, seller_id):
        self.logger.info("IN - ProjectAPI getProjectId method")
        query = "SELECT project_id from " + ProjectAPI.PROJECT_TABLENAME + \
                " WHERE project_name = '" + project_name + "' AND seller_id = '" + seller_id + "'"
        self.logger.debug("Query: " + query)
        return int(self.runSelectDfQuery(query).project_id[0])


    ##
    ## Name: getProjectId
    ## Description: This function returns project info
    ## for a given project_id
    ##
    ## Parameters: project_id
    ##
    ## Returns: returns dataframe containing info for project
    ##
    def getProjectInfo(self, project_id):
        self.logger.info("IN - ProjectAPI getProjectInfo method")
        query = "SELECT project_id, project_name, location, bid_end_time, " \
                "seller_id, buyer_id, description, creation_time FROM " + ProjectAPI.PROJECT_TABLENAME + " WHERE project_id = " + str(project_id)
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query)

    ##
    ## Name: getAllProjects
    ## Description: This function returns info for
    ## all the projects in the db
    ##
    ## Parameters:
    ##
    ## Returns: returns dataframe containing info for
    ## all the projects
    ##
    def getAllProjects(self):
        self.logger.info("IN - ProjectAPI getAllProjects method")
        query = "SELECT project_id, project_name, location, bid_end_time, " \
                "seller_id, buyer_id, description, creation_time FROM " + ProjectAPI.PROJECT_TABLENAME
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query)

    ##
    ## Name: getAllProjectsForBuyers
    ## Description: This function returns info for
    ## all the projects in the db for buyer_id
    ##
    ## Parameters: buyer_id
    ##
    ## Returns: returns dataframe containing info for
    ## all the projects
    ##
    def getAllProjectsForBuyers(self,buyer_id):
        self.logger.info("IN - ProjectAPI getAllProjectsForBuyers method")
        query = "SELECT project_id, project_name, location, bid_end_time, " \
                "seller_id, buyer_id, description, creation_time FROM " + ProjectAPI.PROJECT_TABLENAME + " WHERE buyer_id = '" + buyer_id + "'"
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query)

    ##
    ## Name: getAllProjectsForSellers
    ## Description: This function returns info for
    ## all the projects in the db for seller
    ##
    ## Parameters: seller_id
    ##
    ## Returns: returns dataframe containing info for
    ## all the projects
    ##
    def getAllProjectsForSellers(self, seller_id):
        self.logger.info("IN - ProjectAPI getAllProjectsForSellers method")
        query = "SELECT project_id, project_name, location, bid_end_time, " \
                "seller_id, buyer_id, description, creation_time FROM " + ProjectAPI.PROJECT_TABLENAME + " WHERE seller_id = '" + seller_id + "'"
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query)

    ##
    ## Name: getProjectNameForProject
    ## Description: This function returns name
    ## for a given project
    ##
    ## Parameters: project_id
    ##
    ## Returns: returns project name
    ##
    def getProjectNameForProject(self, project_id):
        self.logger.info("IN - ProjectAPI getProjectNameForProject method")
        query = "SELECT project_name FROM " + ProjectAPI.PROJECT_TABLENAME + " WHERE project_id = " + str(project_id)
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query).project_name[0]

    ##
    ## Name: setProjectNameForProject
    ## Description: This function updates the project
    ## name in the database
    ##
    ## Parameters: project_id, project_name
    ##
    ## Returns: returns True if updated else False
    ##
    def setProjectNameForProject(self, project_id, project_name):
        self.logger.info("IN - ProjectAPI setProjectNameForProject method")
        query = "UPDATE " + ProjectAPI.PROJECT_TABLENAME + " SET project_name = '" + project_name +  "' WHERE project_id = " + str(project_id)
        self.logger.debug("Query: " + query)
        return self.runUpdateQuery(query)

    ##
    ## Name: getLocationForProject
    ## Description: This function returns project location
    ## for a given project
    ##
    ## Parameters: project_id
    ##
    ## Returns: returns project location
    ##
    def getLocationForProject(self, project_id):
        self.logger.info("IN - ProjectAPI getLocationForProject method")
        query = "SELECT location FROM " + ProjectAPI.PROJECT_TABLENAME + " WHERE project_id = " + str(project_id)
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query).location[0]

    ##
    ## Name: setLocationForProject
    ## Description: This function updates project location
    ## in the db
    ##
    ## Parameters: project_id, location
    ##
    ## Returns: returns True if updated else False
    ##
    def setLocationForProject(self, project_id, location):
        self.logger.info("IN - ProjectAPI setLocationForProject method")
        query = "UPDATE " + ProjectAPI.PROJECT_TABLENAME + " SET location = '" + location +  "' WHERE project_id = " + str(project_id)
        self.logger.debug("Query: " + query)
        return self.runUpdateQuery(query)

    ##
    ## Name: setBuyerForProject
    ## Description: This function updates the buyer_id
    ## for a project in the db
    ##
    ## Parameters: project_id, buyer_id
    ##
    ## Returns: returns True if updated else False
    ##
    def setBuyerForProject(self, project_id, buyer_id):
        self.logger.info("IN - ProjectAPI setBuyerForProject method")
        query = "UPDATE " + ProjectAPI.PROJECT_TABLENAME + " SET buyer_id = '" + buyer_id + "' WHERE project_id = " + str(project_id)
        self.logger.debug("Query: " + query)
        return self.runUpdateQuery(query)

    ##
    ## Name: getBuyerForProject
    ## Description: This function returns the buyer_id
    ## for a project in the db
    ##
    ## Parameters: project_id
    ##
    ## Returns: returns the buyer_id for the project
    ##
    def getBuyerForProject(self, project_id):
        self.logger.info("IN - ProjectAPI getBuyerForProject method")
        query = "SELECT buyer_id FROM " + ProjectAPI.PROJECT_TABLENAME + " WHERE project_id = " + str(project_id)
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query).buyer_id[0]

    ##
    ## Name: getBidEndTimeForProject
    ## Description: This function returns project bid_end_time
    ## from the db
    ##
    ## Parameters: project_id
    ##
    ## Returns: returns bid_end_time
    ##
    def getBidEndTimeForProject(self, project_id):
        self.logger.info("IN - ProjectAPI getBidEndTimeForProject method")
        query = "SELECT bid_end_time FROM " + ProjectAPI.PROJECT_TABLENAME + " WHERE project_id = " + str(project_id)
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query).bid_end_time[0]

    ##
    ## Name: load
    ## Description: This function loads the project info
    ## directly from the dataframe given
    ##
    ## Parameters: dataframe df
    ##
    ## Returns: True if all rows inserted else false
    ##
    def load(self, df):
        self.logger.info("IN - ProjectAPI load method")
        check = False
        for index, row in df.iterrows():
            project_dict = {'project_name' : row['project_name'], 'bid_end_time' : row['bid_end_time'], 'location': row['location'],
                         'seller_id' : row['seller_id'], 'description': row['description']}
            if not self.createProject(project_dict):
                self.logger.error("Could not load data in Project table: " + row)
                check = False
            self.logger.debug("Loaded data in Buyer table: " + row)
        return check


