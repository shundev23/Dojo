class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        # 入力文字列を逆順で処理
        for char in reversed(s):
            current_value = roman_to_int[char]

            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            prev_value = current_value

        return total
    
# ここからテスト関数
def test_roman_to_int():
    solution = Solution

    # テストケースと期待する結果
    test_cases = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994)
    ]

    for s, expected in test_cases:
        result = solution.romanToInt(s)
        assert result == expected, f"Test failed for input {s}: expected {expected}, got {result}"
        print(f"Test passed for input {s}: {result} == {expected}")

# メイン関数
if __name__ == "__main":
    test_roman_to_int()