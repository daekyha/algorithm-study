#lec0930 - bst 구현
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    # 0. 생성자
    def __init__(self):
        self.node = None
    
    # 1. 탐색 메서드
    def search(self, key, node = False):
        # 1.1. 기본 루트노드 지정 조건문
        if node is False:
            node = self.node
        
        # 1.2. key 일치 여부 확인 조건문    
        if (not node) or (node.key == key):
           return node
        
        # 1.3. 자식노드 이동 조건문      
        if key < node.key:
           return self.search(key, node.left)
        elif key > node.key:    
           return self.search(key, node.right)
       
        print("탐색실패")
    
    
    # 2. 삽입 메서드
    def insert(self, key, node = False):
        # 2.1. 기본 루트노드 지정 조건문
        if node is False:
            node = self.node
        
        # 2.2. 루트가 비어있을 경우 노드 생성 후 리턴.    
        if (not node):
            new_node = TreeNode(key)
            return new_node
        
        # 2.3. 자식노드 이동 조건문
        if key < node.key:
            node.left = self.insert(key, node.left) 
            return node
        
        elif key > node.key:
            node.right = self.insert(key, node.right)
            return node
        
        return

        
    # 3. 삭제 메서드
    def remove(self, key, node = False):
        # 3.1. 기본 루트노드 지정 조건문
        if node is False:
            node = self.node
        
        # 3.2. key 일치 여부 확인
        if node.key != key:                     # 1) 미일치시 -> 자식노드로 이동 
            if key < node.key:
                self.remove(key, node.left)
            elif key > node.key:
                self.remove(key, node.right)
                
        elif node.key == key:                   # 2) 일치시 -> 경우의 수 체크
            # 3.2.1. Case 1 - Leaf
            if (not node.left) and (not node.right):
                
                pass
            # 3.2.2. Case 2 - Child = 2
            elif (node.left) and (node.right):
                pass 
            # 3.2.3. Case 3 - Child = 1 
            else:
                pass

            
