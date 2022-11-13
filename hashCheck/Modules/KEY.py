from virus_total_apis import PublicApi as VirusTotalPublicApi

keyFile = open("KEY.txt","r")

API_KEY = keyFile.readline().strip("\n")

virustotal = VirusTotalPublicApi(API_KEY)
