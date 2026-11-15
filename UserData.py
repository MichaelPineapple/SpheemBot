#class UserData:
#
#    _idMap = {
#        '<@313518347142823936>': '001000101#0',
#        '<@267401565483040790>': 'sir.puffles#0',
#        '<@120724995021209606>': 'oregoni#0',
#        '<@269876858374324225>': 'rep467#0',
#        '<@490551450200571914>': 'logan314159#0',
#        '<@1008977922247368704>': 'TEST',
#        '<@1009851528091283507>': 'The Bank of Spheem#0300',
#        '<@259863894389030913>': 'arur#0',
#        '<@121785309355573248>': 'gwebz#0'
#    }
#
#    _userMap = {
#        '001000101#0': 'WizlonPineapple',
#        'sir.puffles#0': 'SirPuffles',
#        'oregoni#0': 'Oregoni',
#        'rep467#0': '000',
#        'logan314159#0': 'Logan',
#        'The Bank of Spheem#0300': 'TheBank',
#        'arur#0': 'EpicSpheem5',
#        'gwebz#0': 'Gweb',
#        'TEST': 'test',
#    }
#
#    _passwordMap = {
#        'WizlonPineapple': '123qwasdzx',
#        'SirPuffles': 'Antartica14',
#        'Oregoni': 'penishat123',
#        '000': '000',
#        'Logan': 'Lh129036',
#        'TheBank': '3c2c3b35-5107-47b0-90c0-a8dbf7938ccc',
#        'EpicSpheem5': 'robert69',
#        'Gweb': 'yorio621'
#    }
#
#    @staticmethod
#    def getDiscordName(id: str) -> str:
#        return UserData._idMap.get(id)
#
#    @staticmethod
#    def getUsername(discordName) -> str:
#        return UserData._userMap.get(discordName)
#
#    @staticmethod
#    def getPassword(username) -> str:
#        return UserData._passwordMap.get(username)
