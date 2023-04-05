import pandas as pd
import time
import os

read_file=pd.read_csv('학교기본정보_2023년02월28일기준.csv')

while True:
    print("찾을수 있는 학교급\t초등학교~고등학교")
    print("찾을 학교의 이름을 입력하세요 \t~~초등학교 등과 같이 입력")
    print("입력 :",end=" ")
    loc_num=-1
    school_name=input()
    for lat in read_file['학교명']:
        loc_num+=1
        if lat == school_name:
            break

    if loc_num <= 12553:
        print(read_file.loc[loc_num])
    else:
        print("검색되지 않는 학교입니다.")
    while True:
        print("계속 검색 하시겠습니까(y/n) : ",end=" ")
        answer=input()
        if answer=="y" or answer=="Y":
            os.system("clear")      # windos os 에선 cls명령
            break
        elif answer=="n" or answer=="N":
            print("종료합니다")
            time.sleep(1)
            exit()