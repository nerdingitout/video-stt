# step 4: save transcript to cloudant db

from ibmcloudant.cloudant_v1 import Document, CloudantV1
from ibmcloudant import CouchDbSessionAuthenticator
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator
import random
import config
import stt
#print(stt.output)


# Save results to Cloudant DB
authenticator = BasicAuthenticator(config.CLOUDANT_USERNAME, config.CLOUDANT_PASSWORD)

service = CloudantV1(authenticator=authenticator)

service.set_service_url(config.CLOUDANT_URL)
transcript_doc = Document(
    id="transcript-"+str(random.randint(0,500)),
    transcript_txt=stt.output
    )
response = service.post_document(db='test', document=transcript_doc).get_result()
##print(transcript)
