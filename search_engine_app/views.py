from datetime import datetime
from django.shortcuts import render,HttpResponse
from elasticsearch import Elasticsearch

# Create your views here.
client = Elasticsearch('localhost', port=9200)

def indexluoji(request):
    print(request.method)
    return render(request, 'index.html')

def searchluoji(request):
    key_words = request.GET.get('q', '')
    page = request.GET.get('p', '1')
    try:
        page = int(page)
    except:
        page = 1
    start_time = datetime.now()
    response = client.search(
        index="web_api",
        body={
            "query": {
                "multi_match": {
                    "query": key_words,
                    "fields": ["API name", "Description","Url","Category", "Provider", "ServiceType", "Documentation", "Architectural Style", "Endpoint Url", "Support SSL", "Logo"]
                }
            },
            "from": 0
        }
    )
    end_time = datetime.now()
    last_time = (end_time-start_time).total_seconds()
    total_nums = response["hits"]["total"]["value"]                     # the number of results
    if (page % 10) > 0:                                                 # count the page
        page_nums = int(total_nums/10)+1
    else:
        page_nums = int(total_nums/10)
    hit_list = []
    for hit in response["hits"]["hits"]:
        hit_dict = {}
        # hit_dict["api_name"] = hit["_source"]["API name"]
        hit_dict["architectural_style"] = hit["_source"]["Architectural Style"]
        hit_dict["category"] = hit["_source"]["Category"]
        hit_dict["description"] = hit["_source"]["Description"]
        hit_dict["documentation"] = hit["_source"]["Documentation"]
        hit_dict["endpoint_url"] = hit["_source"]["Endpoint Url"]
        hit_dict["logo"] = hit["_source"]["Logo"]
        hit_dict["provider"] = hit["_source"]["Provider"]
        hit_dict["service_type"] = hit["_source"]["ServiceType"]
        hit_dict["support_SSL"] = hit["_source"]["Support SSL"]
        hit_dict["url"] = hit["_source"]["Url"]
        hit_dict["score"] = hit["_score"]
        hit_dict["id"] = hit["_id"]
        hit_list.append(hit_dict)
    return render(request, 'result.html', {"page": page,
                                           "total_nums": total_nums,
                                           "all_hits": hit_list,
                                           "key_words": key_words,
                                           "page_nums": page_nums,
                                           "last_time": last_time
                                           })