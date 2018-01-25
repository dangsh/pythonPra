from time import ctime , sleep
import threading

def music(func):
    for i in range(2):
        print("i was listening to music %s.... %s" % (func , ctime()));
        sleep(1);

def move(func):
    for i in range(2):
        print("i was at the movies %s!.....  %s" % (func , ctime()));
        sleep(5)


threads = []

t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)

t2 = threading.Thread(target=move , args=(u"功夫" , ));
threads.append(t2);





if __name__ == "__main__":
   


    for t in threads:
        t.start()
 
    for t in threads:
        t.join()
 
    print ("all over %s" %ctime())


