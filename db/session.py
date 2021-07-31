from py2neo import Graph
from core.config import settings


graph = Graph('bolt://localhost:'+settings.NEO4J_PORT, auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD),
              name=settings.NEO4J_DB)  # user - password - database


def get_db():
    try:
        graph.run("Match () Return 1 Limit 1")
        print('ok')
        return graph
    except Exception:
        print('not ok')
