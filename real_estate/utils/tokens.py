""" 
Logic related to the creation, validation and deletion of tokens
used for user activation authentication
"""
from real_estate.apps.agent.models import Agent
# Token scopes can be activation or authentication
SCOPE_ACTIVATION = 'activation'
SCOPE_AUTHENTICATION = 'authentication'


def generateToken(user_id, ttl, scope):
    """ 
    Inputs:
        user_id: the user_id of the user for which the token is generated for
        time-to-live (ttl): for how long the token will be valid. Usually 7 days for activation 
        scope: scope for which the token is intended for 
        
    Creates and saves an instance of the token models related to the user with the given user id
    """
    
    
    ...