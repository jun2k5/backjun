#log_info

군 복학 후 프로그래밍이 아무것도 기억안나
일단 Python으로 백준 1번부터 풀어보도록 하겠다.

Python이 끝나면
C, C#, C++, JAVA, Node.js도 1번부터 시도할 것이다.

환경

    OS : Windows 11 (Pro) x86_64
    Kernel: WIN32_NT 10.0.22631.4391 (23H2)
    Shell: CMD 10.0.22621.4391
    CUP : AMD Ryzen 7 7700 (16) @ 5.35 GHz
    GPU : NVIDIA GeForce RTX 3060 (7.85 GiB) [Discrete]
    Memory : 31.72 GiB
    Swap : 2.00 GiB
    Python : Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32

2024-11-01

    Git 사용법
    깃으로 관리할 작업 폴더를 만들고
    작업 폴더에서 Window PowerShell을 연다.
    여는 방법은 Shift + 우클릭 => 여기에 PowerShell 창 열기
    
    명령어
        git config --global user.email "이메일 명"
        git config --global user.name "이름"
            //현재 깃 사용자 등록

        
    애디터실행 후 작업파일 열기
    Terminal에서 new Terminal 클릭
    명령어
        git init
        git add . or git add file_name
        git commit -m 'comment'
        git push origin master

    에러 대처
        error : failed to push some ..
        푸시 실패 메시지가 나오면 pull로 내 로컬과 Git의 파일을 일치시키고 푸시할 것
            git pull origin master

2024-11-03

    Visual Code 단축키

    Cntl + ` = 터미널 탭으로 focus 이동
    Cntl + 1 = edit 탭으로 focus 이동

    바꾸고 싶은 공통된 단어 드래그
    Cntl + Shift + L
    한꺼번에 많은 공통 단어를 치환할 수 있다.

    함수일 경우 F2를 사용하여 Rename할 수 있다.

    Alt + 클릭하면 멀티 커서가 가능하다.

    emmet 명령어 + tab html or css  
    ex ) div>p*3 + tab
        div.container>p.title*5 + tab
        dn + tab
        m10 + tab

    ShortCuts
    코드 하일라이트 = Cntl + L
    휠 and 코드 워프 = Cntl + 방향키
    코드 이동 and 파일탭 이동 = Alt + 방향키
    행복사 = Alt + Shift + 방향키
    파일 검색 & 이동 = Cntl + p
    
2024-11-06

    Git 명령어 2

    커밋로그를 보여주는 Git 명령어
        git log --oneline --all --graph

    변경점을 알려주는 git 명령어
        git diff

    vim 모드로 변경점을 알려주는 git 명령어
        git difftool

    커밋 ID로 현재 파일과 커밋파일의 차이점을 비교하는 git 명령어
        git difftool Commit_ID

    브랜치 생성 - 복사본을 만들 수 있다.
        git branch branch_name
    
    브랜치 이동
        git switch branch_name

    현재 브랜치 확인
        git status

    브랜치 합치기
        메인 브랜치로 이동 후
        git merge sub_branch_name

    브랜치 합칠때 수정부분이 겹칠 경우, 충돌(conflict) 발생

     Conflict 해결 방법
        1. 원하는 코드만 남기고
        2. git add .
        3. git commit -m 'commit_message'



