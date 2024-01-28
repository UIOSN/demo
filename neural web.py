import numpy as np
alpha=0.01
input=np.array([8.5,0.65,1.2])
goal_pred=np.array([1,0.1,1])      
weight=np.array([[0.1,0.1,-0.3],
                [0.1,0.2,0.0],
                [0.0,1.3,0.1]]).T
deltaweight=np.zeros((3,3))
for i in range(20):
    
    pred=np.dot(input,weight)
    error=(pred-goal_pred)**2 
    print("pred:")
    print(pred)
    print("error:")
    print(error)
    
    deltaweight=np.outer(pred-goal_pred,input).T*alpha
    weight-=deltaweight
    

