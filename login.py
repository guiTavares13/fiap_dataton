allowed_uses = [{'user' : 'admin', 'password' : 'senha'}, {'user' : 'guilherme', 'password' : 'senha'},
                {'user' : 'lucas', 'password' : 'senha'}, {'user' : 'yago', 'password' : 'senha'}]

class Login():

    def validade_user(self,username:str,password:str):
        for user in allowed_uses:
            if (user['user'] == username) and (user['password'] == password):
                return True
        
        return False