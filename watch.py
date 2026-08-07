import re

def main():
    user=parse(input("HTML: "))
    if user :
        print(user)
    else :
        print('None')

def parse(s):
    exp = r'\<iframe(?:(?=.*?src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"))'
    # exp=r'\<iframe(?=[^>]*?src="https?://(?:www\.)?youtube\.com/embed/)[^>]*\>(?=\</iframe\>)'
    # exp=r'\<iframe(?=[^>]*?src="https?://(?:www\.)?youtube\.com/embed/)[^>]*\>\</iframe\>'
    if match:= re.search(exp,s.strip()) :
        # match=re.sub(r'^.*?https?://(?:www\.)?youtube\.com/embed/','',s.strip())
        # b=re.split(r'"',match)[0]
        b=match.group(1)
        return f'https://youtu.be/{b}'
    else :
        return None

if __name__ == "__main__":
    main()

# The fixed-width restriction only applies to lookbehind (?<=...).
# The outer (?:...) wrapping lookahead is redundant
# lookahead is already a special, self-contained assertion 
# that doesn't consume or capture text on its own
# [^"] :alone matches exactly one character, as long as that character isn't "
# [^"]+ :one or more repetitions of that same single-character rule
# which in practice means keep consuming characters until you hit a ", then stop