class Codec:

    def __init__(self):
        self.alph = {
            "10":"A", "11":"B", "12":"C", "13":"D", "14":"E", "15":"F", "16":"G", "17":"H", "18":"I", "19":"J",
            "20":"K", "21":"L", "22":"M", "23":"N", "24":"O", "25":"P", "26":"Q", "27":"R", "28":"S", "29":"T",
            "30":"U", "31":"V", "32":"W", "33":"X", "34":"Y", "35":"Z", "36":"a", "37":"b", "38":"c", "39":"d",
            "40":"e", "41":"f", "42":"g", "43":"h", "44":"i", "45":"j", "46":"k", "47":"l", "48":"m", "49":"n",
            "50":"o", "51":"p", "52":"q", "53":"r", "54":"s", "55":"t", "56":"u", "57":"v", "58":"w", "59":"x",
            "60":"y", "61":"z", "62":"0", "63":"1", "64":"2", "65":"3", "66":"4", "67":"5", "68":"6", "69":"7",
            "70":"8", "71":"9", "72":"-", "73":"_", "74":".", "75":"~", "76":"/", "77":":", "78":"?", "79":"#",
            "80":"[", "81":"]", "82":"@", "83":"!", "84":"$", "85":"&", "86":"'", "87":"(", "88":")", "89":"*",
            "90":"+", "91":",", "92":";", "93":"=", "94":" "
        }
        self.alph2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~/:?#[]@!$&'()*+,;="

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        new = ""
        for i in longUrl:
            keys = [key for key, val in self.alph.items() if val == i]
            if len(keys):
                new += keys[0]
            else:
                return "Символ, используемый в сообщении недоступен, доступные символы: ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~/:?#[]@!$&'()*+,;="
        
        res = ""
        new = int(new)
        while new:
            res = self.alph2[(new%84)] + res
            new = new // 84

        return res
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        sm = 0 
        c = 0
        for i in reversed(shortUrl):
            if i in self.alph2:
                sm += self.alph2.find(i) * (84**c)
                c += 1
            else:
                return "Символ, используемый в сообщении недоступен, доступные символы: ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~/:?#[]@!$&'()*+,;="
        sm = str(sm)
        res = ""
        for i in range(0, len(sm), 2):
            res += self.alph[sm[i]+sm[i+1]]
        return res
