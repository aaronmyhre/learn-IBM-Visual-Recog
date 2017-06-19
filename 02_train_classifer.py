import os, sys, json
from watson_developer_cloud import VisualRecognitionV3


# Create instance of VisualRecognition Class based on our API key
vr = VisualRecognitionV3('2016-05-20', api_key = '')


# List any existing classifiers
classifier = vr.list_classifiers(verbose=True)
print(classifier)

# delete
'''
for c in classifier['classifiers']:
    print(c)
    vr.delete_classifier(c['classifier_id'])

# Create classifier
print(os.path.isfile('./hotdogs_train.zip'))
print(os.path.isfile('./hamburgers_train.zip'))
with open('./hotdogs_train.zip', 'rb') as hotdog, open('./hamburgers_train.zip', 'rb') as hamburger:
    vr.create_classifier("hotdog",
        hotdog_positive_examples = hotdog,
        negative_examples = hamburger
        )


# Query classifier

with open('hotdogs_test.zip', 'rb') as tests:
    results = vr.classify(images_file=tests,
                            threshold=0.1,
                            classifier_ids=[
                                'hotdog_2117466228',
                                #'default'
                                 ])
    print(json.dumps(results, indent=2))
'''
