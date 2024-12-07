# 1.リスト内の偶数だけを抽出
even = [1,2,4,7,8,11]
new_even = [num for num in even if num % 2 == 0]

# 2. 文字列のリストから文字数が５文字以上の文字列だけを抽出
strings = ["apple", "banana", "orange", "grape"]
new_strings = (str for str in strings if len(str) >= 5)
# listでリスト化、↑リストではなく、イテレータとして使う方がメモリ効率が高い
print(list(new_strings))

# 3. 二次元リスト（リストのリスト）を平坦化する
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flattened = [num for row in matrix for num in row]