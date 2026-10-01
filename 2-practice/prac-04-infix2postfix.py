# lec0916 - 연산자 ^ 오류 수정해보기 (참조:Algorithm-02-DataStructure-part1-p51)
class Infix2Postfix:
    
    # 1. 중위->후위 변환 함수
    def infix_to_postfix(self, expression):

        self.stack = []  # Reset stack
        self.output = []  # Reset output

        expression = self.tokenization(expression)               # 토큰화 과정

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
                      self.precedence(token):
                    self.output.append(self.stack.pop())
                self.stack.append(token)

        while self.stack:
            self.output.append(self.stack.pop())

        return ' '.join(self.output)

    # 2. 연산자 우선순위 반환 함수
    def precedence(self, op):
        if op in ('+','-'):
            return 1
        elif op in ('*', '/'):
            return 2
        elif op == '^':
            return 3
        return 0
    
    # 3. 토큰화 함수
    def tokenization(self, expression):
        token = []
        for ch in expression:
            token.append(ch)
        return token

    # 4. 피 구별 함수
    def is_operand(self, token):
        if(token != '+' and token != '-' and token != '*' and token != '/' and token != '^'):
            return True
        else:
            return False
        


if __name__ =='__main__':
    postfix = Infix2Postfix()
    print(postfix.infix_to_postfix("2+5*9-6+3-9/3"))