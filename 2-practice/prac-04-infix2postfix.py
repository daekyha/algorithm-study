# lec0916 - 연산자 '^' 오류 수정해보기 (참조:Algorithm-02-DataStructure-part1-p51)

class Infix2Postfix:
    
    # 1. 중위->후위 변환 메서드
    def infix_to_postfix(self, expression):

        self.stack = []  # Reset stack
        self.output = []  # Reset output

        expression = self.tokenization(expression)               # 토큰화 과정.

        for token in expression:                    
            if self.is_operand(token):                           # 1) 피연산자인 경우  
                self.output.append(token)
                
            elif token == '(':                                   # 2) 여는괄호인 경우
                self.stack.append(token)
                
            elif token == ')':                                   # 3) 닫는괄호인 경우    
                while self.stack and self.stack[-1] != '(':
                    self.output.append(self.stack.pop())
                self.stack.pop()  # pop '('
                
            else:                                                # 4) 연산자인 경우
                while self.stack and \
                      self.precedence(self.stack[-1]) >= \
                      self.precedence(token):                    ## \ 뜻 = 다음줄에 이어짐. 
                                                                 ## 조건 = 스택이 비어있지 않고, [스택 마지막]의 우선순위가 [토큰]보다 크거나 같을때.
                    if (self.stack[-1] == '^') and (token == '^'):       # 4.1.) [스택 마지막]=[토큰]='^'인 경우
                        break
                    else:                                                # 4.2.) 그 외 경우
                        self.output.append(self.stack.pop())

                self.stack.append(token)

        while self.stack:                                        # 스택에 남아있는 것 => output으로 이동.
            self.output.append(self.stack.pop())

        return ' '.join(self.output)

    # 2. 연산자 우선순위 반환 메서드
    def precedence(self, op):
        if op in ('+','-'):
            return 1
        elif op in ('*', '/'):
            return 2
        elif op == '^':
            return 3
        return 0
    
    # 3. 토큰화 메서드
    def tokenization(self, expression):
        num = []
        token = []
        
        for ch in expression:
            if ch in ('+', '-', '*', '/', '^', ')'):        # 1) 토큰이 연산자인경우
                if num:                                     ## 리스트(num)에 담아둔 숫자를 합친 후 초기화 -> token에 추가.
                    token.append(''.join(num))
                    num=[]             
                token.append(ch)
                
            elif ch == '(':                                 # 2) 토큰이 '(' 일 경우.
                token.append(ch)                            ## "+3 ( ~"은 불가능. => 바로 토큰에 추가.
                                                            ## "+3 ) ~" 인 경우는 존재함. => 1)에서 숫자 처리 후 토큰 추가.
                          
            else:                                           # 3) 토큰이 피연산자인 경우
                num.append(ch)                              ## 숫자를 리스트(num)에 담아둠.
                
        if num:
            token.append(''.join(num))
               
        return token

    # 4. 피연산자 구별 메서드
    def is_operand(self, token):
        if token not in('+', '-', '*', '/', '^', '(', ')'):
            return True
        else:
            return False
        

if __name__ =='__main__':
    postfix = Infix2Postfix()
    print("[Test1] 2+5*9-6+3-9/3 =>", postfix.infix_to_postfix("2+5*9-6+3-9/3"))     # 2 5 9 * + 6 - 3 + 9 3 / -
    print("[Test2] 2^3^2 =>", postfix.infix_to_postfix("2^3^2"))                     # 2 3 2 ^ ^
    print("[Test3](1+2)^3*4 =>", postfix.infix_to_postfix("(1+2)^3*4"))              # 1 2 + 3 ^ 4 *