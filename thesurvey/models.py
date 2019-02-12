'''
Created on 10 Feb 2019

@author: A.Braca
'''


from py2neo import Graph, Node, Relationship, authenticate
from passlib.hash import bcrypt
from datetime import datetime
import uuid
import pdb


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
        
    def add_arguments(self, 
                            issue, claim_title,argument, 
                            support, refutation,evidence,
                            reasons, emotional_appeals,
                            linguistic_technique, strength):
        
        user=self.find()

        argument = Node(
            "Argument",
            id=str(uuid.uuid4()),
            issue=issue,
            claim_title=claim_title,
            argument=argument, 
            support=support,
            refutation=refutation,
            evidence=evidence,
            reasons=reasons, 
            emotional_appeals=emotional_appeals,
            linguistic_technique=linguistic_technique, 
            strength=strength,
        )
        rel3 = Relationship(user, "RATES", Argument)
       
        graph.create(rel3)








"""
class Statement:
    def __int__(self, issue):
        self.issue = issue
        graph.create(issue)

    def find(self):
        issue = graph.find_one("Statement", issue=self.issue)
        return issue

    def add_arguments(self, 
                            issue, claim_title,argument, 
                            support, refutation,evidence,
                            reasons, emotional_appeals,
                            linguistic_technique, strength):
        issue = self.find()
        user=self.find()

        argument =Node(
            "Argument",
            id=str(uuid.uuid4()),
            claim_title=claim_title,
            argument=argument, 
            support=support,
            refutation=refutation,
            evidence=evidence,
            reasons=reasons, 
            emotional_appeals=emotional_appeals,
            linguistic_technique=linguistic_technique, 
            strength=strength,
        )
        rel_issue = Relationship(issue, "STRUCTURED", argument)
        graph.create(rel_issue)
        

"""

        

       