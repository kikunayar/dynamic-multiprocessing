







def start(shared_dict):
    print("TEST",shared_dict)



if __name__=='__main__':
    import os
    from engine._mod_ import update
    update(os.path.basename(__file__),'upload')