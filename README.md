# haveibeenpwned-query
Simple query to Have I been Pwned API.

2019-09 : ***The *Have I been pwned* account API is now covered by a $3.5/month fee and is no longer supported by this script.***  
*However, the password API is still functional at the moment.*

#### Notes
The password API query follows the secure way of querying the API, as described in [this article](https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/#cloudflareprivacyandkanonymity). Only the first 5 characters of the SHA-1 hash are sent to the query URL.

`pwned-password.py` code excerpt: 
```python
password_hash = hashlib.sha1(password.encode()).hexdigest().upper()  # password is SHA-1 hashed
password = ''  # then erased

password_hash_prefix = password_hash[:5]  # this part is sent to the query URL
password_hash_suffix = password_hash[5:]  # this part is used to lookup the hash locally in the query response content
```

#### Installation

##### Installation from release :
 - Download and extract the latest [release](https://github.com/Danamir/haveibeenpwned-query/releases). 
 - Open a terminal to the extracted directory.

##### Installation from sources :
```shell
$ curl --location https://github.com/Danamir/haveibeenpwned-query/archive/master.zip --output haveibeenpwned-query-master.zip
$ unzip haveibeenpwned-query-master.zip
$ mv haveibeenpwned-query-master/ haveibeenpwned-query
$ cd haveibeenpwned-query
```

##### Setup :
_(Optional)_ Configure Python virtual environment :
```shell
$ python -m venv .env
$ . .env/bin/activate (Linux) 
-or-
$ .env\Scripts\activate.bat (Windows)
```

Install :
```shell
$ pip install -r requirements.txt
```


#### Running

Display help :
```shell
$ python pwned-account.py --help
$ python pwned-password.py --help
```
