from py2neo import neo4j,node, rel  , graph 

graph = Graph()

authenticate("localhost:7474", "neo4j", "python")
#Create node
user, = graph_db.create({"name":"Greg",'business':"Graph Story"})

# Retrive and updating Nodes
#find the uder by the node id
UserNode =graph_db.node(1)

#update a property
UserNode.set_propertird({"business": "Graph Story" })
# delete the node
UserNode.delete()

#Create two nodes
greg, = graph_db.create({"name": "Greg"})
brad, = graph_db.create({"name": "Brad"})

#Create the relationship between the tow nodes
graph_db.create(rel(greg,"FOLLOWS", brad))

#quering with a label
#users = list(graph_db.find('User', property_key='name',property_value='brad'))










