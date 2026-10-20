class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        i=0
        if strs == []:
            encoded_string = "[]"
        elif strs == [""]:
            encoded_string = ""
        else:
            while i<(len(strs)):
                if i != (len(strs)-1):
                    strs[i]=strs[i]+"''"
                encoded_string=encoded_string+strs[i]
                i=i+1
        return encoded_string;

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            decoded_strs=[]
        elif s == "":
             decoded_strs = [""]
        else:
            decoded_strs = s.split("''")
        return decoded_strs;