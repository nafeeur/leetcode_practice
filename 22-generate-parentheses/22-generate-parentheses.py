class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        #well formed paranthesis = () (()) but not ((() 
        
        #Understanding: max 16 paranthesis - min 2 paranthesis
        #Plan : if empty append open then append open or close
        # Keep track of closing and opening paranthesis
       
    #["((()))","(()())","(())()","()(())","()()()"]
    
             #(
         #((          ()
    #(()      (((      ()( 
#(()(  (()()    ((()      ()((  ()()

#When c == o append o
#When o>c and o == n append c
#When o>c and o < n append o or append c

        parenthesis = ""
        output = []
        o = "("
        c = ")"
        numOpen = 0
        numClose = 0
        
        def recurParenthesis(numOpen, numClose, parenthesis):
            if numOpen == n and numClose == n:
                output.append(parenthesis)
            else:
                if numOpen == numClose:
                    recurParenthesis(numOpen+1, numClose, parenthesis+o)
                elif numOpen > numClose and numOpen == n:
                    recurParenthesis(numOpen, numClose+1, parenthesis+c)
                elif numOpen > numClose and numOpen < n:
                    recurParenthesis(numOpen+1, numClose, parenthesis+o)
                    recurParenthesis(numOpen, numClose+1, parenthesis+c)
        recurParenthesis(numOpen, numClose, parenthesis)
        return output
               
                
            
            
