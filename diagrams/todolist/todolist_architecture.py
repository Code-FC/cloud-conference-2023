from diagrams import Edge, Cluster, Diagram
from diagrams.onprem.client import Client
from diagrams.azure.web import AppServices
from diagrams.azure.database import SQLDatabases


with Diagram("Website landscape", 
             filename="landscape_architecture",
             show=False):
    client = Client("Web browser")

    with Cluster("Azure"):
        webapp = AppServices("Web Apps")                
        sqlDatabase = SQLDatabases("SQL Database")    
    
    client >>  webapp
    
    webapp >> sqlDatabase    


    
