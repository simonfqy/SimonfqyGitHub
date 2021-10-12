'''
https://www.lintcode.com/problem/526/
'''

# My own solution, but largely followed the solution on jiuzhang.com for question 657 (which is very similar to this one):
# https://github.com/simonfqy/SimonfqyGitHub/blob/5f1c136ae8f166a1fca32cfa0cad7cb990f30a23/lintcode/medium/657_insert_delete_getrandom_O(1).py#L96,
# which makes sure that add(), remove() and pick() operations all have O(1) time complexity.
import random
class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.server_id_to_ind = dict()
        self.servers = []

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        self.server_id_to_ind[server_id] = len(self.servers)
        self.servers.append(server_id)

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        bad_server_ind = self.server_id_to_ind[server_id]
        last_server_id = self.servers[-1]

        self.servers[bad_server_ind] = last_server_id
        self.server_id_to_ind[last_server_id] = bad_server_ind
        
        del self.server_id_to_ind[server_id]
        self.servers.pop()

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        return self.servers[random.randint(0, len(self.servers) - 1)]
