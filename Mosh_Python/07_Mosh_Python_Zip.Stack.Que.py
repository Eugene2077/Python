
# Zip ----------------------------------------
list1 = [1,2,3]
list2 = [10,20,30]
# if we wanna combine those two list like this [(1,10),(2,20),(3,30)]
zipped = zip(list1,list2)  # 여기서 저장된 값은 메모리의 위치만 참조, 그러나 이상태로도 iteration 은 가능하다. 
print(list(zipped))        # list 로 casting 한 뒤 print

print(list(zip("abc",list1,list2))) # 이렇게 string 을 같이 넣어도 됨,, tuple에 각각 한개씩 넣는다


# Stacks ----------------------------------------
# LIFO : Last In First Out 후입선출
# when we browsing a website, if we hit the back button, go to the previous page and hit the back button again
#it take us previous of previous page,, this is how Stacks working
# In python, basically we use a list object as a stack
browsing_session = []           # an empty list
browsing_session.append(1)      # the user navigate the website No.1
browsing_session.append(2)      # the user navigate the website No.2
browsing_session.append(3)      # the user navigate the website No.3
print(browsing_session)         # now we have a stack (list of browsing history)
browsing_session.pop()          # when the user hit the back button, we should remove the last item. Return the value
print(browsing_session)         # now we have back to previous webpage
print(browsing_session[-1])     # using [-1], we can get the last item (the last page: current page)
# if the list is empty(계속 뒤로가기 눌러서 모든 리스트가 삭제됬다면) the back button need to be disabled, 리스트가 비었는지 어떻게 알수 있을까?
if not browsing_session:        # an empty list is considered as "False" (처음부분 boolean 강좌 참조)
    print("disable back button")   # 여기에 버튼 비활성화시키는 명령어 

# 즉 요약하면, empty list 를 만들고 append() 와 pop() 를 사용하여 Stack 을 처리하고 [-1]을 이용하여 가장 나중에 들어간 item을 골라낸다는 것.


# Queues ----------------------------------------
# FIFO : First In First Out
# FIFO의 경우 list[] 에 맨 앞에 있는것부터 처리하게 되는데, 하나를 delete 하면, 리스트가 짧으면 별 문제가 없지만, 리스트가 아주 긴 경우 모든 element가 
#순차적로 하나씩 앞으로 자리이동을 해야하므로 system performance 에 영향을 미치게 된다. 따라서 아래와 같이 deque를 사용하게 되는데, 
from collections import deque   # deque 를 불러오고
queue = deque([])               # wrap an empty list with a deque object
queue.append(1)                 # 뒤에 element 추가
queue.append(2)                 # 뒤에 element 추가
queue.append(3)                 # 뒤에 element 추가
queue.popleft()                 # 맨 왼쪽의 element(1)가 제가되었지만, 나머지 element 들은 이동하지 않고 그자리에 있다.
if not queue:                   # check if the list is empty
    print("empty")
