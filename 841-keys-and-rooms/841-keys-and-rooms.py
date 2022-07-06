class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        a = {}
        for i in range(len(rooms)):
            a[i] = rooms[i]
        
        st = []
        visited = set()
        st.append(0)
        while len(st) > 0:
            curr = st.pop()
            if curr in visited:
                continue
            visited.add(curr)
            for n in a[curr]:
                st.append(n)
        if len(rooms) == len(visited):
            return True 
        else:
            return False 