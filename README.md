Using bcrypt-sha256 to hash passwords. Bcrypt by itself is considered durable with the only limitation of truncating passwords if the password goes over a certain length. Running the password through the sha256 algorithm before using bcrypt mitigates this deficiency.

In this program, passwords undergo 12 rounds of hashing. Each round increases the work factor by log2, or 2^12 which is 4096. Therefore the work factor is increased by 4096 for someone attempting a bruteforce. An attacker must compute 4096 hashes for each password tested against. Higher the rounds of hashing = more costly and timely for users and servers but generally more secure. Lower rounds of hashing = less secure but computationally cheaper. For regular hardware and software, a number between 10 and 20 is sufficient (for bcrypt atleast).

Credentials are stored in a text file in the format {*username*}:{*$type$version,rounds$salt$digest*}. In `secret.txt`, each user (`test`...`test4`) has a password of `P@ssword1!`. As you can see the hash is completely different from the next.

# **Example Outputs:**

~User logging in successfully
```
Would you like to login [1] or register [2]? 1

Username: test
Password: 

[+] Welcome test!
```

~User logging in unsuccessfully
```
Would you like to login [1] or register [2]? 1

Username: test
Password: 
[-] Invalid Username or Password
Username: 
```

~User creating an account successfully
```
Would you like to login [1] or register [2]? 2

[!] Username Must Be Between 4-10 Characters and Must Not Already Exist
Username: test5

[!] Minimum Password Requirements: 8-20 Characters, One Uppercase, One Special Character, One Number
Password: 

[+] Account Created!
```

~User creating an account unsuccessfully
```
Would you like to login [1] or register [2]? 2

[!] Username Must Be Between 4-10 Characters and Must Not Already Exist
Username: test5
[-] Username Already Exists or Your Username Does Not Meet Length Requirements
Username: 
Username: test6

[!] Minimum Password Requirements: 8-20 Characters, One Uppercase, One Special Character, One Number
Password: 
[-] Password Does Not Meet Requirements
Password: 
```

~User exceeding login attempts then being forced to quit
```
Would you like to login [1] or register [2]? 1

Username: test
Password: 
[-] Invalid Username or Password
Username: test
Password: 
[-] Invalid Username or Password
Username: test
Password: 
[-] Invalid Username or Password
Username: test
Password: 
[-] Goodbye
```

# **Installation:**

This was made with python 3.6.9 in Ubuntu 18.04 LTS

1) `cd` into a new directory and do `virtualenv env`
2) `source env/bin/activate`
3) `git clone https://github.com/n0pe13/kindof-Secure-Authentication.git`
4) `cd kindof-Secure-Authentication`
5) `pip install -r requirements.txt`
