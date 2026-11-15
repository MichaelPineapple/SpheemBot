#import json
#from typing import List
#
#import requests as requests
#
#from UserData import UserData
#from Utils import Utils
#
#
#class CommandHandler:
#
#    # COMMAND FUNCTIONS
#
#    # **** PAY ****
#    @staticmethod
#    def _cmd_pay(author: str, args: List[str]) -> str:
#
#        if len(args) > 1:
#
#            authorUsername: str = UserData.getUsername(author)
#
#            if authorUsername is not None:
#
#                authorPassword: str = UserData.getPassword(authorUsername)
#
#                if authorPassword is not None:
#
#                    recipientId: str = args[0]
#                    recipientDiscordName: str = UserData.getDiscordName(recipientId)
#
#                    recipientUsername: str = recipientId
#                    if recipientDiscordName is not None:
#                        recipientUsername = UserData.getUsername(recipientDiscordName)
#
#                    if recipientUsername is not None:
#
#                        amountStr = args[1]
#                        amountVal = Utils.parseAmount(amountStr)
#
#                        if amountVal > 0:
#
#                            requestData = {
#                                'username': authorUsername,
#                                'password': authorPassword,
#                                'recipient': recipientUsername,
#                                'amount': amountVal
#                            }
#
#                            response = requests.post('https://us-central1-spheem-2a540.cloudfunctions.net/pay', json=requestData)
#
#                            responseData = json.loads(response.content)
#                            resultCode = responseData['resultCode']
#                            if resultCode == 'SUCCESS':
#                                return "Payment Successful!"
#                            else:
#                                return "Payment Failed: "+resultCode
#                        else:
#                            return "Invalid Amount"
#                    else:
#                        return 'Recipient not found. They may not be registered with SpheemBot. Contact Mcl'
#                else:
#                    return 'Username not found. Contact Mcl'
#            else:
#                return 'You are not registered with SpheemBot. Contact Mcl'
#        else:
#            return "Invalid Parameters"
#
#
#
#
#    # **** BAL ****
#    @staticmethod
#    def _cmd_bal(author: str, args: List[str]) -> str:
#        authorUsername: str = UserData.getUsername(author)
#
#        if authorUsername is not None:
#
#            authorPassword: str = UserData.getPassword(authorUsername)
#
#            if authorPassword is not None:
#
#                requestData = {
#                    'username': authorUsername,
#                    'password': authorPassword,
#                }
#
#                response = requests.post('https://us-central1-spheem-2a540.cloudfunctions.net/login', json=requestData)
#                responseData = json.loads(response.content)
#                resultCode = responseData['resultCode']
#                balance = responseData['payload']
#                if resultCode == 'SUCCESS':
#                    return "Your Balance: " + str(balance)
#                else:
#                    return "Request Failed: "+resultCode
#            else:
#                return 'Username not found. Contact Mcl'
#        else:
#            return 'You are not registered with SpheemBot. Contact Mcl'
#
#
#
#
#
#
#    # **** KEK ****
#    @staticmethod
#    def _cmd_kek(author: str, args: List[str]) -> str:
#        return "cringe!"
#
#
#
#
#
#
#
#
#
#
#    _commandFunctionMap = {
#        'pay': _cmd_pay.__func__,
#        'bal': _cmd_bal.__func__,
#        'kek': _cmd_kek.__func__
#    }
#
#    @staticmethod
#    def getFunction(cmd: str):
#        return CommandHandler._commandFunctionMap.get(cmd)
