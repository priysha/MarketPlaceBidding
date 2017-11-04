##########################################################
##
## File: DataBaseDriver.py
## Author: Priysha Pradhan
## Description: This class is a base class to setup DB
## connection and run MySql db queries
##
##########################################################

# Module Import #
import pymysql
import pandas as pd
from constants import *

##
## Class: DataBaseDriver
## Description: This class is a base class for MySql db connection and queries
##
class DataBaseDriver(object):

    def __init__(self):
        self.conn = pymysql.connect(host=DB_HOST,
                                    user=DB_USER,
                                    passwd=DB_PASSWORD,
                                    db=DB_NAME)
        self.cursorDict = self.conn.cursor(pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.cursorDict.close()
        self.conn.close()

    ##
    ## Name: getConn
    ## Description: Getter function that returns the MySql connector
    ##
    ## Parameters:
    ## None
    ##
    ## Returns: Return the MySql connector
    ##
    def getConn(self):
        return self.conn


    ##
    ## Name: getCursorDict
    ## Description: Getter function that returns the MySql cursor
    ## with values in a dictionary format
    ##
    ## Parameters: conn
    ##
    ## Returns: Return the MySql cursor in a dict format
    ##
    def getCursorDict(self):
        return self.cursorDict


    ##
    ## Name: getCursor
    ## Description: Getter function that returns the MySql cursor
    ##
    ## Parameters: conn
    ##
    ## Returns: Return the MySql cursor
    ##
    def getCursor(self):
        return self.cursor

    ##
    ## Name: commitConn
    ## Description: This function commits the db connection
    ##
    ## Parameters: conn
    ##
    ## Returns: none
    ##
    def commitConn(self):
        self.conn.commit()

    ##
    ## Name: closeConn
    ## Description: This function closes the db connection
    ##
    ## Parameters: conn
    ##
    ## Returns: none
    ##
    def closeConn(self):
        self.cursor.close()
        self.cursorDict.close()
        self.conn.close()

    ##
    ## Name: executeQuery
    ## Description: This function runs given query
    ## and returns value if SELECT query is run
    ##
    ## Parameters: query
    ##
    ## Returns: True if the query runs successfully, else False
    ## returns query result in list for select query
    ##
    def executeQuery(self, query):
        try:
            self.cursor.execute(query)
            self.commitConn()

            if "SELECT" in query or "SHOW" in query:
                db_resp = self.cursor.fetchall()
                return db_resp
            else:
                return True
        except Exception as err:
            print("\n\nError in database query: " + query)
            print("Error Status:\n" + str(err))
            return False

    ##
    ## Name: prepareSelectQuery
    ## Description: This function prepares select query
    ## using given params
    ##
    ## Parameters: table_name, fields, where_clause
    ##
    ## Returns: returns select query result else False
    ##
    def prepareSelectQuery(self, table_name, fields, where_clause='1=1'):
        selectQuery = "SELECT " + fields + " FROM " + table_name + " WHERE " + where_clause
        return self.executeQuery(selectQuery)

    ##
    ## Name: prepareInsertQuery
    ## Description: This function prepares insert query
    ## using given params
    ##
    ## Parameters: table_name, fields, values
    ##
    ## Returns: True if the query runs successfully, else False
    ##
    def prepareInsertQuery(self, table_name, fields, values):
        insertQuery = " INSERT INTO " + table_name + fields + " VALUES " + values
        return self.executeQuery(insertQuery)

    ##
    ## Name: prepareUpdateQuery
    ## Description: This function prepares update query
    ## using given params
    ##
    ## Parameters: table_name, setVal, where_clause
    ##
    ## Returns: True if the query runs successfully, else False
    ##
    def prepareUpdateQuery(self, table_name, setVal, where_clause='1=1'):
        updateQuery = "UPDATE " + table_name + " SET " + setVal + " WHERE " + where_clause
        return self.executeQuery(updateQuery)

    ##
    ## Name: runUpdateQuery
    ## Description: This function prepares delete query
    ## using given params
    ##
    ## Parameters: table_name, where_clause
    ##
    ## Returns: True if the query runs successfully, else False
    ##
    def prepareDeleteQuery(self, table_name, where_clause='1=1'):
        deleteQuery = "DELETE FROM " + table_name + " WHERE " + where_clause
        return self.executeQuery(deleteQuery)

    ##
    ## Name: prepareReplaceQuery
    ## Description: This function prepares replace query
    ## using given params
    ##
    ## Parameters: table_name, fields, values
    ##
    ## Returns: True if the query runs successfully, else False
    ##
    def prepareReplaceQuery(self, table_name, fields, values):
        replaceQuery = " REPLACE INTO " + table_name + fields + " VALUES " + values
        return self.executeQuery(replaceQuery)

    ##
    ## Name: runUpdateQuery
    ## Description: This function runs the update query
    ##
    ## Parameters: query, type
    ##
    ## Returns: True if the query runs successfully, else False
    ##
    def runUpdateQuery(self, query):
        try:
            self.cursor.execute(query)
            self.commitConn()
            return True

        except Exception, e:
            print ("\nError executing SQL UPDATE query: " + query + "\nError status:" + str(e))
            return False

    ##
    ## Name: runDeleteQuery
    ## Description: This function runs the delete query
    ##
    ## Parameters: query, type
    ##
    ## Returns: True if the query runs successfully, else False
    ##
    def runDeleteQuery(self, query):
        try:
            self.cursor.execute(query)
            self.commitConn()
            return True

        except Exception, e:
            print ("\nError executing SQL DELETE query: " + query + "\nError status:" + str(e))
            return False

    ##
    ## Name: selectDfQuery
    ## Description: This function returns the select query
    ## result in a pandas dataframe format
    ##
    ## Parameters: query
    ##
    ## Returns: dataframe with select query result
    ##
    def runSelectDfQuery(self, query):

        try:
            df = pd.read_sql(query, con=self.conn)
            return df
        except Exception, e:
            df = pd.DataFrame()
            print ("\nError executing SQL SELECT query: " + query + "\nError status:" + str(e))
            return df

    ##
    ## Name: selectQuery
    ## Description: This function returns the select query
    ##
    ## Parameters: query
    ##
    ## Returns: select query result
    ##
    def runSelectQuery(self, query):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result

        except Exception, e:
            print ("\nError executing SQL SELECT query: " + query + "\nError status:" + str(e))
            return False

    ##
    ## Name: insertQuery
    ## Description: This function inserts the query into db
    ##
    ## Parameters: query, params
    ##
    ## Returns: returns True if successful else false
    ##
    def runInsertQuery(self,query, params):
        try:
            self.cursor.execute(query, params)
            self.commitConn()
            return True

        except Exception, e:
            print ("\nError executing SQL INSERT query: " + query + "\nError status:" + str(e))
            return False


    ##
    ## Name: runReplaceQuery
    ## Description: This function replaces the query into db
    ##
    ## Parameters: query, params
    ##
    ## Returns: returns True if successful else false
    ##
    def runReplaceQuery(self,query, params):
        try:
            self.cursor.execute(query, params)
            self.commitConn()
            return True

        except Exception, e:
            print ("\nError executing SQL REPLACE query: " + query + "\nError status:" + str(e))
            return False

    ##
    ## Name: runTruncateTableQuery
    ## Description: This function truncates table
    ## in the db
    ##
    ## Parameters: table_name
    ##
    ## Returns: returns True if successful else false
    ##
    def runTruncateTableQuery(self, table_name):
        query = "TRUNCATE TABLE " + table_name
        try:
            self.cursor.execute(query)
            self.commitConn()
            return True

        except Exception, e:
            print ("\nError executing SQL REPLACE query: " + query + "\nError status:" + str(e))
            return False


