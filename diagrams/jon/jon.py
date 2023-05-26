from diagrams import Cluster, Diagram
from diagrams.onprem.client import Client
from diagrams.azure.web import AppServices
from diagrams.azure.database import SQLDatabases
from diagrams.azure.network import CDNProfiles


with Diagram("Perucas Landscape", 
            filename="jon",
            show=False):
    client = Client("Salão")

    with Cluster("Azure"):
        webapp = AppServices("Web Apps")                
        sqlDatabase = SQLDatabases("SQL Database")    
        cdn = CDNProfiles("CDN")

    client >>  webapp
    webapp >> cnd
    
    webapp >> sqlDatabase
