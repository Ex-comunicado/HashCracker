from os import read, system
import sys, getopt, hashlib, time

def banner():
    system("figlet -f slant HashCracker")
    print("Developed by: Ex-Communicado")

def info():
    banner()
    print("Usage: python hashcracker.py [OPTIONS]")
    print("Help Menu:")
    print("   -h, --help; Display this menu.")
    print("   -a, --algos; Hashing algorithms supported.")
    print("   -t, --type; Type of Hash.")
    print("   -f, --file; Specify file containing hash.")
    print("   -w, --wordlist; Specify a file to compare hash file against.")

def crack_hash(hashtype, hash, wordlist):
    line = 0
    found = False
    try:
        with open(wordlist, "r") as passlist:
            start = time.time()
            for w in passlist:
                if hashtype == 'md5':
                    hashed = hashlib.md5(bytes(w.strip(), 'utf-8')).hexdigest()
                elif hashtype == 'sha1':
                    hashed = hashlib.sha1(bytes(w.strip(), 'utf-8')).hexdigest()
                elif hashtype == 'sha224':
                    hashed = hashlib.sha224(bytes(w.strip(), 'utf-8')).hexdigest()
                elif hashtype == 'sha256':
                    hashed = hashlib.sha256(bytes(w.strip(), 'utf-8')).hexdigest()
                elif hashtype == 'sha384':
                    hashed = hashlib.sha384(bytes(w.strip(), 'utf-8')).hexdigest()
                elif hashtype == 'sha512':
                    hashed = hashlib.sha512(bytes(w.strip(), 'utf-8')).hexdigest()
                else:
                    print("[!] This type of hash is not supported.")
                    print("[!] Hashes supported are: MD5, SHA1, SHA224, SHA256, SHA384 , SHA512")
                                                                                                                   
                if hashed == hash:                                                                                 
                    if found == False:                                                                             
                        end = time.time()                                                                          
                        print(" > %s matched.\n" % (w.strip()))
                        print("[*] Hash Found!")
                        print("[*] The decrypted hash is: %s" % w.strip())
                        print("[*] Number of words checked: %s" % (int(line)+1))
                        print("[*] Time Taken: %s seconds" % round((end - start),5))
                    found = True
                elif hashed != hash:
                    if found == False:
                        print(" > %s does not match, trying next." % (w.strip()))
                    line+=1
            end = time.time()
            if found == False:
                print("\n[-] Hash not found.")
                print("[*] Number of words checked: %s" % line)
                print("[*] Time Taken: %s seconds" % round((end - start), 5))
    except FileNotFoundError:
        print("[!] Could not find wordlist file. Try again.")
        info()

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hat:f:w:", ["help", "algos", "type=", "file=", "wordlist="])
    except getopt.GetoptError:
        print("\nInvalid command.")
        info()
        sys.exit()
    for opt, arg in opts:
        if opt in ['-h','--help']:
            info()
            exit()
        elif opt in ['-a', '--algos']:
            print("Hashes supported are: MD5, SHA1, SHA224, SHA256, SHA384 and SHA512.")
            exit()
        elif opt in ['-t', '--type']:
            hashtype=arg.lower()
        elif opt in ['-f', '-file']:
            hashFile = arg
        elif opt in ['-w', '--wordlist']:
            wordlist = arg
    try:
        file = open(hashFile,"r")
        hash = file.readline()
        hash = hash.strip()
    except FileNotFoundError:
        print("[!] Could not find hash file. Try again.")
        info()
    banner()
    print("\n[*] Type of Hash: %s" % hashtype.upper())
    print("[*] Hash: %s" % hash)
    print("[*] Wordlist: %s" % wordlist)
    print("[+] Working...\n")
    try:
        crack_hash(hashtype, hash, wordlist)
    except UnboundLocalError:
        pass

if __name__ == "__main__":
    main(sys.argv[1:])
