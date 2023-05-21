import pickle
import os

scores = list()

def input_scores():
    score=int(input())
    if score > 0:
        scores.append(score)
    return score 

def get_average(scores):
    return sum(scores)/len(scores)

def show_scores(avg):
    print("개인점수:",end=" ")
    for i in scores:
        print(f"{i}",end=" ")
    print()
    print("평균: ",avg)

def search(scores,score):
    count =0
    for i in scores:
        find=0
        count +=1
        if i == score:
            print(f"{score}점은 {count}번 학생의 점수입니다.")
            find = score
            break
    if find == 0:
        print(f"{score}점을 받은 학생은 없습니다.")

filepath = 'C:/Users/ahn/Desktop/mlData/'
filename = 'score.bin'
def save(scores):
    with open(f'{filepath}{filename}','wb') as file:
        pickle.dump(scores,file)

def load():
    with open(filename,'rb') as file:
        scores=pickle.load(file)
    return scores

i=1

    

if not(os.path.exists(filename)):
    while True:    
        print(f"#{i}?",end=" ")
        n = input_scores()
        i+=1
        if n<0:
            break
    save(scores)
else:
    result = load()
    avg = get_average(result)
    print('[파일 읽기]\n')

    print('[점수 출력]')
    show_scores(avg)
