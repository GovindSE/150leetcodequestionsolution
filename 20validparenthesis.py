class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={')':'(' , '}':'{',']':'['}

        for char in s:

            if char in mapping:
                if stack:
                    top= stack.pop()
                else:
                    top='#'
                if top!=mapping[char]:
                    return False

            
            else:
                stack.append(char)

        return not stack
