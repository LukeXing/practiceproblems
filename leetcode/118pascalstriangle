class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        i = 4 
        List = [[1]]
        List2 = [[1,1]]
        List3 = [[1,2,1]]
        Total_List = List+List2+List3
        Blanklist = [[1]]
        
        if numRows == 1:
            return List
        elif numRows == 2:
            return List+List2
        elif numRows == 3:
            return Total_List
        else:
            #while loop to support below numRows
            while i <= numRows:
                print(i, "i")
                #reset prev element
                prev_element = 0
                
                for j in List3[0]:
                    
                    if prev_element == 0:
                        prev_element = j
                    
                    else:
                        Blanklist[0].append(j+prev_element)
                        prev_element = j
                
                #adds the ending 1
                Blanklist[0].append(1)
                Total_List += Blanklist
                List3 = Blanklist
                i+=1
                Blanklist = [[1]]
                    
            return Total_List
                    
