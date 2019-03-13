# haveibeenpwned-query
Simple query to Have I been Pwned API.

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
