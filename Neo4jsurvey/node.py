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



CALL db.schema()

CALL db.relationshipTypes()

CALL db.labels()

MATCH (n:Argument{issue:"Holidays_Greece"}) RETURN n
MATCH (n:User{username:"admin@admin"}) RETURN [(n)-->(a) WHERE a:argument | a.argu] AS  TEST





MATCH person=()-[r:AGREE]->() RETURN person

MATCH (n:Demographic{gender:"Male"}) RETURN n
match(n:Demographic{gender:"Female"}) return n
match (n) where (n)-[:AGREE]-(:Demographic{gender:"Male"}) return n.gender
match (n) -[r]->() where n.gender="Female" and type(r)=~"A.*" return type(r)


match statements=()-[:PRESENT_ARGUMENTS]-> ()
return statements



match (Malta:Argument{issue:"Holidays_ Malta"}) return  Malta

match (Greece:Argument{issue:"Holidays_Greece"}) return  Greece

result = graph.cypher.execute("match (n:Argument) return n.issue, n.argu")


#######################
        for record in graph.cypher.stream("MATCH (n:Argument)WHERE n.side='SideB'RETURN n"):
            print (record[0])
        
        print()
######################################################################################
"""
        topic = set(issue)
        for statement in topic:
            t = graph.merge_one("Issue","x", statement)
            rel4 = Relationship(t, "DIALOGS", argument)
            graph.create(rel4)
"""





@app.route("/like_argument/<argument_id>", methods=["GET","POST"])
def user_ratings(argument_id):
    ratings_list = ["1","2","3","4","5"]
    stars = []
    for element in ratings_list:
        value = request.form[element]
        stars.append(value)

    username = session.get("username")

    if not username:
        flash("You must be logged in to participate in the experiment.")
        return redirect(url_for("login"))

    user = User(username)
    
    user.user_ratings(argument_id)
    flash("Liked Dialogs.")
    return redirect(request.referrer)




    def user_ratings(self, argument_id,stars):
        user = self.find()
        post = graph.find_one("Argument", "id",argument_id)
        rates = Node(
        "Rates",
        id=str(uuid.uuid4()),
        1=stars[0],
        2=stars[1],
        3=stars[2],
        4=stars[3],
        5=stars[4],
        )
        graph.create(rates)
        rel_rates = Relationship(user, "RATES",rates)
        ratings_rel = Relationship(user, "A",post)
        graph.merge(ratings_rel)
        graph.create_unique(ratings_rel)


      





"MATCH (n:Argument)WHERE n.side='SideA'RETURN n SKIP 1LIMIT 1 "