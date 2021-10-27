'''
Link: https://www.lintcode.com/problem/613/
'''

'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''

# My own solution. Uses heap to keep track of the lowest score among the top five. Time complexity should be O(nlogm),
# where n is the total number of Record objects, m is the maximum number of records for each student.
import heapq
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        id_to_top_scores = dict()
        size_limit = 5
        id_to_avg = dict()
        for record in results:
            if record.id not in id_to_top_scores:
                id_to_top_scores[record.id] = []
            if len(id_to_top_scores[record.id]) < size_limit:
                heapq.heappush(id_to_top_scores[record.id], record.score)
            elif record.score > id_to_top_scores[record.id][0]:
                heapq.heappushpop(id_to_top_scores[record.id], record.score)
        for id, top_scores in id_to_top_scores.items():
            avg = sum(top_scores) / len(top_scores)
            id_to_avg[id] = avg
        return id_to_avg
  
