import urllib, base64, json, requests
#uncomment to handle files stored on the web

########### Python 2.7 #############
import http.client, base64, json, os
import urllib.parse

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
subscription_key = '552bf79e0d7846d1b35e5495bb94868e'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'eastus.api.cognitive.microsoft.com'

headers = {
    # Request headers.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.parse.urlencode({
    # Request parameters. All of them are optional.
    'visualFeatures': 'Categories,Description,Color',
    'language': 'en',
})

# The URL of a JPEG image to analyze
body = "{'url':'https://preview.ibb.co/mN4xqc/love_copy.jpg'}"

try:
    # Execute the REST API call and get the response.
    conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()

    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
    """
    print ("Response:")
    #this is the returned json:
    #myJson = json.dumps(parsed, sort_keys=True, indent=2)
    #print (json.dumps(parsed, sort_keys=True, indent=2))
    #since we only care about a pure image description:
    """
    for things in parsed:
        if(things == 'description'):
            #print('************')
            #print(things)
            #print('************')
            for thing in parsed['description']['captions']:
                    #print thing
                    #print('*********')
                    print ('This is {}').format(thing['text'])
                        
    conn.close()

except Exception as e:
    print('Error:')
    print(e)
"""

#handling locally saved file:

########### Python 3.6 #############
headers = {
    # Request headers.
    'Content-Type': 'application/octet-stream',

    # NOTE: Replace the "Ocp-Apim-Subscription-Key" value with a valid subscription key.
    'Ocp-Apim-Subscription-Key': '552bf79e0d7846d1b35e5495bb94868e',
}

params = {
    # Request parameters. All of them are optional.
    'visualFeatures': 'Categories',
    'details': 'Celebrities',
    'language': 'en',
}

# Replace the three dots below with the full file path to a JPEG image of a celebrity on your computer or network.
image = open('/Users/Tomeraharoni/Documents/MakeHarvard/images/love.JPG','rb').read() # Read image file in binary mode

try:
    # NOTE: You must use the same location in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westus, replace "westcentralus" in the 
    #   URL below with "westus".
    response = requests.post(url = 'https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/analyze',
                             headers = headers,
                             params = params,
                             data = image)
    data = response.json()
    print(data)
    for things in data:
        if(things == 'description'):
            print('************')
            print(things)
            print('************')
            for thing in parsed['description']['captions']:
                    print (thing)
                    print('*********')
                    print ('This is {}').format(thing['text'])
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
####################################
"""