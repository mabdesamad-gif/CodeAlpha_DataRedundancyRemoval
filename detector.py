import hashlib
from database import get_all_records

def generate_hash(name, email, phone):
    data = f"{name.lower().strip()}{email.lower().strip()}{phone.strip()}"
    return hashlib.md5(data.encode()).hexdigest()

def is_exact_duplicate(hash_value):
    records = get_all_records()
    for record in records:
        if record[4] == hash_value:  # colonne hash_value
            return True
    return False

def similarity_score(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    matches = sum(c1 == c2 for c1, c2 in zip(str1, str2))
    return matches / max(len(str1), len(str2))

def is_similar_duplicate(name, email):
    records = get_all_records()
    for record in records:
        name_score = similarity_score(name, record[1])
        email_score = similarity_score(email, record[2])
        if name_score > 0.85 or email_score > 0.95:
            return True, record
    return False, None

if __name__ == "__main__":
    hash_test = generate_hash("Alice", "alice@mail.com", "0600000000")
    print("🔑 Hash généré :", hash_test)
    print("🔍 Doublon exact ?", is_exact_duplicate(hash_test))