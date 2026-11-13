# lec 1109 - LCS 구현

class LCS():
    # 0. 생성자 - LCS 테이블 구성
    def __init__(self, Str1, Str2):   # 기본 입력 : String X, Y
        self.Str1 = Str1
        self.Str2 = Str2
        self.m = len(Str1)
        self.n = len(Str2)
        self.table = [[None] * (self.n + 1) for i in range(self.m + 1)]
        
        for i  in range(self.m + 1):
            for j in range(self.n + 1):
                if i==0 or j==0:
                    self.table[i][j] = 0
                elif Str1[i-1] == Str2[j-1]:
                    self.table[i][j] = self.table[i-1][j-1] +1
                else:
                    self.table[i][j] = max(self.table[i-1][j], self.table[i][j-1])
    
    # 1. LCS - 왼쪽/위쪽 동일 시 <왼쪽> 이동
    def find_LCS(self):
        index = self.table[self.m][self.n]      # 테이블의 마지막(우측하단) => LCS 길이
        result = [""] * index                   # 길이만큼 배열 생성.
        
        i = self.m
        j = self.n

        while i > 0 and j > 0:
            if(self.Str1[i-1] == self.Str2[j -1]):          # 1. 두 문자가 같은경우  => 대각선 이동
                result[index-1] = self.Str1[i-1]
                i -= 1 
                j -= 1
                index -= 1
            elif(self.table[i-1][j] > self.table[i][j-1]):  # 2. 두 문자가 다른경우 - (위쪽 > 왼쪽)  => 위쪽으로 이동
                i -= 1
            else:                                           # 3. 위쪽, 왼쪽 동일한 경우 + [2] (위쪽 < 왼쪽)인 경우 => 왼쪽으로 이동 
                j -= 1
                
        return ''.join(result)
    
    # 2. LCS - 왼쪽/위쪽 동일 시 <위쪽> 이동
    def find_LCS_ver2(self):
        index = self.table[self.m][self.n]      # 테이블의 마지막(우측하단) => LCS 길이
        result = [""] * index                   # 길이만큼 배열 생성.
        
        i = self.m
        j = self.n

        while i > 0 and j > 0:
            if(self.Str1[i-1] == self.Str2[j -1]):          # 1. 두 문자가 같은경우  => 대각선 이동
                result[index - 1] = self.Str1[i-1]
                i -= 1 
                j -= 1
                index -= 1
            elif(self.table[i-1][j] < self.table[i][j-1]):  # 2. # 2. 두 문자가 다른경우 - (위쪽 < 왼쪽)  => 왼쪽으로 이동
                j -= 1
            else:                                           # 3. 위쪽, 왼쪽 동일한 경우 + [2] (위쪽 > 왼쪽)인 경우 => 위쪽으로 이동 
                i -= 1
                
        return ''.join(result)
    
    # 3. LCS 길이 반환
    def len(self):
        return self.table[self.m][self.n]
    
    

if __name__ == '__main__':
    lcs = LCS("GOOD MORNING", "GUTEN MORGEN")
    print("[입력] \"GOOD MORNING\", \"GUTEN MORGEN\"")
    print("[1]",lcs.find_LCS())
    print("[2]",lcs.find_LCS_ver2())
    print("[길이]", lcs.len())
    
                 
                
            
                