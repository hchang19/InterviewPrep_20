def droppedRequests(requestTime):
    #Starting time for the time frame

    time_frame_1s = []
    time_frame_10s = []
    time_frame_1m = []
    
    count = 0
    for req in requestTime:
        
        #flush the requests not in the time frame
            
        #for 1s time frame
        while len(time_frame_1s) != 0 and time_frame_1s[0] < req:
            time_frame_1s.pop(0)
                
        #for 10s time frame
        while len(time_frame_10s) != 0 and time_frame_10s[0] < req - 9:
            time_frame_10s.pop(0)

        # #for 1m time frame
        while len(time_frame_1m) != 0 and time_frame_1m[0] < req - 59:
            time_frame_1m.pop(0)
            
        
        #append request in the time frame
        time_frame_1m.append(req)
        time_frame_1s.append(req)
        time_frame_10s.append(req)

        if(len(time_frame_1m ) > 60):
            count += 1
        elif(len(time_frame_10s) > 20):
            count += 1
        elif (len(time_frame_1s) > 3):
            count += 1
        

        #drop request according to the scheme and increment
    return count


sampleRequests = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,
                    7,7,7,7,11,11,11,11]
print(droppedRequests(sampleRequests))