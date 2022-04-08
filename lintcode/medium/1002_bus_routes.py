'''
'''

# My own solution. Uses BFS. Should be correct, but causes memory limit exceeded exception.
from typing import (
    List,
)

from collections import deque
class Solution:
    """
    @param routes:  a list of bus routes
    @param s: start
    @param t: destination
    @return: the least number of buses we must take to reach destination
    """
    def num_buses_to_destination(self, routes: List[List[int]], s: int, t: int) -> int:
        route_ind_to_places = dict()
        place_ind_to_routes = dict()
        for i, route in enumerate(routes):
            route_ind_to_places[i] = route
            for place_ind in route:
                if place_ind not in place_ind_to_routes:
                    place_ind_to_routes[place_ind] = set()
                place_ind_to_routes[place_ind].add(i)
        return self.get_distance(route_ind_to_places, place_ind_to_routes, s, t)
        
    def get_distance(self, route_ind_to_places, place_ind_to_routes, s, t):
        if s == t and s in place_ind_to_routes:
            return 0
        visited_routes = set([])
        visited_places = set([s])
        queue = deque([s])
        length = 0
        while queue:
            size = len(queue)
            length += 1
            for _ in range(size):
                place = queue.popleft()
                routes_this_place_belongs_to = place_ind_to_routes[place]
                for route_id in routes_this_place_belongs_to:
                    if route_id in visited_routes:
                        continue
                    for place_id in route_ind_to_places[route_id]:
                        if place_id == t:
                            return length
                        if place_id in visited_places:
                            continue
                        queue.append(place_id)
                        visited_places.add(place_id)
                visited_routes |= routes_this_place_belongs_to

        return -1
      

# My own solution. Very similar to the one above, but now changed the set to list and avoided the memory limit exceeded exception.
from collections import deque, defaultdict
class Solution:
    """
    @param routes:  a list of bus routes
    @param s: start
    @param t: destination
    @return: the least number of buses we must take to reach destination
    """    
    def num_buses_to_destination(self, routes: List[List[int]], s: int, t: int) -> int:        
        place_ind_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for place_ind in route:                
                place_ind_to_routes[place_ind].append(i)
        return self.get_distance(routes, place_ind_to_routes, s, t)
        
    def get_distance(self, routes, place_ind_to_routes, s, t):
        if s == t and s in place_ind_to_routes:
            return 0
        visited_routes = set([])
        visited_places = set([s])
        queue = deque([s])
        length = 0
        while queue:
            size = len(queue)
            length += 1
            for _ in range(size):
                place = queue.popleft()
                routes_this_place_belongs_to = place_ind_to_routes[place]
                for route_id in routes_this_place_belongs_to:
                    if route_id in visited_routes:
                        continue
                    for place_id in routes[route_id]:
                        if place_id == t:
                            return length
                        if place_id in visited_places:
                            continue
                        queue.append(place_id)
                        visited_places.add(place_id)
                    visited_routes.add(route_id)                

        return -1
    
    
