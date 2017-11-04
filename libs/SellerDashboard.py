##########################################################
##
## File: SellerDashboard.py
## Author: Priysha Pradhan
## Description: This class works for Seller's
## dashboard, all the requirements for seller can be retrived
## using these methods.
##
##########################################################

from Project import Project
from Bid import Bid
from Buyer import Buyer


class SellerDashboard:
    def __init__(self, sellerId):
        self.Project = Project()
        self.Bid = Bid()
        self.Buyer = Buyer()
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
        buyer_info = self.Buyer.getBuyerInfo(self.sellerId)
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
        all_projects = self.Project.getAllProjects()
        seller_projects = all_projects[all_projects.seller_id == self.sellerId]

        return seller_projects

    ##
    ## Name: addANewProject
    ## Description: This function is called to let
    ## seller add a new project with details
    ##
    ## Parameters: project_name, location, bid_end_time, start_date, due_date, description, skills, head_count
    ##
    ## Returns: returns True if project created
    ##
    def addANewProject(self, project_name, location, bid_end_time, start_date, due_date, description, skills, head_count):

        project = {'project_name' : project_name, 'location' : location, 'seller_id' : self.sellerId, 'bid_end_time' : bid_end_time}
        project_detail = {'start_date' : start_date, 'due_date' : due_date, 'skills' : skills, 'head_count' : head_count,
                   'description' : description}
        prj_created = self.Project.createProject(project)
        project_detail['project_id'] = self.Project.getProjectId(project_name, self.sellerId)
        self.addProjectDetail(project_detail)

        return prj_created

    ##
    ## Name: addProjectDetail
    ## Description: This function is called to add the
    ## corresponding project details for the project
    ##
    ## Parameters: project_detail dict
    ##
    ## Returns: returns True if details added
    ##
    def addProjectDetail(self, project_detail):

        return self.Project.createProjectDetail(project_detail)



