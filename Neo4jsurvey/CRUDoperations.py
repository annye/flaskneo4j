'''
Created on 10 Feb 2019

@author: A.Braca
'''
from py2neo import Graph
from py2neo.ext.ogm import Store
import py2neo
from models import Person, Argument

class  DeleteNodes(object):
    """Define the Delete Operation on Nodes"""
    
    def __init__(self,host,port,username,password):
        #Authenticate and Connect to the Neo4j Graph Database
        py2neo.authenticate(host+':'+port, username, password)
        graph = Graph('http://'+host+':'+port+'/db/data/')
        store = Store(graph)
        #Store the reference of Graph and Store.
        self.graph=graph
        self.store=store
    def deletePersonNode(self,node):
        #Load the node from the Neo4j Legacy Index
        cls = self.store.load_indexed('personIndex', 'name', node.name, Person)
        #Invoke delete method of store class
        self.store.delete(cls[0])
    def deleteArgumentNode(self,node):
        #Load the node from the Neo4j Legacy Index
        cls = self.store.load_indexed('argumentIndex', 'name',node.argumentName, Argument)
        #Invoke delete method of store class
        self.store.delete(cls[0])
        


 
class UpdateNodesRelationships(object):
    '''
     Define the Update Operation on Nodes
    '''

    def __init__(self,host,port,username,password):
        #Authenticate and Connect to the Neo4j Graph Database
        py2neo.authenticate(host+':'+port, username, password)
        graph = Graph('http://'+host+':'+port+'/db/data/')
        store = Store(graph)
        #Store the reference of Graph and Store.
        self.graph=graph
        self.store=store  
        
    def updatePersonNode(self,oldNode,newNode):
        #Get the old node from the Index
        cls = self.store.load_indexed('personIndex', 'name', oldNode.name, Person)
        #Copy the new values to the Old Node
        cls[0].username=newNode.username
        cls[0].password=newNode.password
        cls[0].gender=newNode.gender
      
        #Delete the Old Node form Index
        self.store.delete(cls[0])
        #Persist the updated values again in the Index
        self.store.save_unique('personIndex', 'username', newNode.username, cls[0])
    
    def updateArgumentNode(self,oldNode,newNode):
        #Get the old node from the Index
        cls = self.store.load_indexed('argumentIndex', 'name', oldNode.argumentName, Argument)
        #Copy the new values to the Old Node
        cls[0].argumentName=newNode.argumentName
        #Delete the Old Node form Index
        self.store.delete(cls[0])
        #Persist the updated values again in the Index
        self.store.save_unique('personIndex', 'username', newNode.username, cls[0])
        

        
class CreateNodesRelationships(object):
    '''
    Define the Create Operation on Nodes
    '''

    def __init__(self,host,port,username,password):
        #Authenticate and Connect to the Neo4j Graph Database
        py2neo.authenticate(host+':'+port, username, password)
        graph = Graph('http://'+host+':'+port+'/db/data/')
        store = Store(graph)
        #Store the reference of Graph and Store.
        self.graph=graph
        self.store=store
    """
    Create a person and store it in the Person Dictionary. 
    Node is not saved unless save() method is invoked. Helpful in bulk creation
    """   
    def createPerson(self,username,password=None,gender=None):
        person = Person(username,password,gender)
        return person
    
    """
    Create a movie and store it in the Argument Dictionary. 
    Node is not saved unless save() method is invoked. Helpful in bulk creation
    """           
    def createArgument(self,argumentName):
        argument = Argument(argumentName)
        return argument


    """
    Create a HAS_RATED relationships between 2 nodes and invoke a local method of Store class. 
    Relationship is not saved unless Node is saved or save() method is invoked. 
    """


    def createHasRatedRelationship(self,startPerson,argument,ratings):
        self.store.relate(startPerson, 'HAS_RATED', argument,{'ratings':ratings})
    """
    Based on type of Entity Save it into the Server/ database
    """
    def save(self,entity,node):
        if(entity=='person'):
            self.store.save_unique('personIndex', 'username', node.username, node)
        else:
            self.store.save_unique('argumentIndex','name',node.argumentName,node)
            

    
        