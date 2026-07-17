class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_dict = dict()
        for prereq in prerequisites:
            if prereq[0] not in prereq_dict:
                prereq_dict[prereq[0]] = [prereq[1]]
            else:
                prereq_dict[prereq[0]].append(prereq[1])
        
        safe = set()
        
        def dfs(curr_course, visiting):
            if curr_course in visiting:
                return False
            if curr_course in safe:
                return True
            if curr_course not in prereq_dict:
                return True

            for j in range(len(prereq_dict[curr_course])):
                visiting.add(curr_course)
                answer = dfs(prereq_dict[curr_course][j], visiting)
                if answer is False:
                    return False
                visiting.remove(curr_course)
            safe.add(curr_course)
            return True
        

        for i in range(numCourses):
            if not dfs(i, visiting = set()):
                return False
        return True