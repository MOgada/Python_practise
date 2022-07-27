for previous_num in range (0,10):
    if previous_num <= 0:
        print ("Current Number"+str(previous_num), "Previous Number"+str(previous_num), "Sum:"+str(previous_num))

    elif previous_num >= 0:
        previous_num_a=previous_num + 1
        sum = previous_num_a + previous_num
        print ("Current Number"+str(previous_num_a),"Previous Number"+str(previous_num), "Sum:"+str(sum))


