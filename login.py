import  os,sys
def signup():
    userlen=20
    temp=input('Enter Username:')
    l=len(temp)
    temp=temp+((userlen-l)*'')
    temp=temp.encode()
    with open('logindoc.dat','ab+') as f:
        size=os.path.getzise('logindoc.dat')
        n=int(size/28)
        position=0
        for i in range(n):
            f.seek(position)
            str=f.read(20)
            if temp in str:
                print('username already exist')
                return
            position=position+28
    username=temp
    print('Enter password:')
    print('Password must contain One capital alphabet and one special character and must be 8 characters')
    u=0
    s=0
    a=input()
    for i in range (0,len(a)):
        if(a[i].isupper()):
            u=u+1
        elif (a[i]=='@' or a[i]=='$'):
            s=s+1
    try:
        if (u!=0 and s!=0 and len(a)<=8):
            password=a
            password=password.encode()
        else:
            raise Exception('Invalid password')
    except Exception as e:
        print('Password must contain One capital alphabet and one special character and must be 8 characters')
        exit()
    with open('logindoc.dat', 'a+b)') as f:
        f.write(username+password)

    def login():
        userlen=20
        user=input('Enter username')
        l=len(user)
        user=user+((userlen-l)*'')
        user=user.encode()
        password=input('Enter Password')
        password=password.encode()
        userinfo=user+password
        size=os.path.getsize('logindoc.dat')
        n=int(size/28)
    with open('logindoc.dat','rb') as f:
        position=0
        for i in range (n):
            f.seek(position)
            str=f.read(28)
            if userinfo in str:
                print('login successful')
                exit()
        print('username and password does not match')
        return
    while(1):
        print('1.Signup\n2.Login\nExit')
        print('Enter your choice:')
        c=int(input())
        if(c==1):
            signup()
        elif(c==2):
            login()
        elif(c==3):
            exit()
        else:
            print('Invalid choice')