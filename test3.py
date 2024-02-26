dict1={'words_result': [{'words': '雲師'}, {'words': '云师堂'}, {'words': '总有一种技法让你目眩神迷'}, {'words': '2020年普通高等学校招生全国统一考试(3卷)'}, {'words': '文科数学试题解析'}, {'words': '一.选择题：本题共12小题，每小题5分，共60分'}, {'words': '1.已知集合A={1,2,3,5,7,11},B={x|3<x<15},则A∩B中元素个数为'}, {'words': '()'}, {'words': 'A.2'}, {'words': 'B.3'}, {'words': 'C.4'}, {'words': 'D.5'}, {'words': '【答案】B'}, {'words': '【解析】'}, {'words': 'A∩B={5,7,11},则A∩B中共有3个元素，选B。'}, {'words': '2.若z(1+i)=1-i，则z='}, {'words': '()'}, {'words': 'A.1-i'}, {'words': 'B.1+i'}, {'words': 'C.-i'}, {'words': 'D.i'}, {'words': '【答案】D'}, {'words': '【法1】'}, {'words': '设z=a+bi，则z(1+i)=(a-bi)(1+i)=(a+b)+(a-b)i，故a+b=l,a-b=-1，解得'}, {'words': 'a=0,b=1，故z=i,选D。'}, {'words': '【法2】'}, {'words': '由(1+1)=1-1一(1-)一1，数z=f，选D.'}, {'words': '3.设一组样本数据x1,x2,…,x的方差为0.01，则数据10x,10x2,…,10x的方差为()'}, {'words': 'A.0.01'}, {'words': 'B.0.1'}, {'words': 'C.1'}, {'words': 'D.10'}, {'words': '【答案】C'}, {'words': '【 解析】'}, {'words': '由D(aX)=a2D(X)得D(10X)=100D(x)=1，选C。'}, {'words': '4.Logistic模型常用的模型之一， 可应用流行病领域。有学者根据公数据'}, {'words': '建立了某地区新冠肺炎累计确诊病例数I(t)(t的单位：天)的logistic模型：'}, {'words': 'I(1)=1+=,其中K为最大确诊病例数。当I(C)=0.95K时,标志着已初步遏制疫情,'}, {'words': '重庆·杨家坪·西城天街B座23A-20·18680703112'}, {'words': '第1页/共11页'}], 'words_result_num': 40, 'log_id': 1752954479329248728}
list1=dict1['words_result']
for i in range(1,len(list1)):
    dict2=list1[i]
    str=dict2['words']
    subjects=['语文','数学','英语','物理','化学','生物','政治','历史','地理']
    for subject in subjects:
        if str.find(subject)!= -1:
            print(subject)