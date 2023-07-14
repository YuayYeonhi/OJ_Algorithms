class Solution:
    #判断皇后是否符合条件
    def isValid(self, pos: List[int], row:int, col:int):
        # row为当前要放置皇后的行，col当前要摆放皇后的位置
        # 遍历之前所有行，皇后的所在位置
        for i in range(row):
            #不能同行同列同一斜线
            # 不能同列：col == pos[i] 判断当前位置，与之前行位置的皇后是否在同一位置
            # 不能同对角线：abs(row - i) == abs(col - pos[i]) 判断当前位置是否与之前的皇后在同一对角线上
            if col == pos[i]&nbs***bsp;abs(row - i) == abs(col - pos[i]):
                return False
        return True
     
    #递归查找皇后种类
    def recursion(self, n:int, row:int, pos:List[int], res:int):
        #完成全部行都选择了位置
        if row == n:
            res += 1
            return int(res)
        # 每行遍历所有可能
        for i in range(n):
            #检查该位置是否符合条件
            if self.isValid(pos, row, i): 
                #加入位置
                pos[row] = i
                #递归继续查找
                res = self.recursion(n, row + 1, pos, res)
        return res
 
    def Nqueen(self , n: int) -> int:
        res = 0
        # pos[i],i为第几行，pos[i]表示第i行的皇后放的位置，pos[3] = 7 第4行的皇后在第7位置
        pos = [0] * n
        # 递归
        result = self.recursion(n, 0, pos, res)
        return result