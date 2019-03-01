
" " "
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
        

" " "


        argu_post = graph.find_one("Argument","id","argument_id" )
        graph.merge_one(Relationship(user, "AGREES", argu_post))