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
    def search(self, key, node = None):
        # 1.1. 기본 루트노드 지정 조건문
        if node == None:
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
    def insert(self, key, node = None):
        # 2.1. 기본 루트노드 지정 조건문
        if node == None:
            node = self.node
        
        # 2.2. 루트가 비어있을 경우 삽입    
        if (not node):
            node = TreeNode(key)
            return node
        
        # 2.3. 자식노드 이동 조건문
        if key < node.key:
            return self.insert(key, node.left)
        elif key > node.key:
            return self.insert(key, node.right)
        
        print("삽입실패")

        
    # 3. 삭제 메서드
    def remove(self, key, node = None):
        # 3.1. 기본 루트노드 지정 조건문
        if node == None:
            node = self.node
        # 3.2. 
        # 3.2.1. Case 1 - Leaf
        if (not node.left) and (not node.right):
            pass
        # 3.2.2. Case 2 - Child = 1
        # 3.2.3. Case 3 - Child = 2 
