class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mapping = {key: value for key, value in knowledge}

        res = []
        i = 0
        n = len(s)
        
        # 2. Parse the string
        while i < n:
            if s[i] == '(':
                # Find the closing parenthesis
                j = i + 1
                while j < n and s[j] != ')':
                    j += 1
                
                # Extract the key inside the parentheses
                key = s[i+1:j]
                
                # Append the value if the key exists, otherwise append "?"
                res.append(mapping.get(key, "?"))
                
                # Move the pointer past the closing parenthesis
                i = j + 1
            else:
                # Append regular characters
                res.append(s[i])
                i += 1
                
        return "".join(res)