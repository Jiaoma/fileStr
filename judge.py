from collections.abc import Iterable
import numpy as np

def is_image_file(filename,
                  allow=('png','PNG','jpeg','JPEG','tif','TIF','jpg','JPG','gif','ppm','bmp')):
    if not isinstance(allow,list) or not isinstance(allow,tuple):
        allow=(allow),
    return any(filename.endswith(extension) for extension in allow)


def is_relative(keywords,needcheck):
    if keywords==None or not isinstance(keywords,Iterable):
        return
    if '<<' in keywords:
        keywords=list(keywords.split('<<'))
    if not isinstance(keywords,list):
        keywords=[keywords]
    for i in keywords:
        if i in needcheck:
            return True
    return False

def getLabelIndex(label:np.array,colorDict:dict):
    '''

    :param label: h,w,c
    :param colorDict: {(R,G,B):[index,name]}
    :return: h,w,1
    '''
    assert len(label.shape)==3 # h,w,c
    h,w,c=label.shape
    assert c==3
    label=label.reshape(-1,c)
    indexLabel=np.asarray([colorDict[tuple(i.tolist())][0] for i in label])
    indexLabel=indexLabel.reshape((h,w,1))
    return indexLabel

class labelConvert:
    def __init__(self,colorDict:dict):
        self.colorDict=colorDict
        self.index=[0 for _i in range(len(colorDict))]
        for key,value in colorDict.items():
            self.index[value[0]]=key

    def __call__(self,label:np.array):
        assert len(label.shape) == 3  # h,w,c
        h, w, c = label.shape
        assert c == 3
        label = label.reshape(-1, c)
        indexLabel = np.asarray([self.colorDict[tuple(i.tolist())][0] for i in label])
        indexLabel = indexLabel.reshape((h, w, 1))
        return indexLabel

    def goBack(self,label:np.array):
        # shape : n *1 *h*w
        n,c,h,w=label.shape
        assert c==1
        label=label.reshape(-1)
        labelNew=np.asarray([self.index[int(i)] for i in label])
        labelNew=labelNew.reshape(n,h,w,3)
        labelNew=np.transpose(labelNew,(0,3,1,2))
        return labelNew

if __name__=='__main__':
    print(is_relative("34_",'34_training.tif'))
    print(is_image_file('Image_01L_2ndHO.png',allow='jpg'))
    colorDict={(0,200,0):[0,'水田'],(150,250,0):[1,'水浇地'],
               (150,200,150):[2,'旱耕地'],(200,0,200):[3,'园地'],
               (150,0,250):[4,'乔木林地'],(150,150,250):[5,'灌木林地'],
               (250,200,0):[6,'天然草地'],(200,200,0):[7,'人工草地'],
               (200,0,0):[8,'工业用地'],(250,0,150):[9,'城市住宅'],
               (200,150,150):[10,'村镇住宅'],(250,150,150):[11,'交通运输'],
               (0,0,200):[12,'河流'],(0,150,200):[13,'湖泊'],
               (0,200,250):[14,'坑塘'],(0,0,0):[15,'其他类别']
               }
    import numpy as np
    b=np.zeros((2,2,3))
    b_=b.reshape(-1,3)
    label=[colorDict[tuple(i.tolist())] for i in b_]
    print(label)

    b=np.zeros((64,64,3))
    lc=labelConvert(colorDict)
    c=lc(b)
    print(c.shape)
    d=np.zeros((4,1,64,64))
    e=lc.goBack(d)
    print(e.shape)