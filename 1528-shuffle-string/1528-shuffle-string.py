class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # ubah string menjadi list dulu
        list_s = list(s)

        # buat list baru berdasarkan list_s dan indices
        new_list = list(zip(list_s, indices))

        # sort list biar sesuai indices
        sort_list = sorted(new_list, key=lambda x:x[1])

        # buat list kosong untuk menyimpan list yang sudah urut dalam bentuk single list
        string_list = []

        for stri in sort_list:
            string_list.append(stri[0])

        # ubah list ke dalam bentuk str
        output = ''.join(string_list)
        return output
