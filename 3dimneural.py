import numpy as np
streetlights=np.array([[1,0,1],
                       [0,1,1],
                       [0,0,1],
                       [1,1,1]])
walkstop=np.array([1,1,0,0]).T
alpha=0.2
hidden_size=4
np.random.seed(1)
weight0_1=2*np.random.random((3,hidden_size))-1
weight1_2=2*np.random.random((hidden_size,1))-1
def relu(x):
    return (x>0)*x
def reluback2(x):
    return x>0
for i in range(60):
    layor_2_error=0
    for j in range(len(walkstop)):
        layor_0=streetlights[j:j+1]
        layor_1=relu(layor_0.dot(weight0_1))
        layor_2=layor_1.dot(weight1_2)
        delta_2=layor_2-walkstop[j:j+1]
        delta_1=weight1_2.T*delta_2*reluback2(layor_1)
        delta_weight1_2=layor_1.T.dot(delta_2)
        delta_weight0_1=layor_0.T.dot(delta_1)
        weight0_1-=delta_weight0_1*alpha
        weight1_2-=delta_weight1_2*alpha
        layor_2_error+=np.sum((layor_2-walkstop[j:j+1])**2)
    if i%10==9: print(layor_2_error)
#要点： 1.算delta1时，记得relu回去,因为weight1_2*delta_2中可能出现小于零的元素，不能让他影响layer1.
#2.weight 均为列向量，layer均为行向量。
#3.计算deltaweight的公式：deltaweight i_j=layer_i.T .dot(delta_j)*alpha
#4.layor_i=layor_j .dot(weight_i_j)
#5.delta_i=delta_j.dot(weighti_j)*reluback(layer_i)
#6.error_j=np.sum((layer_j-goal_layer_j)**2)

        
        