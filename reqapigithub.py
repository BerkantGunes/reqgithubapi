import requests

class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'

    def getUser(self,username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json() # dondurulen bilgi JSON ile dict veri yapisina cevrilir
    
    def getRepositories(self,username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()
    
github = Github()

while True:
    secim = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSecim: ')

    if secim == '4':
        break

    else:
        if secim == '1':
            username = input('username: ')
            result = github.getUser(username)
            print(f'name: {result['name']} public repos: {result['public_repos']} follower : {result['followers']}')

        elif secim == '2':
            username = input('username: ')
            result = github.getRepositories(username)

            # repolarin icinde gezmek icin dongu kullaniriz
            for repo in result:
                print(repo['name'])
                
        elif secim == '3':
            pass
        else:
            print('yanlis secim')