class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            if ty > tx:
                ty %= tx
            else:
                tx %= ty
        if tx == sx and ty == sy:
            return True
        elif tx == sx:
            return True if ty > sy and not (ty-sy) % sx else False
        elif ty == sy:
            return True if tx > sx and not (tx-sx) % sy else False
        else:
            return False