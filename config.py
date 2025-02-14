import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'Da2Nw3pIJhX3qL83MfKCCCPfQiEEq0D6')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'qmnfGd59rxkhn0OLX1jaaSkGRpt3HMC3')