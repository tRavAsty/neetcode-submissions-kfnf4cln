class Solution:

    def encode(self, strs: List[str]) -> str:
        return "_".join([f"^{s}$" for s in strs ])


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = s.split("$_^")
        if res:
            res[0]=res[0][1:]
            res[-1] = res[-1][:-1]
        return res
