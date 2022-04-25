import facebook
import csv
import requests

graph = facebook.GraphAPI(access_token='EAACEdEose0cBAE1e2ZC3i64I3QfkBK7MHv1mI8GCzUtNNBjczhwEBxQttLosAkoZAvsHB9llfVdLpq1Nz4qvE35zkEHtPpjOyaCllzzScxgydtqMskZB98xPgCzx4cQLiWKbb38yN0tJ0ncGb76zFxr9RtXs5uJFshkiCNyGQZDZD', version='2.5')
post = graph.get_object("yonseibamboo/posts?fields=message,created_time&limit=100&since=1456790439")
file = open(str("./")+str("data")+str('.csv'), "w" )
cw_content = csv.writer(file, delimiter = ',', lineterminator = '\n' )
page = 1
while True:
    if not 'paging' in post :
        break
    
    for i in range(0, len(post['data'])):
        try :
            cont=[]
            message = post['data'][i]['message'] # i번째 제보
            date = post['data'][i]['created_time'][0:10] # 날짜
            time = post['data'][i]['created_time'][10:] # 시간


            cont.append(message)
            cont.append(date)
            cont.append(time)
            cw_content.writerow(cont)

        except :
            pass
        
    page = page + 1
    post = requests.get(post['paging']['next']).json()
    



file.close()
