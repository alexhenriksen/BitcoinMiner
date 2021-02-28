from hashlib import sha256
import time
MAX_NONCE = 1000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Successfully mined bitcoins with nonce value: {nonce}")
            return new_hash
        
    raise BaseException(f"Couldn't find correct hash after trying {MAX_NONCE} time")

if __name__=='__main__':
    block_num = 1
    transactions = '''
                    Alex -> Bill -> 276,
                    Ash -> Pikachu -> 321,
                    Pikachu -> Charmander -> 430
                    '''
    last_hash = '00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048'
    difficulty = 4
    start = time.time()
    print("start mining")
    new_hash = mine(block_num, transactions, last_hash, difficulty)
    total_time = str((time.time() - start))
    print(f"end mining. mining took: {total_time} seconds")
    print(f"New Hash: {new_hash}")
