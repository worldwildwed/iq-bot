from iqoptionapi.stable_api import IQ_Option
import logging
import time
 
EMAIL = "los.napath@gmail.com"
PASS = "testbot123456"

#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
I_want_money=IQ_Option(EMAIL, PASS)
I_want_money.connect()#connect to iqoption
while_run_time=10
 
#For digital option
 
name="live-deal-digital-option" #"live-deal-binary-option-placed"/"live-deal-digital-option"
active="EURUSD"
_type="PT1M"#"PT1M"/"PT5M"/"PT15M"
buffersize=10#
print("_____________subscribe_live_deal_______________")
I_want_money.subscribe_live_deal(name,active,_type,buffersize)

 
start_t=time.time()
while True:
    #data size is below buffersize
    #data[0] is the last data
    data=(I_want_money.get_live_deal(name,active,_type))
    print("__For_digital_option__ data size:"+str(len(data)))
    print(data)
    print("\n\n")
    time.sleep(1)
    if time.time()-start_t>while_run_time:
        break
print("_____________unscribe_live_deal_______________")
I_want_money.unscribe_live_deal(name,active,_type)
