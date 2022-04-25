#program to calculate the time that takes for a Bamboo Forest post to be uploaded after it is written
#The Bamboo Forest states that all posts are uploaded in 72 hours and we are going to find out if that statement is true or not

import csv

file= open('./data.csv','r')
csvreader=csv.reader(file)
data= []


violate=0
count=0
total_how_long=0
k=0
time_data=[]

for line in csvreader:
    data.append(line)

while k<len(data):
    try:
        #the time when the post was written by a Facebook User
        time_written=str(data[k][0][18:41]).strip('\n')
        time_written=time_written.strip(' ')

        #there are cases when the Facebook User wants the written time to be erased
        #we exclude such posts
        if str(2016) in time_written:
            print('The time when this post was written is:', time_written)
            w_month=int(time_written[6:7])
            if len(time_written)==23:
                w_day=int(time_written[9:11])
                w_hour=int(time_written[15:17])
                w_minute=int(time_written[18:20])
                w_second=int(time_written[21:23])
            if len(time_written)==22:
                w_day=int(time_written[9:11].strip(' '))
                w_hour=int(time_written[14:16].strip(' '))
                w_minute=int(time_written[17:19])
                w_second=int(time_written[20:22])
            if len(time_written)==21:
                w_day=int(time_written[9:10])
                w_hour=int(time_written[14:15])
                w_minute=int(time_written[16:18])
                w_second=int(time_written[19:21])

            #express the hours in a 24-hour system
            if '오후' in time_written and int(w_hour)>=1 and int(w_hour)<=11:
                w_hour=int(w_hour)+12
            if '오전' in time_written and int(w_hour)==12:
                w_hour=int(w_hour)-12

            #the time when the post was uploaded by the Bamboo Forest
            time_uploaded=str(data[k][1][0:5]+' '+data[k][1][6:8]+' '+data[k][1][8:10]+' '+data[k][2][1:9])
            time_uploaded=time_uploaded.replace('-','.')
            time_uploaded=(time_uploaded[0:24])
            u_month=int(time_uploaded[6:7])
            u_day=int(time_uploaded[9:11])
            u_hour=int(time_uploaded[12:14])
            u_minute=int(time_uploaded[15:17])
            u_second=int(time_uploaded[18:20])

        
            print('The time when this post was uploaded by Yonsei Bamboo Forest is:', time_uploaded, '[Greenwich Mean Time/ 9 hours behind Korean Standard Time]')

            #Calculate the difference between the written time and the uploaded time
            
            #The number of days in each month
            January= 31
            February= 29   
            March= 31
            April= 30
            May= 31
            

            #The number of seconds in the accumulated previous months for the month when the post was written
            if w_month==2:
                w_month_sec=(January)*24*60*60
                        
            if w_month==3:
                w_month_sec=(January+February)*24*60*60
            
            if w_month==4:
                w_month_sec=(January+February+March)*24*60*60
       
            if w_month==5:
                w_month_sec=(January+February+March+April)*24*60*60
                w_day_sec=w_day*24*60*60

            if w_month==6:
                w_month_sec=(January+February+March+April+May)*24*60*60
                w_day_sec=w_day*24*60*60

            #convert the number of days, hours, and minutes into seconds for the time written
            w_day_sec=w_day*24*60*60
            w_hour_sec=w_hour*60*60
            w_minute_sec=w_minute*60
            total_w_sec=w_month_sec+w_day_sec+w_hour_sec+w_minute_sec+w_second

            #The number of seconds in the accumulated previous months for the month when the post was uploaded 
            if u_month==2:
                u_month_sec=(January)*24*60*60

            if u_month==3:
                u_month_sec=(January+February)*24*60*60
        
            if u_month==4:
                u_month_sec=(January+February+March)*24*60*60
        
            if u_month==5:
                u_month_sec=(January+February+March+April)*24*60*60

            if u_month==6:
                u_month_sec=(January+February+March+April+May)*24*60*60
                u_day_sec=u_day*24*60*60

            #convert the number of days, hours, and minutes into seconds for the time uploaded
            u_day_sec=u_day*24*60*60
            u_hour_sec=u_hour*60*60
            u_minute_sec=u_minute*60
            total_u_sec=u_month_sec+u_day_sec+u_hour_sec+u_minute_sec+u_second

            #subtract the 'total seconds of the written time' from the 'total number of seconds of the uploaded time'
            #we need to add 9 hours since the uploaded time in the excel file is based on Greenwhich Mean Time
            how_long=(total_u_sec-total_w_sec)+9*60*60

            #add the data to a list in order to find the max and min values for later use
            time_data.append(how_long)

            #keep adding the time data in order to calculate the average time for later use
            total_how_long=total_how_long+ how_long     

            #convert the time difference(seconds) into 'days, hours, minutes, and seconds' format
            minute=how_long//60
            second=how_long%60
    
            hour=minute//60
            minute=minute%60
    
            day=hour//24
            hour=hour%24

            print('it took', day, 'day(s)', hour,'hour(s)', minute, 'minute(s)', second, 'second(s) for the post to be uploaded\n')

            #count the number of posts used for analysis
            count=count+1

            #count the number of posts that have been uploaded after 72 hours
            if how_long>= 3*24*60*60:
                violate=violate+1
            
    #make an exception for the posts that do not have proper format for analysis    
    except ValueError:
        print('The format of this particular post provided by Facebook is unsuitable for analysis\n')
                
    k=k+1


#now, let's calculate the average time it takes for a post to be uploaded
average_second=total_how_long//count
average_minute=average_second//60
average_second=average_second%60
average_hour=average_minute//60
average_minute=average_minute%60   
average_day=average_hour//24
average_hour=average_hour%24
print()
print('On average, the post is uploaded in', average_day, 'day(s)', average_hour, 'hour(s)', average_minute, 'minute(s)', average_second, 'second(s)')    

#calculate the maximum time it takes for a post to be uploaded
max_time=max(time_data)
max_minute=max_time//60
max_second=max_time%60
max_hour=max_minute//60
max_minute=max_minute%60
max_day=max_hour//24
max_hour=max_hour%24
print()
print('The maximum amount of time taken for a post to be uploaded is', max_day, 'day(s)', max_hour, 'hour(s)', max_minute, 'minute(s)', max_second, 'second(s)')

#calculate the minimum time it takes for a post to be uploaded
min_time=min(time_data)
min_minute=min_time//60
min_second=min_time%60
min_hour=min_minute//60
min_minute=min_minute%60
min_day=min_hour//24
min_hour=min_hour%24
print()
print('The minimum amount of time taken for a post to be uploaded is', min_day, 'day(s)', min_hour, 'hour(s)', min_minute, 'minute(s)', min_second, 'second(s)')

#print the number of posts that violate the 72 hour uploading statement
print()
print('The Bamboo Forest promises that each post will be uploaded in 72 hours. Of the total', count,' posts', violate, 'posts have violated this regulation.')
