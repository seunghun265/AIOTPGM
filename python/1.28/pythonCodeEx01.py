import re

# 휴대폰 & 지역번호 정규표현식
pattern = r"^(?:01[016789])-\d{3,4}-\d{4}$"

def is_valid_phone(num):
    return bool(re.match(pattern, num))

test_numbers = [
    "010-1234-5678",
    "011-234-5678",
    "02-123-4567",
    "031-1234-5678",
    "032-456-7890",
    "019-12-3456",      # ❌
    "01012345678",      # ❌
    "03-1234-5678",     # ❌ (03은 유효한 지역번호가 아님)
]

for num in test_numbers:
    print(num, "→", is_valid_phone(num))