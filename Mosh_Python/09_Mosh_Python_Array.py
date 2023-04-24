# when we dealing with a large number of data, using Array is more efficient
# array is taking less memory and provide better perfomance (when the data is large, ex: more than 1000 data)
# 그러므로, 데이터가 방대한 경우에만 사용하면 되고, 그렇지 않은 경우에는 이를 사용할 필요가 없다

from array import array  # import the module(called 'array') from class'array

# call array()
# parameter 1:typecode - 이 array에 어떤 object type을 사용할지 결정 https://docs.python.org/3/library/array.html 참고
# parameter 2:data

numbers = array("i", [1,2,3]) 
# now we create an array, it is similar to list, so we can use append, pop, insert, remove etc,,, 
# 하지만 data type 는 엄격히 제한되어 첫번째 parameter 에서 지정한 data type 외에는 사용하지 못한다. 


