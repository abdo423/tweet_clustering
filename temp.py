import random as rd
# import matplotlib.pyplot as plt


def Cleaning (F):

 raws = []
 file = open (F,"r" )
 file = open (F,"r",encoding=('utf-8') )
 for i in file:
     A = i.replace("\n","")
     raws.append(A.lower())
 file.close()
 file.close()
 
 list = []
 for q in raws:
     brid = q.split('|')
     tweet = brid[2]
     new = ""
     checking = 0
     
     for i in range(len(tweet)):
    
         if len(tweet)-i>=4:
             s=tweet[i]+tweet[i+1]+tweet[i+2]+tweet[i+3]
    
         else:
             s=""
    
         if (s=="http" or tweet[i]=='@') and (tweet[i-1]==" " or i == 0 ) :
             checking=1
    
         if checking==0 and tweet[i]!='#':
             new += (tweet[i])
    
         if tweet[i]==' ':
             checking=0
    
     list.append(new)
 return list

def jacard(tweett1,tweett2,frame):
    
    tweet1 = frame[tweett1]
    tweet2 = frame[tweett2]
    newtweet1 = tweet1.replace(" ", "")
    newtweet2 = tweet2.replace(" ", "")

    intersec = set(newtweet1).intersection(set(newtweet2))
    unio = set(newtweet1).union(set(newtweet2))
    Result = 1- (len(intersec)/len(unio))
    
    return Result

def First_time(frame,boool):
    clusterList=[]
    
    if(boool =="y" or boool =="Y"):
        l = int(input("enter the number of clusters: ")) 
        if (l == 0):
            print("\n","Disallowed Value")
            return
        else:
            for c in range(0,l):
                #random number
                A = rd.randint(0,len(frame))
                cluster = [A,]
                #compare betwwen the random number and other tweets
                for B in range(0,len(frame)):
                    z = jacard(A,B,frame)
                    print (z)
                    if(z == 0):
                        o = 1
                    elif (z == 1):
                        o = 0
                    elif (z <= 0.5):
                        o = 1
                    elif (z > 0.5):
                        o = 0
                        
                    if (o == 1):
                        cluster.append(B)
                        
                clusterList.append(cluster)
        NEW_CLUSTER_LIST = compare(clusterList,frame)        
        return NEW_CLUSTER_LIST          
    else:
        for c in range(0,3):
            #random number
            A = rd.randint(0,len(frame))
            cluster = [A,]
            #compare betwwen the random number and other tweets
            for B in range(0,len(frame)):
                z = jacard(A,B,frame)
                if(z == 0):
                    o = 1
                elif (z == 1):
                    o = 0
                elif (z < 0.5 or z == 0.5):
                    o = 1
                elif (z > 0.5):
                    o = 0
                if (o == 1):
                    cluster.append(B)
            clusterList.append(cluster)
        NEW_CLUSTER_LIST = compare(clusterList,frame)
        return NEW_CLUSTER_LIST

def compare (data,frame):
    
    for j in range(0,len(data)):
        for g in range(0,len(data)):
            if (j != g):
                intersec = set(data[j]).intersection(set(data[g]))
                for i in intersec:
                    first = jacard(data[j][0],i,frame)
                    second = jacard(data[g][0],i,frame)
                    if(first == second):
                        data[g].remove(i)
                    elif(first < second):
                        data[g].remove(i)
                    elif(second < first):
                        data[j].remove(i)
    return data
    
def many_times(frame):
    ttmp =[]
    number = []
    boool = input("Do you want to mention the number of clusters?(y/n): ")
    data = First_time(frame,boool)
    exp = input("Do you want to mention the number of experiments?(y/n): ")
    SSEE = []
    if(exp == "y" or exp == "Y"):
        n = int(input("enter the number of expre: "))
        x = data
        for p in range(0,len(data)):
            number.append(len(data[p]))
        print("\n","the size of clusters(data) is: ",number)
        SSEE= com_sse(data,frame)
        ttmp.append(sum (SSEE))
        print("\n","the Number of SSE for (data) cluster is: ",SSEE)
        if(n==0):
            print("\n","Disallowed Value")
            return
        
        else:
            
            for q in range(n-1):
                number = []
                x = update_cen(x,frame)
                for ff in range(0,len(x)):
                    number.append(len(x[ff]))
                print("\n","the size of clusters is: ",number)
                SSEE=com_sse(x,frame)
                ttmp.append(sum (SSEE))
                print("\n","the Number of SSE for each cluster is: ",SSEE)
            
            # pplot = input("Do you want to show elbow plot(y/n): ")
            # if(pplot == "y" or pplot=="Y"):
                
            #     elbow_plotting(ttmp)
            # elif(pplot=="n" or pplot=="N"):
            #     return
                
                
                
                
    else:
        x = data
        for p in range(0,len(data)):
            number.append(len(data[p]))
        print("\n","the size of clusters(data) is: ",number)
        SSEE = com_sse(data,frame)
        print("\n","the Number of SSE for (data) cluster is: ",SSEE)
        
        for ww in range(4):
            number = []
            x = update_cen(x,frame)
           
            for ff in range(0,len(x)):
                number.append(len(x[ff]))
            print("\n","the size of clusters is: ",number)
            SSEE=com_sse(x,frame)
            ttmp.append(sum (SSEE))
            print("\n","the Number of SSE for each cluster is: ",SSEE)
        
        # pplot = input("Do you want to show elbow plot(y/n): ")
        # if(pplot == "y" or pplot=="Y"):
            
        #     elbow_plotting(ttmp)
        # elif(pplot=="n" or pplot=="N"):
        #     return
     
        
     
def update_cen (new_data,frame):
    
    new_cen = []
    new_cluster = []
    
    for z in range(0,len(new_data)):
         store = new_data[z]
         Sum = []
         
         for one in range(0,len(store)) :
              
              seeeeeeeeee = 0
              for two in range(0,len(store)):
                  if(one != two):
                      seeeeeeeeee = seeeeeeeeee + jacard(store[one],store[two],frame) 
              Sum.append(seeeeeeeeee)
         minimum = min(Sum)
         for x in range(len(Sum)):
             
              if(Sum[x] == minimum):
                  new_cen.append(store[x])
                  break

    for q in new_cen:
        cluster = [q,]
        for j in range(0,len(frame)):
            z = jacard(q,j,frame)
            print(z)
            if(z == 0):
                o = 1
            elif (z == 1):
                o = 0
            elif (z <= 0.5):
                o = 1
            elif(z > 0.5):
                o = 0
            if (o == 1):
                cluster.append(j)
        new_cluster.append(cluster)
    GG = compare(new_cluster,frame)
    return GG

def com_sse (data,frame):
    sum_sse = []
    for t in range(len(data)):
        ss = 0
        clus = data[t]
        centro = data[t][0]
        for tt in range(len(clus)):
            ss = ss + (( jacard(centro,clus[tt],frame) )**2)
        sum_sse.append(ss)
    return sum_sse
     
# def elbow_plotting (SSEE):
    
#     x = range(1 , len(SSEE)+1)
  
    
#     y = SSEE
        
#     plt.plot(x,y)
#     plt.xlabel('number of K')
#     plt.ylabel('SSE')
#     plt.title('Elbow Method')
#     #plt.ylim(1,8)
#     plt.xlim(1,len(SSEE))
#     plt.show()
    
    
        

#Main
FFile = r'C:\Users\abdel\.spyder-py3\Health-Tweets\\' + input("enter the File name: ") + ".txt"
frame = Cleaning(FFile)
many_times(frame)
