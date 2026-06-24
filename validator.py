from database import get_all_records, get_conn
from detector import generate_hash, is_exact_duplicate, is_similar_duplicate
from datetime import datetime

def add_record(name, email, phone):
    hash_value = generate_hash(name, email, phone)

    # Vérification 1 : doublon exact
    if is_exact_duplicate(hash_value):
        return {
            "status": "REJECTED",
            "reason": "Doublon exact détecté",
            "data": None
        }

    # Vérification 2 : doublon similaire
    is_similar, similar_record = is_similar_duplicate(name, email)
    if is_similar:
        return {
            "status": "FALSE_POSITIVE",
            "reason": f"Entrée similaire trouvée : {similar_record[1]} / {similar_record[2]}",
            "data": None
        }

    # ✅ Données uniques → on insère
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO records (name, email, phone, hash_value, created_at)
        VALUES (%s, %s, %s, %s, %s)
    ''', (name, email, phone, hash_value, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

    return {
        "status": "ACCEPTED",
        "reason": "Donnée unique ajoutée",
        "data": {"name": name, "email": email, "phone": phone}
    }