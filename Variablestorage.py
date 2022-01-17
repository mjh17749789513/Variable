__version__ = '1.0.0'
import pickle
def save_variable(v,filename):
    f=open(filename,'wb')
    pickle.dump(v,f)
    f.close()
    return filename
 
def load_variavle(filename):
   f=open(filename,'rb')
   r=pickle.load(f)
   f.close()
   return r
if __name__ == '__save_variable__':
    save_variable()
if __name__ == '__load_variavle__':
    load_variavle()
