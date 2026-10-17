import csv
def get_client():
    with open('clients.csv', 'r', encoding ='utf-8') as file:
        reader = csv.reader(file)
        result = []
        for client in reader:
            clean_client = [item.strip() for item in client]
            if not clean_client[0]:
                continue
            if clean_client not in result:
                result.append(clean_client)
        return result
names = get_client()

with open('result.csv', 'w', encoding ='utf-8', newline ='') as file:
    writer = csv.writer(file)
    
    writer.writerows(names)


