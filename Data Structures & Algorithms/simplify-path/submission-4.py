class Solution:
    def simplifyPath(self, path: str) -> str:
        curr_dir = ""
        stack = []
        directory_name_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_."
        for i in range(len(path)):
            if path[i] in directory_name_letters:
                curr_dir += path[i]
            else:
                if curr_dir != "":
                    if curr_dir[-1] != ".":
                        stack.append(curr_dir)
                        curr_dir = ""
                    else:
                        if curr_dir == ".":
                            curr_dir = ""
                        elif curr_dir == "..":
                            if stack:
                                stack.pop()
                            curr_dir = ""
                        else:
                            stack.append(curr_dir)
                            curr_dir = ""
                if path[i] == "/":
                    continue
        if curr_dir:
            if curr_dir == ".":
                pass
            elif curr_dir == "..":
                stack.pop()
            else:
                stack.append(curr_dir)

        directory = "/" + "/".join(stack)
        return directory