class Solution:
    def countSeniors(self, details: List[str]) -> int:
        new_list = []
        output = 0
        
        for det in details:
            detail = det[10:13]
            new_list.append(detail)
        number_list = []
        
        for new in new_list:
            num = new[1:]
            number_list.append(num)
            
        new_number_list = []
        new_number_list = list(map(int, number_list))
        for num in new_number_list:
            if num > 60:
                output += 1
            else:
                output += 0

        return output
                

