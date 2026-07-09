class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        global_visited = set()
        
        prereq_dict = dict()
        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in prereq_dict:
                prereq_dict[prerequisites[i][0]] = prerequisites[i][1:]
            else:
                prereq_dict[prerequisites[i][0]].extend(prerequisites[i][1:])
        
        def dfs(curr_course, prereq_dict, visited):
            if curr_course in visited:
                return False
            visited.add(curr_course)
            if curr_course in global_visited:
                return True
            value = True
            if curr_course in prereq_dict:
                for i in range(len(prereq_dict[curr_course])):
                    value = dfs(prereq_dict[curr_course][i], prereq_dict, visited)
                    if value == False:
                        return value
            visited.remove(curr_course)
            global_visited.add(curr_course)
            return value
        
        for i in range(len(prerequisites)):
            if not dfs(prerequisites[i][0], prereq_dict, visited = set()):
                return False
        return True