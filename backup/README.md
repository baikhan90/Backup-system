### For installing dependencies, run 
```
pip install -r requirements
```

### For running the backup system, run the following command.
`./data` is the folder where the backedup files will reside. 10s stands for the interval in which the tool which check for backing up if any of the files has changed.

```
python ./app.py --directory ./data --interval 10s        
```

For decrpyting the files from the backup, run
```
python ./encryptor.py --files './backup/a.txt' './backup/b.txt'  
```



For encrypting the files we are using [Fernet](https://cryptography.io/en/latest/fernet/) symmetric encryption. The encryption key has been saved under **private.key** file.