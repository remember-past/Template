def test(A,**kwargs):
    if('name' in list(kwargs.keys())):
        print('name')
    if('name' in kwargs.keys()):
        print('name')
    print(A,kwargs.keys())

test(1,name='a',age=13)