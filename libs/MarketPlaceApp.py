##########################################################
##
## File: MarketPlaceApp.py
## Author: Priysha Pradhan
## Description: This is where  our REST API is implemented
## and all the requests are handled and directed to
## corresponding class methods
## Authentication for rest requests is also implemented here
## api endpoints are defined at the end of the file
##
##########################################################

# Module Import #
from BuyerDB import BuyerDB
from SellerDB import SellerDB
from BidDB import BidDB
from ProjectDB import ProjectDB
from ProjectBidDB import ProjectBidDB
from flask_restful import Resource, Api, reqparse, fields, marshal
from flask import Flask, jsonify, abort, make_response, request
from flask_httpauth import HTTPBasicAuth
from constants import *

market_place = Flask(__name__)
api = Api(market_place)

BuyerDB = BuyerDB()
SellerDB = SellerDB()
BidDB = BidDB()
ProjectDB = ProjectDB()
ProjectBidDB = ProjectBidDB()
auth = HTTPBasicAuth()

USER_DATA = {
    USERNAME: PASSWORD
}


@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password


#Flask-RESTful provides a Resource base class that can define
# the routing for one or more HTTP methods for a given URL

##
## Class: BuyerAPI
## Description: Buyer API derived
## from Resource base class
##
class BuyerAPI(Resource):

    @auth.login_required
    def get(self, id=None):
        if id is None:
            df = BuyerDB.getAllBuyers()
            ret_val = BuyerDB.jsonEncoder(df)
        else:
            df = BuyerDB.getBuyerInfo(id)
            ret_val = BuyerDB.jsonEncoder(df)

        return ret_val

    @auth.login_required
    def put(self):
        json_data = request.json['data']
        if len(json_data)==0:
            abort(404)
        buyer_dict = BuyerDB.jsonDecoder(json_data)
        BuyerDB.createBuyer(buyer_dict)

    @auth.login_required
    def delete(self, id):
        if len(BuyerDB.getBuyerInfo(id)) == 0:
            abort(404)
        BuyerDB.removeBuyer(id)
        return {'result': True}

##
## Class: SellerAPI
## Description: Seller API derived
## from Resource base class
##
class SellerAPI(Resource):

    @auth.login_required
    def get(self, id=None):
        if id is None:
            df = SellerDB.getAllSellers()
            ret_val = SellerDB.jsonEncoder(df)
        else:
            df = SellerDB.getSellerInfo(id)
            ret_val = SellerDB.jsonEncoder(df)

        return ret_val

    @auth.login_required
    def put(self):
        json_data = request.json['data']
        if len(json_data)==0:
            abort(404)
        seller_dict = SellerDB.jsonDecoder(json_data)
        SellerDB.createSeller(seller_dict)

    @auth.login_required
    def delete(self, id):
        if len(SellerDB.getSellerInfo(id)) == 0:
            abort(404)
        SellerDB.removeSeller(id)
        return {'result': True}

##
## Class: BidAPI
## Description: Bid API derived
## from Resource base class
##
class BidAPI(Resource):

    @auth.login_required
    def get(self, id=None):
        if id is None:
            df = BidDB.getAllBids()
            ret_val = BidDB.jsonEncoder(df)
        else:
            df = BidDB.getBidInfo(id)
            ret_val = BidDB.jsonEncoder(df)

        return ret_val

    @auth.login_required
    def put(self):
        json_data = request.json['data']
        if len(json_data)==0:
            abort(404)
        bid_dict = BidDB.jsonDecoder(json_data)
        BidDB.createBid(bid_dict)

    @auth.login_required
    def delete(self, id):
        if len(BidDB.getBidInfo(id)) == 0:
            abort(404)
        BidDB.removeBid(id)
        return {'result': True}

##
## Class: ProjectAPI
## Description: Project API derived
## from Resource base class
##
class ProjectAPI(Resource):

    @auth.login_required
    def get(self, id=None):
        if id is None:
            df = ProjectDB.getAllProjects()
            ret_val = ProjectDB.jsonEncoder(df)
        else:
            df = ProjectDB.getProjectInfo(id)
            ret_val = ProjectDB.jsonEncoder(df)
        return ret_val

    @auth.login_required
    def put(self):
        json_data = request.json['data']
        if len(json_data)==0:
            abort(404)
        project_dict = ProjectDB.jsonDecoder(json_data)
        ProjectDB.createProject(project_dict)

    @auth.login_required
    def delete(self, id):
        if len(ProjectDB.getProjectInfo(id)) == 0:
            abort(404)
        ProjectDB.removeProject(id)
        return {'result': True}

##
## Class: ProjectBidsAPI
## Description: ProjectBids API derived
## from Resource base class which handles
## requests for getting eligible bids for a project
##
class ProjectBidsAPI(Resource):

    @auth.login_required
    def get(self, id=None):
        df = ProjectBidDB.getAllEligibleBidsForProject(id)
        ret_val = BidDB.jsonEncoder(df)
        return ret_val

##
## Class: ProjectMinBidAPI
## Description: ProjectMinBid API derived
## from Resource base class which handles
## requests for getting minimum bids for a project
##
class ProjectMinBidAPI(Resource):

    @auth.login_required
    def get(self, id=None):
        df = ProjectBidDB.getMinimumBidForProject(id)
        ret_val = BidDB.jsonEncoder(df)
        return ret_val

##
## Class: MostRecentNProjectsAPI
## Description: MostRecentNProjects API derived
## from Resource base class which handles
## requests for displaying most recent n projects
##
class MostRecentNProjectsAPI(Resource):

    @auth.login_required
    def get(self,n=None):
        if n is None:
            n = 100

        df = ProjectDB.getMostRecentNProjects(n)
        ret_val = ProjectDB.jsonEncoder(df)
        return ret_val

#The add_resource function registers the routes
# with the framework using the given endpoint
api.add_resource(BuyerAPI, '/buyers', endpoint="buyers")
api.add_resource(BuyerAPI, '/buyers/<id>', endpoint="buyer")
api.add_resource(SellerAPI, '/sellers', endpoint="sellers")
api.add_resource(SellerAPI, '/sellers/<id>', endpoint="seller")
api.add_resource(BidAPI, '/bids', endpoint="bids")
api.add_resource(BidAPI, '/bids/<id>', endpoint="bid")
api.add_resource(ProjectAPI, '/projects', endpoint="projects")
api.add_resource(ProjectAPI, '/projects/<id>', endpoint="project")
api.add_resource(ProjectBidsAPI, '/projects/<id>/bids', endpoint="project_bids")
api.add_resource(ProjectMinBidAPI, '/projects/<id>/min_bid', endpoint="project_min_bid")
api.add_resource(MostRecentNProjectsAPI, '/projects/most_recent/<n>', endpoint="project_most_recent")
api.add_resource(MostRecentNProjectsAPI, '/projects/most_recent', endpoint="project_most_recent100")

if __name__ == '__main__':
    market_place.run()