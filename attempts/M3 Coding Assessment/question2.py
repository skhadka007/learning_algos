def test(a):
    times_list = []
    times_list_str = []
    n = int(a[0])
    for i in range(1, n+1):
        # print(a[i])
        times_list_str.append(str(a[i]))
        print(times_list_str[i-1])
        times_list.append(int(str(a[i]).replace(':', '')))
        print(times_list[i-1])
        
    

a = [10, '15:41:24', '21:40:40', '05:27:01', '13:37:33', '07:40:36', '08:03:28', '03:46:47', '20:05:22', '04:04:57', '04:34:40']
test(a)


  