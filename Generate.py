'''
Created on Jul 25, 2016

@author: yangta
'''
import numpy as np
import scipy.sparse.construct as sparse
import random
# from sklearn.cluster import KMeans

# Size configuration

n = 50     # Case Number
p = 100   # Feature
k = 5       # Number of Group
h = 0.4     # Impact of Group
# config = np.array([n,p,k,h])

# generate a random X matrix
X = np.random.random((n,p))     # X is a n x p matrix with the value from 0 to
X = np.around(X, decimals=2)
X = np.where(X > 0.05 , 1, 2)
# X_1 = np.where(X > 0.1 , 1, 2)
# X_2 = np.where(X > 0.6 , 1, 0)
#X = X_1 + X_2

# maintain 0 issue
index = np.where(X==0)
check = index[1]
pair = np.where(check%2==0, check+1, check-1)
newindex = (index[0], pair)
print newindex
X[newindex] = 0





B = sparse.random(p, 1, density=0.1)    # B is random sparse vector
B = B.A
B = np.around(B, decimals=2)
Y_1 = X.dot(B)
Y = np.around(Y_1, decimals=2)

print X.shape
print B.shape
print Y.shape
# Y = np.where(Y_1 > np.median(Y_1, axis=0), 2,1)

# Clustering

# clf = KMeans(n_clusters = k)
# s = clf.fit(Y_1)

# Generate the group
# Y_2 = np.zeros([n,1])
# for i in range(0,n):
#     Y_2[i] = clf.cluster_centers_[clf.labels_[i]]
# Y_2 = np.around(Y_2, decimals=2)
# print Y_2.shape
# G = clf.labels_

# Comprise to Y
# Y = Y_1 * [[1-h]] + Y_2 * [[h]]
# Y = np.around(Y, decimals=2)
print Y

info_ped = np.zeros((X.shape[0],5))
for i in range(X.shape[0]):
    info_ped[i][0] = 1
    info_ped[i][1] = i+1
    info_ped[i][2] = 0
    info_ped[i][3] = 0
    info_ped[i][4] = random.choice([1,2])
    
ped_left = np.column_stack((info_ped, Y))
ped = np.column_stack((ped_left, X))

print type(ped)
print ped.shape

np.set_printoptions(precision=4,suppress=True)

snp = int(X.shape[1]/2)
print type(snp)
charar = np.zeros((snp,4))
for i in range(snp):
    charar[i][0] = 1
#     random.choice(np.arange(1,22))
    charar[i][1] = i
    charar[i][2] = 0
    charar[i][3] = 1000 + i

print type(charar)
print charar.shape

print "Start save txt"
# np.savez("../Data/0726/numpydata", X, B, Y)
np.savetxt("./Data/plink/traitVal.csv", Y, '%5.2f',delimiter=" ")
# np.savetxt("./Data/plink/markerVal.csv", X, delimiter=" ")
# np.savetxt("./Data/0726/G.csv", G, delimiter=",")
np.savetxt("./Data/plink/B.csv", B, '%5.2f',delimiter=" ")
print "File saving done"


print "Start save txt"
# np.savez("./Data/plink/numpydata1", X, B, Y)
np.savetxt("./Data/plink/fakedata1.ped", ped.astype(int),fmt='%d',delimiter=" ")
# np.savetxt("../Data/0726/fakedata.map", charar, delimiter=" ")
np.savetxt("./Data/plink/fakedata1.map", charar.astype(int), fmt='%d', delimiter=" ")
# np.savetxt("./Data/0726/G.csv", G, delimiter=",")
# np.savetxt("../Data/0726/B.csv", B, delimiter=" ")
print "File saving done"


