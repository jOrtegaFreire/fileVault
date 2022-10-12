from aes import encrypted_data
from ntpath import basename

def read_file(path,mode=0):
    """!
    @brief   reads file as byte object
    if mode==1, file is encrypted an first 16 bytes are cipher iv
    @param   path, type string, path to file
    """
    with open(path,"rb") as f:
        if mode==1:
            iv=f.read(16)
        ct=f.read()
    if mode==1:
        return encrypted_data(iv=iv,ct=ct)
    else:return ct

def write_file(data,path,mode=0):
    """!
    @brief   reads file as byte object
    if mode==1, file is encrypted and is a encrypted_data type object 
    @param   data, data to write to file
    @param   path, type string, path to file
    """
    with open(path,"wb") as f:
        if mode==1:
            f.write(data.iv)
            f.write(data.ct)
        else:f.write(data)
        


