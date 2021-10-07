import hashlib
import csv

def create_hash(plain_pw):
    salted = plain_pw + "potato"
    encoded = salted.encode()
    result = hashlib.sha256(encoded)
    return result.hexdigest()

#lines = [tuple(line.strip().split(',')) for line in f.readline()]
headers = {"username" : None, "password" : None}


with open('user_db2.csv') as inf:
    reader = csv.DictReader(inf)
    rows = []
    for row in reader:
        row['password'] = create_hash(row['password'])
        rows.append(row)
    with open('new_db.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames = headers, lineterminator = '\n')
        writer.writeheader()
        writer.writerows(rows)