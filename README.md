


**USAGE**



- step 1 run start.py
- step 2 upload your .py to pool folder
- step 3 make sure your .py have below code
  
```
def start(shared_dict):
  print("I can see",shared_dict)# <-- you can delete this
  
    
if __name__=='__main__':
    from os.path import basename
    from engine._mod_ import update
    update(basename(__file__),'upload') # 'upload' or 'delete'
```
- step 4 run your .py
