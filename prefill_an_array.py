# Prefill an array
# https://www.codewars.com/kata/54129112fb7c188740000162
# 04/11/2021

# The final submitted function
def prefill(n,v=None):
    try:    
        return [v for i in range(int(n))]
    except:
        raise TypeError("{} is invalid".format(n))

# Test code sample
#generated_array = prefill('0','2d')
# generated_array = prefill(0,'abc')
#print(generated_array)