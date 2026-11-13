# lec 1109 - 피보나치 수열 구현
import numpy as np
import time

class Fibonacci:
    # 1. Recursive : O(2^n)
    def fib_ver1(self, n):
        if n <= 0:
            return 0
        if (n == 1) or (n==2):
            return 1
        return self.fib_ver1(n-1) + self.fib_ver1(n-2)
   
    # 2. Divide & Conquer (Recursive) : O(log n)
    def fib_ver2(self,n):
        if n <= 0:
            return 0
        if n==1 or n==2:
            return 1
        
        X = [[1,1], [1,0]]      # 초기 배열 [[F2, F1], [F1, F0]]
        Y = self.matrix_Power(X, n-1)
        return Y[0][0]
    
    def matrix_Multiply(self, A, B):
        res = np.matmul(np.array(A), np.array(B))
        return res.tolist()
    def matrix_Power(self, A, n):
        if n>1:
            A = self.matrix_Power(A, n//2)
            A = self.matrix_Multiply(A,A)
            
            if n % 2:
                B = [[1,1],[1,0]]
                A = self.matrix_Multiply(A, B)
        return A        
        
    # 3. Dynamic Programming (Bottom-up, Iterative) : O(n)
    def fib_ver3(self, n):
       if(n <= 1):
           return n
       
       fib_table = [0] * (n+1) 
       fib_table[1] = 1
       
       for i in range(2, n+1):
           fib_table[i] = fib_table[i-1] + fib_table[i-2]
       
       return fib_table [n]
   
    # 4. Dynamic Programming (Top-down, Recursive) : O(n)
    def fib_ver4(self, n, memo = [0,1] + [-1]*100):
        if n<=1:
             return n
        if memo[n] != -1:
            return memo[n]
        
        memo[n] = self.fib_ver4(n-1, memo) + self.fib_ver4(n-2, memo)
        return memo[n]

if __name__ == '__main__':
    Fib = Fibonacci()
    
    print("[1] FIB Recursive - O(2^n)")
    start_time = time.time()
    result = Fib.fib_ver1(40)
    end_time = time.time()
    print(f"result:{result}, time:{(end_time-start_time)} sec")
   
    print("[2] FIB Divide & Conquer (Recursive) : O(log n)")
    start_time = time.time()
    result = Fib.fib_ver2(40)
    end_time = time.time()
    print(f"result:{result}, time:{end_time-start_time} sec")
    
    print("[3] FIB Dynamic Programming (Bottom-up, Iterative) : O(n)")
    start_time = time.time()
    result = Fib.fib_ver3(40)
    end_time = time.time()
    print(f"result:{result}, time:{end_time-start_time} sec")
    
    print("[4] Dynamic Programming (Top-down, Recursive) : O(n)")
    start_time = time.time()
    result = Fib.fib_ver4(40)
    end_time = time.time()
    print(f"result:{result}, time:{end_time-start_time} sec")