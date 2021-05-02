





print(ill)

for i in range(1,T):
    temp = (alpha-1)*R[i-1]-alpha * R[i-1] + mu * I[i-1] +R[i-1]
    R.append(temp)
    temp = L * (gamma-1) * I[i-1] * S[i-1] - gamma * S[i-1] + (1-alpha)*R[i-1] + S[i-1]
    S.append(temp)
    temp = - mu * I[i-1] + L * (1-gamma)*I[i-1]*S[i-1] + I[i-1]
    I.append(temp)


for i in range(96,99):

    print(S[i])
    print(I[i])
    print(R[i])
   

