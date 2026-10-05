# lec0921 - Heap 구현해보기

class Heap:
    heap=[]
    
    # 1. 최소값 반환 메소드
    def min(self):
        if self.heap:                   # 1) 힙이 비어있지 않음.
            return self.heap[0] 
        else:
            print("heap이 비어있음.")   # 2) 힙이 비어있음.
            return None
    
    # 2. 삽입 메소드
    def insert(self, data):
        self.heap.append(data)
        index = len(self.heap) - 1
        
        # 최하위에 추가된 data를 비교 후 교체하는 과정.
        while True:
            parent = (index-1) // 2
            if self.heap[parent] > self.heap[index]:            # 1) 부모 > 현재노드 => 교체
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]  
                if parent == 0:     # 1.1.) 부모 = 루트 노드인경우 => break
                    break
                else:               # 1.2.) 아니라면, index <- 부모인덱스 => 반복
                    index = parent
            else:                                               # 2) 부모 < 현재노드 => break
                break    
        return
    
    # 3. 삭제 메소드
    def remove(self):
        if len(self.heap) == 1:     # 1) 잔여 노드가 1개 - 바로 삭제, 종료
            self.heap.pop()
            return
        elif len(self.heap) == 0:   # 2) 잔여 노드가 0개 - 종료
            return
        else:                       # 3) 잔여 노드가 2개 이상 - 마지막노드 => 루트노드
            self.heap[0] = self.heap.pop()
      
        index = 0
        while True:
            left_index = 2*index + 1    
            right_index = 2*index + 2
            
            # 자식 노드 중 최소값을 가진 인덱스 찾기
            if left_index >= len(self.heap):                        # 1) 좌측 자식 노드가 범위를 벗어난 경우 - break
                break
            elif right_index < len(self.heap):                      # 2) 우측 자식 노드가 범위 안에 있는 경우 - 자식들 비교 후 최소값을 가진 인덱스 저장.
                if (self.heap[left_index] < self.heap[right_index]):
                    min_index = left_index
                else:                                               
                    min_index = right_index
            else:                                                   # 3) 좌측 = 범위 안, 우측 = 범위 밖 - 좌측 자식노드의 인덱스 저장.
                min_index = left_index
        
            # 자식노드 vs 현재노드 비교 후 교체
            if self.heap[index] > self.heap[min_index]:           
                self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
                index = min_index
            else:
                break    
            
    
    def print_heap(self):
        print(self.heap)
            
if __name__ == "__main__":
    heap = Heap()
    
    heap.min()
    
    heap.insert(2)
    heap.insert(7)
    heap.insert(52)
    heap.insert(8)
    heap.insert(13)

    heap.min()
    heap.print_heap()
    
    heap.remove()
    heap.print_heap()
    