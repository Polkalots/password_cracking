import hashlib
import argparse

def main(file='', hash='', wordlist=''):
    words_to_hashes = hash_wordlist(wordlist)
    for word in words_to_hashes:
        print(word)
    # if file:
    #     print(hash_wordlist(file, wordlist))
    # if hash:
    #     print(hash_wordlist(wordlist))


def hash_wordlist(file):
    hashes = []
    with open(file, 'r') as wordlist:
        for word in wordlist:
            word = word.strip()
            h = hashlib.md5(word.encode()).hexdigest()
            hashes.append({h: word})
    return hashes


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Crack MD5 password hashes using a wordlist')
    parser.add_argument('-f', '--file', help='Text file that contains hashes to be cracked')
    parser.add_argument('-hs', '--hash', help='Single MD5 hash to be cracked')
    parser.add_argument('-w', '--wordlist', help='Dictionary wordlist to compare against')
    args = parser.parse_args()

    main(args.file, args.hash, args.wordlist)