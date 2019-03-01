from .views import app
from .models import graph

graph.cypher.execute("CREATE CONSTRAIN ON (n:User) ASSERT n.username IS UNIQUE")
graph.cypher.execute("CREATE CONSTRAIN ON (n:Argument) ASSERT n.id IS UNIQUE")
#graph.cypher.execute("CREATE CONSTRAIN ON (n:Tag) ASSERT n.name IS UNIQUE")
#graph.cypher.execute("CREATE INDEX ON :Argument(claim_title)")