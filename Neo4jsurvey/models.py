'''
Created on 10 Feb 2019

@author: A.Braca
'''


from py2neo import Graph, Node, Relationship, authenticate
from passlib.hash import bcrypt
from datetime import datetime
import uuid
import pdb
import sys   



graph = Graph()  

authenticate("localhost:7474", "neo4j", "python")



class User:
    def __init__(self, username):
        self.username = username


    def find(self):
        user = graph.find_one("User", "username", self.username)
        return user

    def register(self, password):
        if not self.find():
            user = Node("User", username=self.username, password=password)
            graph.create(user)
            return True
        return False

    def verify_password(self, password):
        user = self.find()

        if not user:
            return False

        return password ==user["password"]



    def add_survey(self,gender,
                        sexuality,
                        ethnicity,
                        occupation,
                        marital_status,
                        education,
                        vehicle,
                        age,
                        religion,
                        recreation):
        user = self.find()

        demographic = Node(
            "Demographic",
            id=str(uuid.uuid4()),
            gender=gender,
            sexuality=sexuality,
            ethnicity=ethnicity,
            occupation=occupation,
            marital_status=marital_status,
            education=education,
            vehicle=vehicle,
            religion=religion,
            age=age,
            recreation=recreation,
            timestamp=int(datetime.now().strftime("%s")),
            date=datetime.now().strftime("%F")
        )

        rel = Relationship(user, "DEMOGRAPHIC_FACTORS", demographic)
        graph.create(rel)
    

    def add_personality(self, likert):
        user=self.find()
        personality = Node(
        "Personality",
        id=str(uuid.uuid4()),
        p1=likert[0],
        p2=likert[1],
        p5=likert[2],
        p8=likert[3],
        p10=likert[4],
        p12=likert[5],
        p18=likert[6],
        p19=likert[7],
        p20=likert[8],
        p24=likert[9],
        p27=likert[10],
        p28=likert[11],
        p29=likert[12],
        p30=likert[13], 
        p31=likert[14],
        p32=likert[15],
        p33=likert[16],
        p34=likert[17],
        p36=likert[18],
        p37=likert[19],
        p39=likert[20],
        p40=likert[21], 
        p42=likert[22], 
        p44=likert[23],
        p46=likert[24],
        p47=likert[25],
        p48=likert[26],
        p49=likert[27],
        p50=likert[28],
        p51=likert[29],
        timestamp=int(datetime.now().strftime("%s")),
        date=datetime.now().strftime("%F")
        )
        rel2 = Relationship(user, "PERSONALITY_TRAITS", personality)
        graph.create(rel2)

    def add_values(self, likert):
        user=self.find()
        values = Node(
        "Values",
        id=str(uuid.uuid4()),
        v1=likert[0],
        v2=likert[1],
        v3=likert[2],
        v4=likert[3],
        v5=likert[4],
        v6=likert[5],
        v7=likert[6],
        v8=likert[7],
        v9=likert[8],
        v10=likert[9],
        v11=likert[10],
        v12=likert[11],
        v13=likert[12],
        v14=likert[13], 
        v15=likert[14],
        v16=likert[15],
        v17=likert[16],
        v18=likert[17],
        v19=likert[18],
        v20=likert[19],
        v21=likert[20],
        v22=likert[21],
        v23=likert[22], 
        v24=likert[23],
        v25=likert[24],
        v26=likert[25],
        v27=likert[26],
        v28=likert[27],
        v29=likert[28],
        v30=likert[29],
        v31=likert[30],
        v32=likert[31],
        v33=likert[32],
        timestamp=int(datetime.now().strftime("%s")),
        date=datetime.now().strftime("%F")
        )
        rel_values = Relationship(user, "VALUES", values)
        graph.create(rel_values)





        
    def add_arguments(self,
                            issue, side,type_schema, premise_type, 
                            argu, major_premise,evidence,minor_premise,
                            conclusion,type_dialog,influence_social,
                            support, source):
        
        user=self.find()
        print("Adding arguments")
        print (issue, side, type_schema,premise_type, 
                            argu, major_premise,minor_premise,
                            conclusion,type_dialog,influence_social,
                            support, source)

        argument = Node(
            "Argument",
            id=str(uuid.uuid4()),
            issue=issue, 
            side=side,
            type_schema=type_schema,
            premise_type=premise_type, 
            argu=argu, 
            major_premise=major_premise,
            minor_premise=minor_premise,
            conclusion=conclusion,
            type_dialog=type_dialog,
            influence_social=influence_social,
            support=support, 
            source=source, 
            
        )
        graph.create(argument)
        rel_admin_argu = Relationship(user, "Admin_Present_Arguments", argument)
        print(rel_admin_argu)
        graph.create(rel_admin_argu)


    def like_argument(self, argument_id):
        user = self.find()
        post = graph.find_one("Argument", "id",argument_id)
        rel_agree = Relationship(user, "AGREE",post)
        graph.merge(rel_agree)
        graph.create_unique(rel_agree)
    
    def add_ratings(self,stars):
        user = self.find()
      
        rates= Node(
        "Ratings",
        id=str(uuid.uuid4()),
        rating=stars,
        )
        rel_stars = Relationship(user, "RATING",rates)
        graph.create_unique(rel_stars)
   
        print(rel_stars)

 
      
"""
        if stars:
            d = []
            for key in stars:
                try:
                    i = self.index(key)
                except KeyError:
                    d.append(None)
                else:
                    d.append(self[i])
            return d

"""           
     


       

       
        
        

  


            

def display():
       
        posts = graph.cypher.execute("match(n:Argument)return n")
        postsA= graph.cypher.execute("MATCH (n:Argument)WHERE n.side='SideA'RETURN n")
        postsB= graph.cypher.execute("MATCH (n:Argument)WHERE n.side='SideB'RETURN n")
        #test = graph.cypher.execute("MATCH (n:Argument)WHERE n.side='SideA'RETURN n SKIP 1 LIMIT 1 ")

       
        print()
       
       
        print (posts)
        print (type(posts))
       
    
    
        return posts 


        



