import hashlib
import argparse

def main(hash_file='', single_hash='', wordlist=''):
    words_to_hashes = hash_wordlist(wordlist)
    if hash_file:
        passwords = {}
        hashes = get_hashes(hash_file)
        for hash in hashes:
            for entry in words_to_hashes:
                for key, value in entry.items():
                    if hash == key:
                        passwords.update({hash: value})
        for entry in passwords:
            print(f'{entry}: {passwords[entry]}')
        # print(hashes)

    elif single_hash:
        for entry in words_to_hashes:
            for key, value in entry.items():
                if single_hash == key:
                    password = value
                    print(password)

# Returns a list of dictionaries with the hashes and each associated word in the wordlist
def hash_wordlist(wordlist):
    hashes = []
    with open(wordlist, 'r') as w:
        for word in w:
            word = word.strip()
            h = hashlib.md5(word.encode()).hexdigest()
            hashes.append({h: word})
    return hashes

# Returns the hashes to be cracked in a list object
def get_hashes(hash_file):
    hashes = []
    with open(hash_file, 'r') as f:
        for hash in f:
            hashes.append(hash.strip())
    return hashes


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Crack MD5 password hashes using a wordlist')
    parser.add_argument('-hf', '--hash_file', help='Text file that contains hashes to be cracked')
    parser.add_argument('-sh', '--single_hash', help='Single MD5 hash to be cracked')
    parser.add_argument('-w', '--wordlist', help='Dictionary wordlist to compare against')
    args = parser.parse_args()

    main(args.hash_file, args.single_hash, args.wordlist)

    # get_hashes(args.file)