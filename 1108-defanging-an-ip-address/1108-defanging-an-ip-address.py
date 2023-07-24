class Solution:
    def defangIPaddr(self, address: str) -> str:
        self.address = address

        if '.' in address:
            return address.replace('.', '[.]')