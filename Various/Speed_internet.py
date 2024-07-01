# pip install speedtest-cli

from speedtest import Speedtest

st = Speedtest()

download=float(st.download()/1000/1000)
upload=float(st.upload()/1000/1000)

print(f'Скорость загрузки - {download:.2f} mBit/s')
print(f'Скорость   отдачи - {upload:.2f} mBit/s')
