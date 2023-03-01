class MergeSort:
    #nums is list array
    """sortArray() returns list of sorted array"""
    def sortArray(self, nums):
        return MergeSort.dfs(nums, 0 , len(nums))
    
    def dfs(nums, start:int, end:int):
        if start >= end -1:
            temp= []
            temp.append(nums[start])
            return temp
        
        mid = (start + end) // 2
        leftTree = MergeSort.dfs(nums,start, mid)
        rightTree = MergeSort.dfs(nums, mid, end)
        ptr1 = 0
        ptr2 = 0
        mergeArr = []
        mergeArrLength = len(leftTree) + len(rightTree)
        while ptr1 + ptr2 < mergeArrLength:
            if ptr1 < len(leftTree) and ptr2 < len(rightTree):
                if leftTree[ptr1] <= rightTree[ptr2]:
                    mergeArr.append(leftTree[ptr1])
                    ptr1 += 1
                else:
                    mergeArr.append(rightTree[ptr2])
                    ptr2 += 1
            elif ptr2 >= len(rightTree) and ptr1 < len(leftTree):
                mergeArr.append(leftTree[ptr1])
                ptr1 += 1
            else:
                mergeArr.append(rightTree[ptr2])
                ptr2 += 1
        return mergeArr

omergeSort = MergeSort()
input = [12,33,23,55,66,-4]
output = omergeSort.sortArray(input)
print(input)
print('after merge sort')
print(output)