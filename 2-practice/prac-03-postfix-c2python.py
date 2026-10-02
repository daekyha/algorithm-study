# lec0916 - 후위표기 C => Python 

"""
[ Postfix_funct_C ]

int eval( char exp[] )
{
    int op1, op2, value, i = 0;
    intlen = strlen(exp);
    char ch;
    StackType s;

    init_stack(&s);
    for(i = 0; i < len ; i ++){
        ch = exp [i];
        if(ch != '+' && ch != '-' && ch != '*' && ch != '/'){
            value = ch - '0';     // 입력이 피연산자이면
            push(&s, value);
        }
        else{                      //연산자이면 피연산자를 스택에서 제거
            op2 = pop(&s);
            op1 = pop(&s);
            switch(ch) {           //연산을 수행하고 스택에 저장
            case '+': push(&s, op1 + op2); break;
            case '-': push(&s, op1 - op2); break;
            case '*': push(&s, op1 * op2); break;
            case '/': push(&s, op1 / op2); break;
            }
        }
    }
    return pop(&s);
}
"""

# [ Postfix_funct_py ]
class Postfixfunct:
    def eval(self, exp):
        stack = []
        #data = stack.pop()
      
        for ch in exp:
            if(ch != '+' and ch != '-' and ch != '*' and ch != '/'):
                  stack.append(int(ch))   # 입력 ch = 스트링 -> 정수형 변환 후 push.
            else:
                  op2 = stack.pop()
                  op1 = stack.pop()
                  match ch:
                      case '+':
                          stack.append(op1 + op2)
                      case '-':
                          stack.append(op1 - op2)
                      case '*':
                          stack.append(op1 * op2)
                      case '/':                
                          stack.append(op1 // op2)    ##  / => 실수형 반환, // => 정수형 반환.
        return stack.pop()

if __name__ == '__main__':
    # --------------------------------
    # Test
    # --------------------------------
    P=Postfixfunct()
    
    print("[Test 01]")
    print(f"321*+ = {P.eval("321*+")}")                # 3+2*1     => 예상 결과 = 5.
    
    print("[Test 02]")
    print(f"73-5* = {P.eval("73-5*")}")                # (7-3)*5   => 예상 결과 = 20.
    
    print("[Test 03]")
    print(f"82/3-32*+ = {P.eval("82/3-32*+")}")        # ((8/2)-3)+(3*2)   => 예상 결과 = 5.