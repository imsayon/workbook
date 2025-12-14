import shelve, pprint

def count_and_store(filename):
    try:
        with open(filename, 'r') as f:
            words = f.read().lower().split()
        
        counts = {w: words.count(w) for w in set(words)} # Count frequencies
        
        # Store in shelve
        with shelve.open("word_db") as db:
            db['counts'] = counts
            print("Stored in shelve."); pprint.pprint(counts)
            
    except FileNotFoundError: print("File not found")

count_and_store("word_count.txt")