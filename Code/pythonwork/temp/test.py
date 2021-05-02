N = 24230000                # 总人数(上海)
L = 0.7                       # 平均每人每天有效感染人数
alpha = 0.9                 # 获得免疫概率
mu = 0.07                   # 每天治愈人数占患病人数比例
perDay = 15                 # 平居治愈天数
sigma = 105                 # 每个患者感染期间感染人数
gamma = 0.0035              # 每日接种比

ill = 0.000005              # 初始患病人数
T = 100


S,M,I,R,dat = [],[],[],[],[]
S.append(1-ill)
M.append(0)
I.append(ill)
R.append(0)

for i in range(1,t):
    temp = -L*S(t)*I(t)+(1-alpha)*R(t)
    S.append(temp)
    temp = -L*s(t)*I(t)-mu*I(t)
    I.append(temp)
    temp = mu*I(t)-(1-alpha)*R(t)
    R.append(temp)
for i in range(1,10):
  print(S[i])
  print(I[i])
  print(R[i])
