# import traceback
#异常处理
while True:
    try:
        print(int(input('please input')))
    except (ValueError   , TypeError  ) :
        print(v1)
    except  NameError as v1:
        print(v1)
    else:
        pass
    finally:
        print('end')
    break
        
    
