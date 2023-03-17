'''
Link: https://www.lintcode.com/problem/421/
This problem was asked in Lotusflare's 1st round technical interview on Mar 16, 2023. I wasn't able to solve 
it using the best method.
'''

# My own solution. Uses stack. I arrived at this solution after getting the hint from the interviewer.
# I originally understood this problem as a string comprehension and manipulation problem. I didn't realize that
# splitting based on '/' and getting a list of path entities can be useful. Nor did I realize this was a stack
# related problem. So I demonstrated a lack of abstraction ability in solving this problem. In the future I should
# think harder about how to construct a model to accurately abstract the problem, instead of directly working on the
# concrete low-level data.
class Solution:
    """
    @param path: the original path
    @return: the simplified path
    """
    def simplify_path(self, path: str) -> str:
        # write your code here
        path_entities = path.split('/')
        path_entities = [entity for entity in path_entities if entity != '']
        stack = ['']
        for entity in path_entities:
            if entity == ".":
                continue
            elif entity == "..": 
                if len(stack) > 1:
                    stack.pop()
            else:
                stack.append(entity)
        if len(stack) == 1:
            stack.append('')
        return '/'.join(stack)
      
      
