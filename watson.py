# import json 
# from watson_developer_cloud import VisualRecognitionV3

# visual_recognition = VisualRecognitionV3(
#     version='2018-03-19',
#     iam_apikey='9ccc76ukWVTdBbtQWgMF8iZspq84vEXzDwhKRW76EDp7'
# )
# with open('C:/Users/arsal/Desktop/test.jpg','rb') as im:
#     result= visual_recognition.classify(
#         image_file=im,threshold='0.6',classifier_ids='DefaultCustomModel_596598549'
#     ).get_result()

# print(json.dumps(result,indent=2))
import json
import ibm_watson
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#print(ibm_watson.__version__)
authenticator = IAMAuthenticator('9ccc76ukWVTdBbtQWgMF8iZspq84vEXzDwhKRW76EDp7')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)

visual_recognition.set_service_url('https://api.kr-seo.visual-recognition.watson.cloud.ibm.com/instances/759b0fe8-7620-4b8d-9fc0-2bbabc10be67')

with open('C:/Users/arsal/Desktop/anaconda/procure_me/test.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file=images_file,
        threshold='0.6',
        owners=["me"]).get_result()
    y=json.dumps(classes['images'])
    y=str(y)
    print(y)
    a=0
    l=[]
    for i in y.split():
        #print(i,a)
        l.append(i)
        a+=1
    print(l[9])
    #print(type(classes))dict
    # for i in classes['custom_classes']:
    #     print(i)