import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def abririmagen(TIF,indice):   
    im = Image.open('LC80090652013197LGN00/'+TIF)
    imarray = np.asarray(im)
    imrecortado = imarray[5000:6000,1000:2000]
    im.close()
    return imrecortado
    
    
def grafico(raster,ndvi,cursorx,cursory):
    
    fig = plt.figure()    
    fig, (ax1, ax2) = plt.subplots(1, 2)
    
    ax1.set_title('NDVI Map')
    ax1.plot(cursorx,cursory,'o',markersize=10,c='Yellow')
    ax1.imshow(ndvi)
    
    def prompixel(x,y,raster):
        return raster[y-1:y+2,x-1:x+2].mean()

    ax2.bar(([0,1,2,3,4,5,6,7,8,9,10]), 
            ([
                prompixel(cursorx,cursory,raster[:,:,0]), 
                prompixel(cursorx,cursory,raster[:,:,1]),
                prompixel(cursorx,cursory,raster[:,:,2]),
                prompixel(cursorx,cursory,raster[:,:,3]),
                prompixel(cursorx,cursory,raster[:,:,4]),
                prompixel(cursorx,cursory,raster[:,:,5]),
                prompixel(cursorx,cursory,raster[:,:,6]),
                prompixel(cursorx,cursory,raster[:,:,7]),
                prompixel(cursorx,cursory,raster[:,:,8]),
                prompixel(cursorx,cursory,raster[:,:,9]),
                prompixel(cursorx,cursory,raster[:,:,10])
            ]),log=True)
    ax2.set_ylim(0,45000)
    fig.set_size_inches(12,6)
    
    return plt.show()
