print (chr(27)+"[33m"+"               =========================================")
print (chr(27)+"[33m"+"                           Wifi Server Info            ")
print (chr(27)+"[33m"+"               =========================================")
print (chr(27)+"[33m"+"                    Author : Rahat Khan Tusar(rkt)      ")
print (chr(27)+"[33m"+"                   Github  : https://github.com/r3k4t   ")
print (chr(27)+"[33m"+"               =========================================")
import speedtest
st = speedtest.Speedtest()
st.download()
st.upload()
servernames = []
st.get_servers(servernames)
print (st.results)
