##########################################################
##
## File: ProjectDB.py
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
import datetime
import logging.config
import json
logging.config.fileConfig(LOGGING_CONF)

##
## Class: ProjectDB
## Description: This class is the database driver for Project
##
class ProjectDB(DataBaseDriver.DataBaseDriver):
    projectTablename = PROJECT_TABLE
    def __init__(self):
        self.logger = logging.getLogger('Market_Place')
        self.logger.info("IN - ProjectDB constructor")
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
        self.logger.info("IN - ProjectDB.createProject")
        #project_id, project_name, location, bid_end_time, seller_id, buyer_id, description, creation_time
        query = "INSERT INTO " + ProjectDB.projectTablename + \
                " (project_id, project_name, location, bid_end_time, seller_id, buyer_id, description, creation_time) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP) ON DUPLICATE KEY " \
                "UPDATE project_name = %s, location = %s, bid_end_time = %s, " \
                "seller_id = %s, buyer_id = %s, description = %s"
        params = (project['project_id'], project['project_name'], project['location'], project['bid_end_time'],
                  project['seller_id'], project['buyer_id'], project['description'],
                  project['project_name'], project['location'], project['bid_end_time'],
                  project['seller_id'], project['buyer_id'],project['description'])
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
        self.logger.info("IN - ProjectDB.getProjectId")
        query = "SELECT project_id from " + ProjectDB.projectTablename + \
                " WHERE project_name = '" + project_name + "' AND seller_id = '" + seller_id + "'"
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query).project_id[0]


    ##
    ## Name: getProjectInfo
    ## Description: This function returns project info
    ## for a given project_id
    ##
    ## Parameters: project_id
    ##
    ## Returns: returns dataframe containing info for project
    ##
    def getProjectInfo(self, project_id):
        self.logger.info("IN - ProjectDB.getProjectInfo")
        query = "SELECT project_id, project_name, location, bid_end_time, " \
                "seller_id, buyer_id, description, creation_time FROM " + ProjectDB.projectTablename + " WHERE project_id = " + str(project_id)
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
        self.logger.info("IN - ProjectDB.getAllProjects")
        query = "SELECT project_id, project_name, location, bid_end_time, " \
                "seller_id, buyer_id, description, creation_time FROM " + ProjectDB.projectTablename
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
        self.logger.info("IN - ProjectDB.getAllProjectsForBuyers")
        query = "SELECT project_id, project_name, location, bid_end_time, " \
                "seller_id, buyer_id, description, creation_time FROM " + ProjectDB.projectTablename + " WHERE buyer_id = '" + buyer_id + "'"
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
        self.logger.info("IN - ProjectDB.getAllProjectsForSellers")
        query = "SELECT project_id, project_name, location, bid_end_time, " \
                "seller_id, buyer_id, description, creation_time FROM " + ProjectDB.projectTablename + " WHERE seller_id = '" + seller_id + "'"
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query)

    ##
    ## Name: getMostRecentNProjects
    ## Description: This function is called to retrieve
    ## top n most recent projects
    ##
    ## Parameters: n
    ##
    ## Returns: returns dataframe with top n most recent
    ## projects' info if exists else returns empty dataframe
    ##
    def getMostRecentNProjects(self, n):
        self.logger.info("IN - ProjectDB.getMostRecentNProjects")
        query = "SELECT project_id, project_name, location, bid_end_time, " \
                "seller_id, buyer_id, description, creation_time FROM " \
                + ProjectDB.projectTablename + " ORDER BY creation_time DESC LIMIT " + str(n)
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query)

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
        self.logger.info("IN - ProjectDB.setBuyerForProject")
        query = "UPDATE " + ProjectDB.projectTablename + " SET buyer_id = '" + buyer_id + "' WHERE project_id = " + str(project_id)
        self.logger.debug("Query: " + query)
        return self.runUpdateQuery(query)

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
        self.logger.info("IN - ProjectDB.getBidEndTimeForProject")
        query = "SELECT bid_end_time FROM " + ProjectDB.projectTablename + " WHERE project_id = " + str(project_id)
        self.logger.debug("Query: " + query)
        return self.runSelectDfQuery(query).bid_end_time[0]

    ##
    ## Name: removeProject
    ## Description: This function removes project
    ## from the db
    ##
    ## Parameters: project_id
    ##
    ## Returns: Returns True if deleted else False
    ##
    def removeProject(self,project_id):
        self.logger.info("IN - BidDB.removeBid")
        query = "DELETE FROM " + ProjectDB.projectTablename + " WHERE project_id=" + str(project_id)
        self.logger.debug("Query: " + query)
        return self.runDeleteQuery(query)

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
        self.logger.info("IN - ProjectDB.load")
        check = False
        for index, row in df.iterrows():

            project_dict = {'project_id': row['project_id'], 'project_name' : row['project_name'], 'bid_end_time' : row['bid_end_time'],
                            'location': row['location'], 'seller_id' : row['seller_id'], 'buyer_id': None, 'description': row['description'],
                            'creation_time' :str(datetime.datetime.now())}
            if not self.createProject(project_dict):
                self.logger.error("Could not load data in Project table: ")
                self.logger.error(row)
                check = False
            self.logger.debug("Loaded data in Project table: ")
            self.logger.debug(row)
        return check

    ##
    ## Name: jsonEncoder
    ## Description: This function converts the passed
    ## dataframe for ProjectDB class into json and
    ## checks the format of code sent
    ##
    ## Parameters: dataframe df
    ##
    ## Returns: returns json data
    ##
    def jsonEncoder(self,input_df):
        column_list = input_df.columns.tolist()

        try:
            #project_id, project_name, location, bid_end_time, seller_id, buyer_id, description, creation_time
            column_list = input_df.columns.tolist()
            print column_list
            if 'project_id' not in column_list or 'project_name' not in column_list \
            or 'location' not in column_list or 'bid_end_time' not in column_list \
            or 'seller_id' not in column_list or 'buyer_id' not in column_list \
            or 'description' not in column_list or 'creation_time' not in column_list:
                print "here"
                return None

            output_json = input_df.to_json(orient='records')
            print output_json
            return output_json
        except TypeError, e:
            self.logger.error("Cannot convert input dataframe to json: " + str(e))
            return None

    ##
    ## Name: jsonDecoder
    ## Description: This function converts passed json data
    ## for ProjectDB class into dict and checks
    ## if the json has required fields
    ##
    ## Parameters: json
    ##
    ## Returns: Returns dict
    ##
    def jsonDecoder(self, input_json):
        try:
            output_dict = json.loads(input_json)[0]
        # the dict should have project_id, project_name, bid_end_time, seller_id and description
            if not output_dict['project_id'] or not output_dict['project_name'] or not output_dict['location']\
                or not output_dict['bid_end_time']or not output_dict['seller_id'] or not output_dict['buyer_id'] or not output_dict['description']:
                return None
            else:
                return output_dict

        except IndexError, e:
            self.logger.error("Input data passed is not correct: " + str(e))
            return None







