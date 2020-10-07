import wget

print('Beginning file download with wget module')


def filedownload(branch_name):
    url = 'https://sjc-cm01.olympus.f5net.com/build/bigip/project/{}/daily/'.format(branch_name)
    #url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
    wget.download(url, '/tmp/')
