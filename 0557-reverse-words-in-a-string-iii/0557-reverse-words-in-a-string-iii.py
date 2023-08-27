class Solution:
    def reverseWords(self, s: str) -> str:
        split_s = s.split(" ")
        result_sementara = []
        for word in split_s:
            reverse_word = word[::-1]
            result_sementara.append(reverse_word)

            # change result to string
            real_result = ' '.join(result_sementara)

        return real_result

           