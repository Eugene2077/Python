



# we made modules2 folder as a package folder by adding a file name '__init__'
# now we can import the modules in modules2 folder



import modules2.module_temp     # import the module
modules2.module_temp.to_cel(50) # execute a function in the folder
modules2.module_temp.to_feh(50) # execute a function in the folder

# we have another way(much better) 

from modules2.module_temp import to_cel, to_feh
to_cel(60)
to_feh(60)

# another way

from modules2 import module_temp
module_temp.to_cel(50)    # 이렇게하면 module_temp 후 .(dot)을 입력하면 그 module에 있는 모든 사용가능한 member를 선택할 수 있다.
module_temp.to_feh(50)

# 먄약 원하는 module 이 서브폴더에 있는경우 인식을 못하는데, 이 경우 서브폴더에 역시 __init__.py(모든 module 폴더에 필요)만들고 아래와 같이 경로를 지정해 주면 된다.

from modules2.sub import sub_module
sub_module.message(5)

# Intra-package References : 만약 어느 module이 다른 module 의 function, variable 을 이용하는경우 공통되는 상위 디렉토리부터 경로 지정해서 쓰면 됨
# 그러나 그 module 파일을 직접 실행하면 공통 상위폴더를 찾을 수 없다고 나옴,  module로서만 사용해야 함(직접 실행하지말고 여기를 통해서 실행)
from modules2.sub2 import a_file
a_file.orange(15)

# the "dir" function
print (dir(modules2))
# with the function dir, we get an array of strings: all the attributes and methods in the directory