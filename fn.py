def my_up_upyun( name, byte, retry_time):
    upyun_pic = ''
    for j in range(retry_time):
        try:
            upyun_pic = up_to_upyun(name, byte)
            break
        except Exception as e:
            print "exception:", str(e)
    return upyun_pic

def get_pic_byte( src , retry_time):
    pic_byte = ''
    for j in range(retry_time):
        try:
            pic_byte = urllib2.urlopen(new_src).read()
            break
        except:
            pass
    return pic_byte