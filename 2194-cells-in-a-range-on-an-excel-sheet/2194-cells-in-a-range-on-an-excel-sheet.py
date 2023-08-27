class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        output = []
        list_string = []
        list_number = []
        # number
        number = re.findall(r'\d+', s)
        number_only = list(map(int, number))

        # rewrite the number list
        start_number = number_only[0]
        end_number = number_only[1]

        for num in range(start_number, end_number + 1):
            list_number.append(num)

        # character
        character = re.findall(r'[a-zA-Z]', s)
        character_only = list(map(str, character))

        # rewrite the list
        start_char = ord(character_only[0])
        end_char = ord(character_only[1])

        for ord_val in range(start_char, end_char + 1):
            list_string.append(chr(ord_val))

        for char in list_string:
            for num in list_number:
                output.append(char + str(num))

        unique_output = list(set(output))
        unique_output.sort()

        return unique_output


            