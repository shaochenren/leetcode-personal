#recursive way to solve 
#lint code 366
#1递归的定义 ， 函数要接受什么样的参数没返回什么样的值，代表什么样的意思
def bibnoacci(int a){
    #3递归的出口
    if (n<=2){
        return n-1
    }
    #2递归的拆解
    return fibnocci(n-1) + fibonacci(n-2)
}