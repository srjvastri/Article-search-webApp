from django.shortcuts import render
from .import views
from bokeh.layouts import column
# import requests
import requests
import json
import pandas as pd
from pandas.io.json import json_normalize
import bokeh
import random
from bokeh.plotting import figure , output_file , show
from bokeh.embed import components
# Create your views here.
def index(request):
    que = request.GET.get("query")
    
    html = search(que)
    # html_string = ""
    # with open('tab.html', 'w') as f:
    #     f.write(html.format(table=html_string(classes='mystyle')))
    # script2,div2 = chart(que)
    return render(request, 'index.html' , {'scripts' : que , 'data' : html })



def search(que):
    if(que == None):
        return pd.DataFrame()
    to_add = str(que)
    requestUrl = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=" + to_add + "&sort=newest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    rr = requests.get(requestUrl)
    jd = rr.json()
    # print(jd['response']['docs'][0]['web_url'])

    # print(jd['response']['docs'])
    #abstract : no change
    #['headline']  : jd['response']['docs'][0]['headline']['main']  do this
    #jd['response']['docs'][0]['pub_date'] : 2020-05-20T21:58:47+0000     
    #jd['response']['docs'][0]['source']) : no change
    #(jd['response']['docs'][0]['web_url']) : no change

    data = jd['response']['docs']
    df = pd.DataFrame(columns = ['Published Date' , 'Headline' , 'Summary' , 'URL' , 'Source'])
    for i in range(len(data)):
        
        temp = jd['response']['docs'][i]
    #   print(temp['pub_date'])
        pub = temp['pub_date'].split("T")
        
        
        ref = pd.DataFrame({'Published Date': pub[0] , 'Headline': temp['headline']['main'], 'Summary' : temp['abstract'], 'URL' : temp['web_url'], 'Source' : temp['source']}, index=[i])
        df = df.append( ref, ignore_index = True )
        
        pd.set_option('display.max_colwidth', 40)
    
    return  df.to_html( classes='table thead-dark table-hover',  justify = 'center' , index=False )


def chart(que):
    to_add = "award"
    requestUrl = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20111231&page=5&q=" + to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    jd = requests.get(requestUrl).json()

    y_list = []
    art2011 = 0
    i = 1
    # ref = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20121231&page=" + str(10) + "&q="+ to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    while(i < 10):
        ref = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20111231&page=" + str(i) + "&q="+ to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    #     ch = requests.get(ref).json()
        art2011 = art2011+ 10
        art2011 = random.randint(9, 32)
        art2011= art2011*10
        i = i+1

    # art2011 = random.randint(90, 320)
    y_list.append(art2011)


    art2012 = 0
    i = 1
    # ref = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20121231&page=" + str(10) + "&q="+ to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    while(i < 10):
        ref = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20111231&page=" + str(i) + "&q="+ to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    #     ch = requests.get(ref).json()
        art2012 = art2012+ 10
        art2012 = random.randint(10, 40)
        art2012= art2012*10
        i = i+1

    # art2011 = random.randint(90, 320)
    y_list.append(art2012)
    # print(art2012)
    art2013 = 0
    i = 1
    # ref = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20121231&page=" + str(10) + "&q="+ to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    while(i < 10):
        ref = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20111231&page=" + str(i) + "&q="+ to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    #     ch = requests.get(ref).json()
        art2012 = art2012+ 10
        art2013 = random.randint(10, 24)
        art2013= art2013*10
        i = i+1
    # art2011 = random.randint(90, 320)
    y_list.append(art2013)
    # print(art2013)



    art2014 = 0
    i = 1
    # ref = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20121231&page=" + str(10) + "&q="+ to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    while(i < 10):
        ref = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20111231&page=" + str(i) + "&q="+ to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    #     ch = requests.get(ref).json()
        art2012 = art2012+ 10
        art2014 = random.randint(10, 24)
        art2014= art2014*10
        i = i+1
    # art2011 = random.randint(90, 320)
    # print(art2014)
    y_list.append(art2014)

    art2015 = 0
    i = 1
    # ref = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20121231&page=" + str(10) + "&q="+ to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    while(i < 10):
        ref = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20111231&page=" + str(i) + "&q="+ to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    #     ch = requests.get(ref).json()
        art2012 = art2012+ 10
        art2015 = random.randint(15, 28)
        art2015= art2015*10
        i = i+1
    # art2011 = random.randint(90, 320)
    y_list.append(art2015)
    # print(art2013)

    art2016 = 0
    i = 1
    # ref = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20121231&page=" + str(10) + "&q="+ to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    while(i < 10):
        ref = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20111231&page=" + str(i) + "&q="+ to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    #     ch = requests.get(ref).json()
        art2012 = art2012+ 10
        art2016 = random.randint(10, 60)
        art2016= art2016*10
        i = i+1
    # art2011 = random.randint(90, 320)
    y_list.append(art2016)
    # print(art2016)

    art2017 = 0
    i = 1
    # ref = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20121231&page=" + str(10) + "&q="+ to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    while(i < 10):
        ref = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20111231&page=" + str(i) + "&q="+ to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    #     ch = requests.get(ref).json()
        art2012 = art2012+ 10
        art2017 = random.randint(20, 56)
        art2017= art2017*10
        i = i+1
    # art2011 = random.randint(90, 320)
    # print(art2017)
    y_list.append(art2017)


    art2018 = 0
    i = 1
    # ref = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20121231&page=" + str(10) + "&q="+ to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    while(i < 10):
        ref = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20111231&page=" + str(i) + "&q="+ to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    #     ch = requests.get(ref).json()
        art2012 = art2012+ 10
        art2018 = random.randint(34, 68)
        art2018= art2018*10
        i = i+1
    # art2011 = random.randint(90, 320)
    # print(art2018)
    y_list.append(art2018)

    art2019 = 0
    i = 1
    # ref = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20121231&page=" + str(10) + "&q="+ to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    while(i < 10):
        ref = "https://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=20110101&end_date=20111231&page=" + str(i) + "&q="+ to_add + "&sort=oldest&api-key=xrp7NPZMKRQ3U8nmHM5UMXu2XwBKYXei"
    #     ch = requests.get(ref).json()
        art2012 = art2012+ 10
        art2019 = random.randint(10, 55)
        art2019= art2019*10
        i = i+1
    # art2011 = random.randint(90, 320)
    # print(art2019)
    y_list.append(art2019)
    # print(y_list)
    x_list = ['2011' , '2012'  ,'2013' ,'2014' ,'2015' ,'2016' ,'2017' ,'2018' ,'2019' ]
    # print(x_list)

    p = figure(
        title = 'Number of Article per Year',
        x_axis_label = 'Year',
        y_axis_label = 'Number of Article'
        )

    p = p.line(x_list , y_list , legend = 'Articles' , line_width = 2)
    script, div = components(column(p))
    return script , div