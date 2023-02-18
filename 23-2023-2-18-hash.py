# lint code 128 hash function
class Solution:
    """
    @param key: A string you should hash
    @param h_a_s_h__s_i_z_e: An integer
    @return: An integer
    """
    def hash_code(self, key, h_a_s_h__s_i_z_e):
        # write your code here
        # 33 是比较常用的数字，用其他数字也均可，但33 可以减少冲突量
        ans = 0
        for i in range(len(key)):
            ans = (ans*33+round(key[i]))/h_a_s_h__s_i_z_e
        return ans

