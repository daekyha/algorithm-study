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
class Postfixfunct:
    def eval(self, exp):
      stack = []
      #data = stack.pop()
      
      for ch in exp:
          if(ch != '+' and ch != '-' and ch != '*' and ch != '/'):
                stack.push(ch)
          else:
                op2 = stack.pop()
                op2 = stack.pop()
                case 
          print(ch)

if __name__ == '__main__':
    # --------------------------------
    # Test
    # --------------------------------
    P=Postfixfunct()
    P.eval("3+2*1")