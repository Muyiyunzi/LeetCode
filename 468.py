class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        def judge4(ip):
            if not ip.isnumeric():
                return False
            if ip[0] == '0' and ip != '0':
                return False
            ip = int(ip)
            if not (0 <= ip <= 255):
                return False
            return True
        
        def judge6(ip):
            if not (1 <= len(ip) <=4):
                return False
            for i in ip:
                if not ('0' <= i <= '9' or 'a' <= i <= 'f' or 'A' <= i <= 'F'):
                    return False
            return True

        if '.' in queryIP:
            ips = queryIP.split('.')
            if len(ips) == 4:
                for ip in ips:
                    if not judge4(ip):
                        break
                else:
                    return 'IPv4'

        elif ':' in queryIP:
            ips = queryIP.split(':')
            if len(ips) == 8:
                for ip in ips:
                    if not judge6(ip):
                        break
                else:
                    return 'IPv6'
        
        return 'Neither'